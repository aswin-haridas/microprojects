import os

folder_location = "D:\Temp\music from phone"

def capitalize_words(file_name):
    return " ".join([word.capitalize() for word in file_name.split()])

for file_name in os.listdir(folder_location):
    new_file_name = capitalize_words(file_name)
    os.rename(os.path.join(folder_location, file_name), os.path.join(folder_location, new_file_name))
