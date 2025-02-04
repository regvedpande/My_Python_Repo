import os

# Create a directory
if not os.path.exists("mydir"):
    os.makedirs("mydir")

# Create a file
with open("mydir/myfile.txt", "w") as f:
    f.write("Hello, world!")

# Read a file
with open("mydir/myfile.txt", "r") as f:
    content = f.read()
    print(content)

# List files in a directory
files = os.listdir("mydir")
print(files)

# Rename a file
os.rename("mydir/myfile.txt", "mydir/newfile.txt")

# Delete a file
os.remove("mydir/newfile.txt")

# Delete a directory
os.rmdir("mydir")
