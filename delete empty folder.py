import os
import shutil
from tqdm import tqdm

def remove_empty_folders(root_dir):
    num_dirs = sum([len(dirs) for _, dirs, _ in os.walk(root_dir)])
    with tqdm(total=num_dirs, desc="Removing empty folders") as pbar:
        for root, dirs, files in os.walk(root_dir, topdown=False):
            for dir in dirs:
                dir_path = os.path.join(root, dir)
                if not os.listdir(dir_path):
                    pbar.write(f"Removing empty folder: {dir_path}")
                    shutil.rmtree(dir_path)
                pbar.update(1)


root_dir = r"C:\\Users\\Aswin"
remove_empty_folders(root_dir)
