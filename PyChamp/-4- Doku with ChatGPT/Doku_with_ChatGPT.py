import os

"""
Write me a .py docstr ("""""") with the content:
Args, Returns and Example Usage.
For Args and Returns create a list with "- "-
and for Example Usage create a list with ">>> ".
Only write the docstr in """""" in copycode mode. Here is the code:
"""


def Folder_gen(Folder_Name, Folder_dir ):
    """
Create a new folder with the specified name in the specified directory.

Args:
- Folder_Name (str): The name of the folder to be created.
- Folder_dir (str): The directory in which the new folder should be created.

Returns:
- full_path (str): The full path to the newly created folder.

Example Usage:
>>> Folder_gen("test_folder", "Documents")
'/Users/username/Documents/test_folder'
"""

    folder = Folder_Name
    dir = f"~{os.sep}{Folder_dir}{os.sep}{folder}"
    full_path = os.path.expanduser(dir)
    if os.path.exists(full_path):
        pass
    else:
        os.makedirs(full_path)
    return(full_path)


Folder_gen("PyChamp", "Documents" )