import os

# Get the list of all files and directories
# '.' refers to the current directory
entries = os.listdir('/snap/libreoffice/365')

print("Contents of the current directory:")
for entry in entries:
    print(entry)