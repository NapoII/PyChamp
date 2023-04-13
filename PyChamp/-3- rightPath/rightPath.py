import os

path1 = "/home/user/"
path2 = "project/"
path3 = "PyChamp/"
file_name = "Sub.txt"

result_path = os.path.join(path1, path2, path3, file_name)

print(result_path)


# Example file path with mixed slashes

file_path = "C:/Users\\username/Documents\\example.txt"

# Normalize the file path

file_path = os.path.normpath(file_path)

print(file_path)

# Use os.sep to add ad a "/" or "\"

file_path = "C:/Users/username " + os.sep + " Documents"
