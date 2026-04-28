import os
from PIL import Image

def build_whatsapp_stickers(input_dir="raw_images", output_dir="stickers_ready"):
    """
    Converts PNG/JPG images to WhatsApp-compliant WebP stickers.
    Forces 512x512 dimensions with transparent padding.
    """
    # Create directories if you haven't already
    if not os.path.exists(input_dir):
        os.makedirs(input_dir)
        print(f"Created '{input_dir}' directory. Drop your raw images there and rerun.")
        return
        
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    valid_extensions = {".png", ".jpg", ".jpeg"}
    processed_count = 0
    
    for filename in os.listdir(input_dir):
        ext = os.path.splitext(filename)[1].lower()
        if ext not in valid_extensions:
            continue
            
        input_path = os.path.join(input_dir, filename)
        output_filename = os.path.splitext(filename)[0] + ".webp"
        output_path = os.path.join(output_dir, output_filename)
        
        try:
            with Image.open(input_path) as img:
                # Force RGBA for the transparency channel
                img = img.convert("RGBA")
                
                # Resize proportionally to fit inside a 512x512 box
                img.thumbnail((512, 512), Image.Resampling.LANCZOS)
                
                # Create a blank 512x512 transparent canvas
                canvas = Image.new("RGBA", (512, 512), (255, 255, 255, 0))
                
                # Calculate center position to paste the resized image
                paste_x = (512 - img.width) // 2
                paste_y = (512 - img.height) // 2
                canvas.paste(img, (paste_x, paste_y), img) # Use img as its own mask
                
                # Save as WebP with WhatsApp constraints (quality=80 keeps it under 100KB)
                canvas.save(output_path, "webp", quality=80, method=6)
                
                print(f"[SUCCESS] Processed: {filename}")
                processed_count += 1
                
        except Exception as e:
            print(f"[FAILED] Could not process {filename}: {e}")
            
    print(f"\nExecution Complete. {processed_count} stickers generated in '{output_dir}'.")

if __name__ == "__main__":
    build_whatsapp_stickers()