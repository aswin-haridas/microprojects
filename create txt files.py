import os

# Create a directory for the text files
if not os.path.exists("D:\Documents\Journal"):
    os.mkdir("D:\Documents\Journal")

# Create the text files
for i in range(1, 30):
    filename = "feb " + str(i) + " 2023"
    with open(os.path.join("D:\Documents\Journal", filename + ".txt"), "w") as f:
        pass
