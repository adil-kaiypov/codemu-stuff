import os

# specify the directory in which to create the folders
directory = ".\Объекты"

# create folders with names based on numbers 38-55
for i in range(48, 56):
    folder_name = str(i)
    folder_path = os.path.join(directory, folder_name)
    os.makedirs(folder_path)
