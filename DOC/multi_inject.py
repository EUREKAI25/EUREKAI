#!/usr/bin/env python3
"""
Script d'injection JSON vers Markdown pour la documentation ZORBEC.
Insère le contenu de fichiers JSON dans les sections correspondantes d'un fichier Markdown.
Version corrigée pour l'ordre des sections et l'injection du contenu.
"""

import json
import os
import re
import argparse
import shutil
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple
import unicodedata


class MarkdownInjector:
    """Gère l'injection de contenu JSON dans un fichier Markdown structuré."""
    
    def __init__(self, json_dir: str, target_file: str, dry_run: bool = False):
        self.json_dir = Path(json_dir)
        self.target_file = Path(target_file)
        self.dry_run = dry_run
        self.backup_file = None
        self.logs = []
        self.sections_created = []
        self.content_injected = []
        
    def normalize_text(self, text: str) -> str:
        """Normalise les accents pour éviter les problèmes de comparaison."""
        return unicodedata.normalize('NFC', text)
    
    def log(self, level: str, message: str):
        """Ajoute un message de log."""
        timestamp = datetime.now().strftime("%H:%M:%S")
        log_msg = f"[{timestamp}] [{level}] {message}"
        self.logs.append(log_msg)
        print(log_msg)
    
    def create_backup(self):
        """Crée une sauvegarde du fichier cible."""
        if not self.target_file.exists():
            self.log("ERROR", f"Fichier cible introuvable: {self.target_file}")
            return False
            
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_name = f"{self.target_file.stem}.bak-{timestamp}{self.target_file.suffix}"
        self.backup_file = self.target_file.parent / backup_name
        
        try:
            shutil.copy2(self.target_file, self.backup_file)
            self.log("BACKUP", f"Sauvegarde créée: {self.backup_file}")
            return True
        except Exception as e:
            self.log("ERROR", f"Échec de la sauvegarde: {e}")
            return False
    
    def load_json_files(self) -> List[Dict]:
        """Charge tous les fichiers JSON du répertoire."""
        json_data = []
        
        if not self.json_dir.exists():
            self.log("ERROR", f"Répertoire JSON introuvable: {self.json_dir}")
            return json_data
        
        for json_file in sorted(self.json_dir.glob("*.json")):
            try:
                with open(json_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    
                # Détecter le format et normaliser
                normalized_data = self.normalize_json_format(data, json_file.name)
                if normalized_data:
                    json_data.append(normalized_data)
                    
            except json.JSONDecodeError as e:
                self.log("ERROR", f"JSON invalide: {json_file.name} - {e}")
            except Exception as e:
                self.log("ERROR", f"Erreur lecture {json_file.name}: {e}")
        
        return json_data
    
    def normalize_json_format(self, data: Dict, filename: str) -> Optional[Dict]:
        """Normalise les différents formats JSON en un format commun."""
        normalized = {'_filename': filename}
        
        # Format 1: avec 'category' et 'sections' liste (LAYERS.json, ETHIQUE.json)
        if 'category' in data and isinstance(data.get('sections'), list):
            normalized['category'] = self.normalize_text(data['category']).upper()
            normalized['sections'] = data['sections']
            return normalized
        
        # Format 2: avec 'sections' dict imbriqué
        elif 'category' in data and isinstance(data.get('sections'), dict):
            normalized['category'] = self.normalize_text(data['category']).upper()
            # Convertir le dict en liste de sections
            sections = []
            for vector_type in ['identité', 'vue', 'contexte']:
                if vector_type in data['sections']:
                    vector_data = data['sections'][vector_type]
                    for part in ['Définitions', 'Règles', 'Options']:
                        if part in vector_data:
                            sections.append({
                                'vector': vector_type,
                                'part': part,
                                'content': vector_data[part]
                            })
            normalized['sections'] = sections
            return normalized
        
        # Format 3: Structure simple - créer sections vides
        elif 'src' in data or 'target' in data:
            category = filename.replace('.json', '').upper()
            normalized['category'] = self.normalize_text(category)
            normalized['sections'] = []
            return normalized
        
        # Format 4: AGENCE.json - skip pour l'instant
        elif 'source' in data or filename.startswith('AGENCE'):
            self.log("INFO", f"Format AGENCE détecté pour {filename}, skipping")
            return None
        
        # Essayer d'extraire un nom de catégorie du fichier
        category = filename.replace('.json', '').replace('_', ' ').upper()
        if category:
            normalized['category'] = self.normalize_text(category)
            normalized['sections'] = []
            return normalized
        
        self.log("WARNING", f"Format non reconnu pour {filename}")
        return None
    
    def find_section_bounds(self, lines: List[str], level: int, title: str) -> Tuple[int, int]:
        """Trouve les limites d'une section dans le Markdown."""
        title_norm = self.normalize_text(title)
        pattern = r'^' + '#' * level + r'\s+' + re.escape(title_norm) + r'\b'
        
        start = -1
        end = len(lines)
        
        for i, line in enumerate(lines):
            line_norm = self.normalize_text(line)
            if re.match(pattern, line_norm, re.IGNORECASE):
                start = i
                break
        
        if start == -1:
            return (-1, -1)
        
        # Trouver la fin de la section
        for i in range(start + 1, len(lines)):
            if lines[i].strip().startswith('#'):
                level_count = len(lines[i].split()[0])
                if level_count <= level:
                    end = i
                    break
        
        return (start, end)
    
    def ensure_section_exists(self, lines: List[str], category: str) -> bool:
        """S'assure que la section de catégorie existe dans toutes les dimensions."""
        modified = False
        
        # Les trois dimensions principales
        dimensions = [
            ('## 1.1 Identité', 'identité'),
            ('## 1.2 Vue', 'vue'),
            ('## 1.3 Contexte', 'contexte')
        ]
        
        for dim_title, dim_name in dimensions:
            # Trouver la dimension
            dim_start, dim_end = self.find_section_bounds(lines, 2, dim_title.replace('## ', ''))
            
            if dim_start == -1:
                self.log("ERROR", f"Dimension {dim_title} non trouvée!")
                continue
            
            # Chercher la catégorie dans cette dimension
            cat_pattern = r'^###\s+' + re.escape(category) + r'\b'
            cat_found = False
            
            for i in range(dim_start + 1, dim_end):
                if re.match(cat_pattern, self.normalize_text(lines[i]), re.IGNORECASE):
                    cat_found = True
                    break
            
            # Si la catégorie n'existe pas, la créer
            if not cat_found:
                self.log("INFO", f"Création de la section {category} dans {dim_title}")
                
                # Trouver où insérer (juste avant la prochaine section ### ou à la fin de la dimension)
                insert_pos = dim_end
                for i in range(dim_start + 1, dim_end):
                    if lines[i].strip().startswith('###'):
                        # On a trouvé une section, chercher la fin de celle-ci
                        for j in range(i + 1, dim_end):
                            if lines[j].strip().startswith('###'):
                                insert_pos = j
                                break
                        else:
                            insert_pos = dim_end
                        break
                else:
                    # Pas de section trouvée, insérer après le titre
                    insert_pos = dim_start + 1
                    # S'il y a un commentaire après le titre, insérer après
                    if insert_pos < len(lines) and lines[insert_pos].strip().startswith('<!--'):
                        insert_pos += 1
                
                # Créer la structure complète de la catégorie (ordre correct)
                new_lines = [
                    f"### {category} <!-- SECTION:{category} -->",
                    f"#### Définitions ({dim_name})",
                    "<!-- à remplir -->",
                    "",
                    f"#### Règles ({dim_name})",
                    "<!-- à remplir -->",
                    "",
                    f"#### Options ({dim_name})",
                    "<!-- à remplir -->"
                ]
                
                # Insérer les nouvelles lignes
                for j, line in enumerate(new_lines):
                    lines.insert(insert_pos + j, line)
                
                modified = True
                self.sections_created.append(f"{category} dans {dim_title}")
        
        return modified
    
    def inject_content_in_section(self, lines: List[str], category: str, 
                                 section_type: str, content_type: str, 
                                 content: str) -> bool:
        """Injecte le contenu dans une sous-section spécifique."""
        # Normaliser les types
        if section_type in ['identité', 'identite']:
            section_type = 'identité'
            main_section = '1.1 Identité'
        elif section_type == 'vue':
            main_section = '1.2 Vue'
        elif section_type == 'contexte':
            main_section = '1.3 Contexte'
        else:
            return False
        
        # Normaliser le type de contenu
        content_type_normalized = content_type
        if content_type.lower() in ['définitions', 'definitions']:
            content_type_normalized = 'Définitions'
        elif content_type.lower() in ['règles', 'regles']:
            content_type_normalized = 'Règles'
        elif content_type.lower() == 'options':
            content_type_normalized = 'Options'
        
        # Trouver la section principale
        main_start, main_end = self.find_section_bounds(lines, 2, main_section)
        if main_start == -1:
            self.log("WARNING", f"Section principale {main_section} non trouvée")
            return False
        
        # Trouver la catégorie
        cat_pattern = r'^###\s+' + re.escape(category) + r'\b'
        cat_start = -1
        
        for i in range(main_start + 1, main_end):
            if re.match(cat_pattern, self.normalize_text(lines[i]), re.IGNORECASE):
                cat_start = i
                break
        
        if cat_start == -1:
            self.log("WARNING", f"Catégorie {category} non trouvée dans {main_section}")
            return False
        
        # Trouver la fin de la catégorie
        cat_end = main_end
        for i in range(cat_start + 1, main_end):
            if lines[i].strip().startswith('###'):
                cat_end = i
                break
        
        # Trouver la sous-section (Définitions, Règles, Options)
        subsection_pattern = r'^####\s+' + re.escape(content_type_normalized) + r'\s*\(' + re.escape(section_type) + r'\)'
        
        for i in range(cat_start + 1, cat_end):
            if re.match(subsection_pattern, self.normalize_text(lines[i]), re.IGNORECASE):
                # Trouver la fin de cette sous-section
                end_idx = cat_end
                for j in range(i + 1, cat_end):
                    if lines[j].strip().startswith('####'):
                        end_idx = j
                        break
                
                # Vérifier si le contenu actuel est juste "<!-- à remplir -->"
                current_content = []
                for j in range(i + 1, end_idx):
                    current_content.append(lines[j])
                
                # Si le contenu actuel est vide ou juste un commentaire "à remplir"
                is_empty = len(current_content) == 0 or \
                          (len(current_content) == 1 and '<!-- à remplir -->' in current_content[0])
                
                if is_empty and content.strip():
                    # Remplacer le contenu
                    del lines[i + 1:end_idx]
                    
                    # Insérer le nouveau contenu
                    content_lines = content.strip().split('\n')
                    for k, line in enumerate(content_lines):
                        lines.insert(i + 1 + k, line)
                    
                    self.content_injected.append(f"{category}/{section_type}/{content_type_normalized}")
                    return True
                elif not is_empty:
                    self.log("DEBUG", f"Contenu déjà présent pour {category}/{section_type}/{content_type_normalized}")
        
        return False
    
    def process_json_data(self, json_data: Dict, lines: List[str]) -> bool:
        """Traite un fichier JSON et injecte son contenu dans le Markdown."""
        category = json_data.get('category', '').upper()
        sections = json_data.get('sections', [])
        filename = json_data.get('_filename', 'unknown.json')
        
        if not category:
            self.log("WARNING", f"Pas de catégorie pour {filename}")
            return False
        
        # S'assurer que la section existe
        section_created = self.ensure_section_exists(lines, category)
        
        any_modified = section_created
        
        # Traiter chaque section
        for section in sections:
            if isinstance(section, dict):
                vector = section.get('vector', '').lower()
                part = section.get('part', '')
                content = section.get('content', '')
                
                if vector and part and content:
                    if self.inject_content_in_section(lines, category, vector, part, content):
                        any_modified = True
                        self.log("OK", f"Contenu injecté: {category}/{vector}/{part}")
        
        if any_modified:
            self.log("SUCCESS", f"Traité: {filename}")
        else:
            self.log("INFO", f"Aucun changement: {filename}")
        
        return any_modified
    
    def run(self):
        """Exécute le processus d'injection."""
        # Créer une sauvegarde
        if not self.dry_run and not self.create_backup():
            return False
        
        # Charger les fichiers JSON
        json_files = self.load_json_files()
        if not json_files:
            self.log("WARNING", "Aucun fichier JSON valide trouvé")
            return False
        
        self.log("INFO", f"Chargé {len(json_files)} fichiers JSON")
        
        # Lire le fichier Markdown
        try:
            with open(self.target_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            lines = [line.rstrip('\n') for line in lines]
        except Exception as e:
            self.log("ERROR", f"Impossible de lire {self.target_file}: {e}")
            return False
        
        # Traiter chaque fichier JSON
        any_changes = False
        for json_data in json_files:
            if self.process_json_data(json_data, lines):
                any_changes = True
        
        # Écrire le fichier modifié (PAS le backup!)
        if not self.dry_run and any_changes:
            try:
                with open(self.target_file, 'w', encoding='utf-8') as f:
                    for line in lines:
                        f.write(line + '\n')
                self.log("SUCCESS", f"Fichier mis à jour: {self.target_file}")
            except Exception as e:
                self.log("ERROR", f"Impossible d'écrire {self.target_file}: {e}")
                return False
        elif self.dry_run:
            self.log("INFO", "Mode dry-run: aucune modification effectuée")
        elif not any_changes:
            self.log("INFO", "Aucun changement nécessaire")
        
        # Afficher le résumé
        if self.sections_created:
            print("\n=== SECTIONS CRÉÉES ===")
            for section in self.sections_created:
                print(f"  - {section}")
        
        if self.content_injected:
            print("\n=== CONTENU INJECTÉ ===")
            for content in self.content_injected:
                print(f"  - {content}")
        
        return True


def main():
    """Point d'entrée principal du script."""
    parser = argparse.ArgumentParser(
        description="Injecte le contenu de fichiers JSON dans un fichier Markdown structuré"
    )
    parser.add_argument(
        '--json-dir',
        required=True,
        help="Répertoire contenant les fichiers JSON"
    )
    parser.add_argument(
        '--target',
        required=True,
        help="Fichier Markdown cible"
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help="Mode test: affiche les changements sans modifier le fichier"
    )
    
    args = parser.parse_args()
    
    # Créer et exécuter l'injecteur
    injector = MarkdownInjector(
        json_dir=args.json_dir,
        target_file=args.target,
        dry_run=args.dry_run
    )
    
    success = injector.run()
    
    # Afficher le résumé
    print("\n=== RÉSUMÉ ===")
    print(f"Statut: {'SUCCÈS' if success else 'ÉCHEC'}")
    print(f"Fichiers JSON traités: {len(injector.logs)}")
    
    return 0 if success else 1


if __name__ == "__main__":
    exit(main())