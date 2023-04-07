import os

directory = ".\Объекты"

for i in range(56, 72):
    folder_name = str(i)
    folder_path = os.path.join(directory, folder_name)
    os.makedirs(folder_path)
