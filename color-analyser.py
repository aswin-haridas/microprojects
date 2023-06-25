import cv2
import numpy as np
import pandas as pd
import os

def calculate_color_change(original_image, edited_image, hue_value):
    # Convert images to the HSV color space
    original_hsv = cv2.cvtColor(original_image, cv2.COLOR_BGR2HSV)
    edited_hsv = cv2.cvtColor(edited_image, cv2.COLOR_BGR2HSV)
    
    # Define the range of hue values to consider for the given color
    lower_hue = hue_value - 15
    upper_hue = hue_value + 15
    
    # Create a mask to extract pixels within the specified hue range
    mask_original = cv2.inRange(original_hsv, np.array([lower_hue, 50, 50]), np.array([upper_hue, 255, 255]))
    mask_edited = cv2.inRange(edited_hsv, np.array([lower_hue, 50, 50]), np.array([upper_hue, 255, 255]))
    
    # Count the number of pixels in each mask
    original_pixel_count = cv2.countNonZero(mask_original)
    edited_pixel_count = cv2.countNonZero(mask_edited)
    
    # Check if the original pixel count is zero
    if original_pixel_count == 0:
        return 0
    
    # Calculate the color change percentage
    color_change_percentage = ((edited_pixel_count - original_pixel_count) / original_pixel_count) * 100
    
    # Constrain the color change within the range of -100 to 100
    color_change_percentage = np.clip(color_change_percentage, -100, 100)
    
    return color_change_percentage


# Load the original image
original_image = cv2.imread('og.png')

# Define the hue values for the colors
colors = {'red': 0, 'orange': 30, 'yellow': 60, 'green': 120, 'blue': 180, 'violet': 240, 'magenta': 300}

# Create a DataFrame to store the color change data
data = {'File Name': [], 'Red Change': [], 'Orange Change': [], 'Yellow Change': [],
        'Green Change': [], 'Blue Change': [], 'Violet Change': [], 'Magenta Change': []}

# Path to the preset folder
preset_folder = 'T:\ML\presets'

# Iterate through each file in the preset folder
for file_name in os.listdir(preset_folder):
    # Construct the file path
    file_path = os.path.join(preset_folder, file_name)
    
    # Skip directories
    if not os.path.isfile(file_path):
        continue
    
    # Load the edited image
    edited_image = cv2.imread(file_path)
    
    # Calculate color change for each color
    color_changes = {}
    for color, hue_value in colors.items():
        percentage_change = calculate_color_change(original_image, edited_image, hue_value)
        color_changes[color] = percentage_change
    
    # Append the data to the DataFrame
    data['File Name'].append(file_name)
    data['Red Change'].append(color_changes['red'])
    data['Orange Change'].append(color_changes['orange'])
    data['Yellow Change'].append(color_changes['yellow'])
    data['Green Change'].append(color_changes['green'])
    data['Blue Change'].append(color_changes['blue'])
    data['Violet Change'].append(color_changes['violet'])
    data['Magenta Change'].append(color_changes['magenta'])

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Create the Excel file if it doesn't exist
excel_file = 'color_changes.xlsx'
if not os.path.isfile(excel_file):
    df.to_excel(excel_file, index=False)
else:
    # Append the data to the existing Excel file
    with pd.ExcelWriter(excel_file, engine='openpyxl', mode='a') as writer:
        df.to_excel(writer, index=False, header=not writer.sheets['Sheet1'])

print(f"Color changes appended to the file: {excel_file}")
