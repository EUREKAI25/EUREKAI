#!/usr/bin/env python3
"""
Script d'injection complète - lit et injecte TOUS les JSON
"""

import json
import re
from pathlib import Path
from datetime import datetime

def fix_encoding(text):
    """Corrige l'encodage UTF-8 mal interprété"""
    # Remplacements simples sans caractères problématiques
    fixes = {
        'Ã©': 'é', 'Ã¨': 'è', 'Ãª': 'ê', 'Ã ': 'à',
        'Ã¢': 'â', 'Ã´': 'ô', 'Ã»': 'û', 'Ã§': 'ç',
        'Ã‰': 'É', 'Ãˆ': 'È', 'Ã€': 'À', 'Ã‡': 'Ç',
        'Ã®': 'î', 'Ã¯': 'ï', 'Ã¹': 'ù', 'Ã¼': 'ü',
        'Ã"': 'Ô', 'Ãœ': 'Ü', 'ÃŽ': 'Î', 'Ã‹': 'Ë'
    }
    
    for old, new in fixes.items():
        text = text.replace(old, new)
    
    return text

def load_all_json_content(json_dir):
    """Charge tout le contenu des fichiers JSON"""
    all_data = {}
    json_path = Path(json_dir)
    
    if not json_path.exists():
        print(f"❌ Dossier JSON non trouvé: {json_dir}")
        return all_data
    
    print(f"📚 Chargement des fichiers JSON...")
    
    for json_file in json_path.glob("*.json"):
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Déterminer le nom de la section
            section_name = None
            if 'category' in data:
                section_name = data['category']
            elif 'area' in data:
                section_name = data['area']
            else:
                # Utiliser le nom du fichier
                section_name = json_file.stem.upper().replace('_', ' ')
            
            # Nettoyer le nom (enlever les chiffres à la fin)
            section_name = re.sub(r'\d+$', '', section_name).strip()
            
            if section_name not in all_data:
                all_data[section_name] = []
            
            # Extraire le contenu des sections
            if 'sections' in data and isinstance(data['sections'], list):
                for section in data['sections']:
                    if 'content' in section and section['content']:
                        all_data[section_name].append({
                            'vector': section.get('vector', 'identité'),
                            'part': section.get('part', 'Définitions'),
                            'content': section['content']
                        })
                        
            print(f"   ✅ {section_name}: {len(all_data.get(section_name, []))} contenus")
                        
        except Exception as e:
            print(f"   ⚠️ Erreur {json_file.name}: {e}")
    
    return all_data

def inject_into_md(md_file, all_json_data):
    """Injecte le contenu JSON dans le fichier MD"""
    
    # Backup
    backup_path = f"{md_file}.backup-{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    Path(md_file).rename(backup_path)
    print(f"\n✅ Backup: {backup_path}")
    
    with open(backup_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Corriger l'encodage
    content = fix_encoding(content)
    
    print(f"📝 Injection du contenu...")
    injected_count = 0
    
    # Pour chaque section avec du contenu JSON
    for section_name, json_sections in all_json_data.items():
        for json_section in json_sections:
            vector = json_section['vector']
            part = json_section['part']
            new_content = json_section['content']
            
            # Nettoyer le contenu
            # Remplacer # par ** pour éviter les conflits avec la hiérarchie MD
            new_content = re.sub(r'^#\s+(\d+\.)', r'**\1', new_content, flags=re.MULTILINE)
            new_content = re.sub(r'\n#\s+(\d+\.)', r'\n\n**\1', new_content)
            
            # Pattern pour trouver la section à remplacer
            # Chercher : ### SECTION ... #### Part (vector) ... jusqu'à la prochaine section
            pattern = (
                rf'(###\s+{re.escape(section_name)}\s*(?:<!--.*?-->)?\s*\n'
                rf'(?:.*?\n)*?'
                rf'####\s+{re.escape(part)}\s*\({re.escape(vector)}\)\s*\n)'
                rf'(.*?)'
                rf'(?=\n####|\n###|\n##|\n#\s|\Z)'
            )
            
            def replacer(match):
                header = match.group(1)
                existing_content = match.group(2)
                
                # Si c'est vide ou "à remplir", remplacer
                if '<!-- à remplir -->' in existing_content or not existing_content.strip():
                    injected_count_local = 1
                    print(f"   💉 {section_name}/{vector}/{part}")
                    return header + new_content + '\n'
                
                # Sinon, garder l'existant
                return match.group(0)
            
            # Appliquer le remplacement
            new_content_full = re.sub(pattern, replacer, content, flags=re.DOTALL)
            
            if new_content_full != content:
                content = new_content_full
                injected_count += 1
    
    # Écrire le fichier mis à jour
    with open(md_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"\n✅ {injected_count} sections injectées")
    
    # Statistiques finales
    lines = content.splitlines()
    empty_count = content.count('<!-- à remplir -->')
    
    print(f"\n📊 Statistiques finales:")
    print(f"   - Lignes: {len(lines)}")
    print(f"   - Sections vides: {empty_count}")
    print(f"   - Taille: {len(content):,} caractères")
    
    return md_file

def main():
    """Point d'entrée principal"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Injecter le contenu JSON dans le MD')
    parser.add_argument('--target', default='trame_IN_PROGRESS.md', help='Fichier cible')
    parser.add_argument('--json-dir', default='../json', help='Dossier des JSON')
    
    args = parser.parse_args()
    
    print("="*60)
    print("INJECTION COMPLÈTE DES CONTENUS JSON")
    print("="*60)
    print()
    
    # Vérifier que le fichier cible existe
    if not Path(args.target).exists():
        print(f"❌ Fichier non trouvé: {args.target}")
        # Chercher un backup récent
        backups = list(Path('.').glob(f"{args.target}.backup-*"))
        if backups:
            latest = max(backups, key=lambda x: x.stat().st_mtime)
            print(f"   Utilisation du backup: {latest}")
            latest.rename(args.target)
        else:
            print("   Aucun backup trouvé!")
            return
    
    # Charger tous les JSON
    all_json_data = load_all_json_content(args.json_dir)
    
    if not all_json_data:
        print("❌ Aucun contenu JSON trouvé!")
        return
    
    # Injecter dans le MD
    inject_into_md(args.target, all_json_data)
    
    print("\n✨ Terminé!")
    print("\n💡 Pour vérifier:")
    print(f"   head -100 {args.target}")
    print(f"   grep -A 5 '### LAYERS' {args.target}")
    print(f"   grep -c '<!-- à remplir -->' {args.target}")

if __name__ == "__main__":
    main()