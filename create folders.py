import os

path = "D:\\Documents\\College\\S3\\SS\\"

for i in range(1, 6):
    folder_name = "Module " + str(i)
    os.mkdir(path + folder_name)
    print("Folder " + folder_name + " created.")