import os

def delete_files(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            print(f"Do you want to delete '{file_path}'? (y/n)")
            answer = input().lower()
            if answer == "y":
                os.remove(file_path)
                print(f"Deleted '{file_path}'")
            else:
                print(f"Skipped '{file_path}'")

if __name__ == "__main__":
    print("Enter the directory path to scan:")
    path = input()
    delete_files(path)
