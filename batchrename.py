import os
import shutil
from PIL import Image
import imagehash

first_folder = 'T:\\ML\\digital'
second_folder = 'T:\\ML\\film'

# Get the list of image files in the first folder
first_images = [f for f in os.listdir(first_folder) if os.path.isfile(os.path.join(first_folder, f))]

# Iterate over the image files in the first folder
for image in first_images:
    image_path = os.path.join(first_folder, image)

    # Calculate the perceptual hash of the image
    hash1 = imagehash.average_hash(Image.open(image_path))

    # Search for similar images in the second folder
    for file in os.listdir(second_folder):
        file_path = os.path.join(second_folder, file)

        # Calculate the perceptual hash of the current image in the second folder
        hash2 = imagehash.average_hash(Image.open(file_path))

        # Compare the hashes to determine similarity
        if hash1 == hash2:
            new_path = os.path.join(second_folder, image)
            shutil.move(file_path, new_path)
            print(f"Renamed {file_path} to {new_path}")
            break  # Move to the next image in the first folder

