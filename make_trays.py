from PIL import Image
import os

input_files = ['./static/dist/sticker_001.webp', './static/dist/sticker_002.webp', './static/dist/sticker_003.webp']

print("Initiating tray icon generation...")

for index, file in enumerate(input_files):
    if not os.path.exists(file):
        print(f"Error: Could not find {file}. Make sure it is in the same directory.")
        continue
        
    try:
        # Open the image
        img = Image.open(file)
        
        # WhatsApp strictly enforces 96x96 pixels for tray icons
        img = img.resize((96, 96), Image.Resampling.LANCZOS)
        
        # Save as PNG with optimization to ensure it stays well under the 50kb limit
        output_name = f'tray_{index + 1}.png'
        img.save(output_name, 'PNG', optimize=True)
        
        # Verify file size
        size_kb = os.path.getsize(output_name) / 1024
        print(f"Success: {output_name} generated at {size_kb:.2f} KB.")
        
    except Exception as e:
        print(f"Failed to process {file}: {e}")

print("Pipeline closed.")