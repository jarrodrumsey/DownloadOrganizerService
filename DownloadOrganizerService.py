import os
import shutil

def get_ext_name(ext):
    """
    Convert file extension to a directory name format.

    Parameters:
    ext (str): The file extension.

    Returns:
    str: The formatted directory name.
    """
    return ext.replace(".", "").upper()

def sort(root, file_entry):
    """
    Sort files in the given directory into subdirectories based on file extensions.

    Parameters:
    directory (Path): The path to the directory with files to sort.
    """
    if file_entry.is_file():
        
        name, ext   = os.path.splitext(file_entry.name)
        sorted_dir  = os.path.join(root, get_ext_name(ext))

        if not os.path.exists(sorted_dir):
            os.mkdir(sorted_dir)
        
        old_path = file_entry.path
        new_path = os.path.join(sorted_dir, file_entry.name)
       
        new_file_name = ""
        copy_number = 1
        
        while os.path.exists(new_path):   
            new_file_name = f"{name} ({copy_number}){ext}"
            new_path = os.path.join(sorted_dir, new_file_name)
            copy_number += 1
        
        try:
            shutil.move(old_path, new_path)    
        except Exception as e:
                  print(f"Could not move file {old_path} to {new_path}")
            
## Path to downloads folder
folder_path = 'C:\\Users\\Workplace\\Downloads';

for entry in os.scandir(folder_path):
    if entry.is_file():
        sort(folder_path, entry)





