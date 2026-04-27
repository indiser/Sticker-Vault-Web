import os
import hashlib
import shutil
import json
from pathlib import Path

INPUT_DIR = Path('stickers')
OUTPUT_DIR = Path('dist')
MANIFEST_FILE = OUTPUT_DIR / 'stickers.json'

def get_file_hash(filepath):
    """Generate SHA-256 hash to detect duplicate stickers."""
    hasher = hashlib.sha256()
    with open(filepath, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()

def process_stickers():
    OUTPUT_DIR.mkdir(exist_ok=True)
    seen_hashes = set()
    manifest = []
    counter = 1

    print("Initiating build pipeline...")

    for file_path in INPUT_DIR.glob('*.webp'):
        file_hash = get_file_hash(file_path)
        
        # Deduplication check
        if file_hash in seen_hashes:
            print(f"Duplicate detected and destroyed: {file_path.name}")
            continue
            
        seen_hashes.add(file_hash)
        
        # Rename and move to deployment folder
        new_filename = f"sticker_{counter:03d}.webp"
        output_path = OUTPUT_DIR / new_filename
        shutil.copy2(file_path, output_path)
        
        # Add to manifest
        manifest.append({
            "id": counter,
            "src": new_filename
        })
        
        counter += 1

    # Generate the JSON manifest
    with open(MANIFEST_FILE, 'w') as f:
        json.dump(manifest, f, indent=4)

    print(f"Pipeline complete. {len(manifest)} unique stickers processed and staged in /dist.")

if __name__ == '__main__':
    process_stickers()