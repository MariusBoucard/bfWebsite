import os
from PIL import Image

def compress_images(folder_path, output_folder, quality=85):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Iterate over all files and subdirectories in the given folder
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # Check if the file is an image (you can add more extensions if needed)
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                # Create the output directory structure to mirror the input folder
                relative_path = os.path.relpath(root, folder_path)
                output_dir = os.path.join(output_folder, relative_path)
                os.makedirs(output_dir, exist_ok=True)

                # Compress the image
                input_path = os.path.join(root, file)
                output_path = os.path.join(output_dir, file)
                compress_image(input_path, output_path, quality)

def compress_image(input_path, output_path, quality):
    with Image.open(input_path) as image:
        # Resize the image while preserving the aspect ratio
        image.thumbnail(calculate_new_size(image.size), Image.ANTIALIAS)
        # Save the compressed image with the specified quality
        image.save(output_path, optimize=True, quality=quality)

def calculate_new_size(size, max_width=1200, max_height=1200):
    width, height = size
    ratio = min(max_width / width, max_height / height)
    return int(width * ratio), int(height * ratio)

# Example usage
folder_path = './static'
output_folder = './static'
compress_images(folder_path, output_folder)