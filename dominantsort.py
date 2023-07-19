import colorsys
import os
from PIL import Image
import numpy as np
import shutil
from sklearn.cluster import KMeans
from tqdm import tqdm

def get_dominant_hue(image_path):
    # Open the image and resize it for efficiency
    image = Image.open(image_path)
    image.thumbnail((100, 100))

    # Convert the image to an array of RGB pixels
    rgb_image = image.convert("RGB")
    pixel_array = np.array(rgb_image)

    # Reshape the pixel array to a flat list of pixels
    pixels = pixel_array.reshape(-1, 3)

    # Apply k-means clustering to find dominant colors
    kmeans = KMeans(n_clusters=1)
    kmeans.fit(pixels)

    # Get the centroid of the dominant color cluster
    dominant_color = kmeans.cluster_centers_[0]

    # Convert the RGB color to HSV color space
    dominant_hsv = colorsys.rgb_to_hsv(*dominant_color)

    # Extract the hue value
    dominant_hue = dominant_hsv[0]

    return dominant_hue

def rename_images_with_hue(folder_path):
    # Get a list of all image files in the folder
    image_files = [f for f in os.listdir(folder_path) if f.endswith(('.png', '.jpg', '.jpeg'))]

    for image_file in tqdm(image_files, desc="Renaming images"):
        image_path = os.path.join(folder_path, image_file)

        # Get the dominant hue of the image
        dominant_hue = get_dominant_hue(image_path)

        # Adjust the number of decimal places
        decimal_places = 4
        dominant_hue_formatted = f"{dominant_hue:.{decimal_places}f}"

        # Rename the image file
        new_file_name = f"{dominant_hue_formatted}.jpg"
        new_file_path = os.path.join(folder_path, new_file_name)

        # Check if the new file name already exists
        if os.path.exists(new_file_path):
            # Generate a new file name with a copy suffix
            copy_count = 1
            while True:
                copy_file_name = f"{dominant_hue_formatted}_copy{copy_count}.jpg"
                copy_file_path = os.path.join(folder_path, copy_file_name)
                if not os.path.exists(copy_file_path):
                    new_file_name = copy_file_name
                    new_file_path = copy_file_path
                    break
                copy_count += 1

        # Rename the file
        shutil.move(image_path, new_file_path)


folder_path = "/home/aswin/Pictures/Photos"
rename_images_with_hue(folder_path)
