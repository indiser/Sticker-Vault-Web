import json
import os
from pathlib import Path

# Configuration
DIST_DIR = Path('./static/dist')
MANIFEST_FILE = 'contents.json'
MAX_STICKERS_PER_PACK = 30

def generate_whatsapp_manifest():
    if not DIST_DIR.exists():
        print("Error: /dist directory not found.")
        return

    # Get all webp files and sort them to maintain order
    stickers = sorted([f.name for f in DIST_DIR.glob('*.webp')])
    total_stickers = len(stickers)
    
    if total_stickers == 0:
        print("No stickers found in /dist.")
        return

    # Chunk the stickers into groups of 30
    chunks = [stickers[i:i + MAX_STICKERS_PER_PACK] for i in range(0, total_stickers, MAX_STICKERS_PER_PACK)]
    
    sticker_packs = []

    for index, chunk in enumerate(chunks):
        pack_id = str(index + 1)
        
        # Build the sticker array for this specific chunk
        pack_stickers = []
        for sticker_file in chunk:
            pack_stickers.append({
                "image_file": sticker_file,
                "emojis": ["🔥", "😎"] # WhatsApp requires at least one emoji per sticker
            })

        # Build the pack metadata
        pack_data = {
            "identifier": pack_id,
            "name": f"Sticker Vault Vol. {pack_id}",
            "publisher": "Indiser",
            "tray_image_file": f"tray_{pack_id}.png", # Critical requirement
            "image_data_version": "1",
            "avoid_cache": False,
            "publisher_email": "",
            "publisher_website": "",
            "privacy_policy_website": "",
            "license_agreement_website": "",
            "stickers": pack_stickers
        }
        
        sticker_packs.append(pack_data)

    # Wrap in the final WhatsApp schema
    final_json = {
        "android_play_store_link": "",
        "ios_app_store_link": "",
        "sticker_packs": sticker_packs
    }

    # Export
    with open(MANIFEST_FILE, 'w', encoding="utf-8") as f:
        json.dump(final_json, f, indent=2, ensure_ascii=False)

    print(f"Success. Generated contents.json with {len(chunks)} packs for {total_stickers} total stickers.")

if __name__ == '__main__':
    generate_whatsapp_manifest()