#!/usr/bin/env python3
"""
Script pour nettoyer et restructurer le fichier Markdown
en respectant strictement la hiérarchie et le formatage.
"""

import re
import argparse
from datetime import datetime
from pathlib import Path
from typing import List, Tuple

class MarkdownCleaner:
    def __init__(self, target_file: str, output_file: str = None):
        self.target_file = Path(target_file)
        self.output_file = Path(output_file) if output_file else self.target_file
        self.content = ""
        self.lines = []
        
    def log(self, message: str):
        """Affiche un message avec horodatage."""
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"[{timestamp}] {message}")
        
    def load_file(self):
        """Charge le fichier Markdown."""
        with open(self.target_file, 'r', encoding='utf-8') as f:
            self.content = f.read()
            self.lines = self.content.split('\n')
        self.log(f"Fichier chargé: {len(self.lines)} lignes")
        
    def create_backup(self):
        """Crée une sauvegarde du fichier."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_file = self.target_file.parent / f"{self.target_file.stem}.backup-{timestamp}.md"
        with open(backup_file, 'w', encoding='utf-8') as f:
            f.write(self.content)
        self.log(f"Backup créé: {backup_file.name}")
        
    def clean_definitions(self):
        """Nettoie les sections Définitions mal formatées."""
        new_lines = []
        in_definition = False
        definition_buffer = []
        
        for i, line in enumerate(self.lines):
            # Détection d'une section Définitions
            if re.match(r'^#### Définitions \(.*?\)\s*$', line):
                # Sauvegarder la ligne de titre
                new_lines.append(line)
                in_definition = True
                definition_buffer = []
                continue
                
            # Détection de la fin de la section
            if in_definition and re.match(r'^####', line):
                # Traiter le buffer avant de continuer
                cleaned_content = self.process_definition_buffer(definition_buffer)
                if cleaned_content:
                    new_lines.extend(cleaned_content)
                    new_lines.append("")  # Ligne vide après le contenu
                in_definition = False
                new_lines.append(line)
                continue
                
            # Accumulation du contenu de la définition
            if in_definition:
                definition_buffer.append(line)
            else:
                new_lines.append(line)
                
        # Traiter le dernier buffer si nécessaire
        if in_definition and definition_buffer:
            cleaned_content = self.process_definition_buffer(definition_buffer)
            if cleaned_content:
                new_lines.extend(cleaned_content)
                
        self.lines = new_lines
        self.log("Sections Définitions nettoyées")
        
    def process_definition_buffer(self, buffer: List[str]) -> List[str]:
        """
        Traite le contenu d'une section Définition pour le nettoyer.
        """
        cleaned = []
        skip_next = False
        
        for line in buffer:
            # Supprimer les faux titres markdown
            line = re.sub(r'^\*\*\d+\.\s+.*?\*\*$', '', line)
            line = re.sub(r'^##\s+\d+\.\d+\s+', '', line)
            line = re.sub(r'^##\s+', '', line)
            
            # Garder seulement le contenu valide
            if line.strip() and not line.strip().startswith('##'):
                # Nettoyer les caractères bizarres
                line = line.replace('â€™', "'")
                line = line.replace('â€"', "—")
                line = line.replace('Ã©', "é")
                line = line.replace('Ã¨', "è")
                line = line.replace('Ãª', "ê")
                line = line.replace('Ã ', "à")
                line = line.replace('Ã§', "ç")
                line = line.replace('Ã´', "ô")
                line = line.replace('Ã»', "û")
                
                # Si c'est un placeholder, le garder tel quel
                if '<!-- à remplir -->' in line or '<-type f -iname' in line:
                    cleaned.append('<!-- à remplir -->')
                else:
                    cleaned.append(line)
                    
        return cleaned
        
    def fix_rules_and_options(self):
        """Corrige le formatage des sections Règles et Options."""
        new_lines = []
        
        for i, line in enumerate(self.lines):
            # Nettoyer les sous-titres mal formatés dans Règles et Options
            if re.match(r'^##### (Exigences|Conformité|Standardisation|Variantes|Perspectives|Environnements|Conventions|Modes|Sécurité|Cas)', line):
                # Garder ces sous-sections mais avec un formatage propre
                new_lines.append(line)
            elif re.match(r'^#### (Règles|Options) \(.*?\)\s*$', line):
                new_lines.append(line)
                # Vérifier si la ligne suivante est vide ou un placeholder
                if i + 1 < len(self.lines):
                    next_line = self.lines[i + 1].strip()
                    if not next_line or '<!-- à remplir -->' in next_line or '<-type f -iname' in next_line:
                        new_lines.append('<!-- à remplir -->')
                        new_lines.append('')
            else:
                new_lines.append(line)
                
        self.lines = new_lines
        self.log("Sections Règles et Options corrigées")
        
    def ensure_spacing(self):
        """Assure un espacement correct entre les sections."""
        new_lines = []
        prev_was_header = False
        
        for line in self.lines:
            # Détection des headers
            is_header = bool(re.match(r'^#{1,6}\s+', line))
            
            # Ajouter une ligne vide avant les headers (sauf le premier)
            if is_header and not prev_was_header and new_lines:
                if new_lines[-1].strip():  # Si la ligne précédente n'est pas vide
                    new_lines.append('')
                    
            new_lines.append(line)
            prev_was_header = is_header
            
        self.lines = new_lines
        self.log("Espacement corrigé")
        
    def remove_duplicate_sections(self):
        """Supprime les sections en double."""
        seen_sections = set()
        new_lines = []
        current_section = None
        skip_until_next_section = False
        
        for line in self.lines:
            # Détection d'une nouvelle section niveau 3
            match = re.match(r'^### (.+?)$', line)
            if match:
                section_name = match.group(1).strip()
                section_key = section_name.upper().replace(' ', '_')
                
                if section_key in seen_sections:
                    self.log(f"Section dupliquée ignorée: {section_name}")
                    skip_until_next_section = True
                    continue
                else:
                    seen_sections.add(section_key)
                    skip_until_next_section = False
                    current_section = section_name
                    
            if not skip_until_next_section:
                new_lines.append(line)
                
        self.lines = new_lines
        self.log("Sections dupliquées supprimées")
        
    def save_file(self):
        """Sauvegarde le fichier nettoyé."""
        self.content = '\n'.join(self.lines)
        
        # Corrections finales
        self.content = re.sub(r'\n{3,}', '\n\n', self.content)  # Max 2 lignes vides
        self.content = re.sub(r'[ \t]+$', '', self.content, flags=re.MULTILINE)  # Supprimer espaces fin de ligne
        
        with open(self.output_file, 'w', encoding='utf-8') as f:
            f.write(self.content)
        self.log(f"Fichier sauvegardé: {self.output_file}")
        
    def run(self):
        """Exécute le processus de nettoyage complet."""
        self.log("Démarrage du nettoyage du fichier Markdown")
        
        self.load_file()
        self.create_backup()
        
        self.log("Nettoyage en cours...")
        self.clean_definitions()
        self.fix_rules_and_options()
        self.remove_duplicate_sections()
        self.ensure_spacing()
        
        self.save_file()
        
        self.log("Nettoyage terminé avec succès")
        
        # Rapport
        print("\n" + "="*50)
        print("RAPPORT DE NETTOYAGE")
        print("="*50)
        print(f"Fichier source    : {self.target_file}")
        print(f"Fichier nettoyé   : {self.output_file}")
        print(f"Lignes traitées   : {len(self.lines)}")
        print("="*50)


def main():
    parser = argparse.ArgumentParser(description='Nettoie et restructure un fichier Markdown')
    parser.add_argument('--target', required=True, help='Fichier Markdown à nettoyer')
    parser.add_argument('--output', help='Fichier de sortie (par défaut: remplace le fichier source)')
    
    args = parser.parse_args()
    
    cleaner = MarkdownCleaner(args.target, args.output)
    cleaner.run()


if __name__ == '__main__':
    main()