from PIL import Image
import os

folder_path = r"T:\\ML\\film"

# Iterate over all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.png'):
        continue  # Skip if the file is already in PNG format
    
    # Load the image
    image_path = os.path.join(folder_path, filename)
    image = Image.open(image_path)
    
    # Convert the image to PNG format
    new_filename = os.path.splitext(filename)[0] + '.png'
    new_image_path = os.path.join(folder_path, new_filename)
    image.save(new_image_path, 'PNG')
    
    # Remove the original image
    os.remove(image_path)
