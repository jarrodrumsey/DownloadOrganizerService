import argparse
from ast import parse
from re import M
import shutil

from pathlib import Path
from xmlrpc.client import Boolean

def get_ext_name(ext):
    """
    Convert file extension to a directory name format.

    Parameters:
    ext (str): The file extension.

    Returns:
    str: The formatted directory name.
    """
    return ext.replace(".", "").upper()

def sort_file(root : Path, file_path : Path):
    """
    Sort a file into a subdirectory based on its file extension.
    
    Parameters:
    root (Path): Path to the directory of sorted file subdirectories
    file_path (Path): Path to the file to be sorted into a subdirectory
    """
    if file_path.is_file() and not file_path.name.startswith('.'):
        
        ext = file_path.suffix
        sorted_dir  = root / get_ext_name(ext)

        # Create folder at the given path
        sorted_dir.mkdir(exist_ok=True)
        
        # Ideal location of file after sort
        new_path = sorted_dir / file_path.name
        
        new_file_name = ""
        copy_number = 1
        
        # Rename file if file w/ same name already exists in sorted location
        while new_path.exists():   
            new_file_name = f"{file_path.stem} ({copy_number}){ext}"
            new_path = sorted_dir/new_file_name
            copy_number += 1
        
        try:
            shutil.move(file_path, new_path)    
        except Exception as e:
                  print(f"Could not move file {file_path} to {new_path}")
                         
def sort_dir(dir_path):
    """
    Sort all files in a given directory into subdirectories corresponding to file extension
        
    Parameters:
    dir_path (Path): The path to the directory with files to sort.
    """
    for entry in dir_path.iterdir():
        sort_file(dir_path, entry) 

def dialog(folder_path): 
    """Prompt the user for confirmation before starting the sort"""
    choice = input(f"Are you sure you would like to sort the following directory?\nDirectory: {folder_path}\n(y/n): ").strip().lower()
    return choice == 'y';
   
# Main Execution
def main(folder_path: Path, no_dialog: bool):
    
    if no_dialog:
        #sort_dir(folder_path)
        print("SORT | ", folder_path)
    else:
        if dialog(folder_path):
            #sort_dir(folder_path)
            print("SORT CONFIRMED | ", folder_path)
        else:
            print("SORT DENIED")    
            

        
if __name__ == "__main__":
    DOWNLOADS_PATH = Path.home() / 'Downloads'
    
    parser = argparse.ArgumentParser(description="Sort all files in a given directory into subdirectories corresponding to file extension.")
    
    parser.add_argument('-p','--path', 
                        type=Path, 
                        help='The path to the directory with files to sort.',
                        default=DOWNLOADS_PATH)
    
    parser.add_argument('-nd','--no_dialog', 
                       action='store_true',
                       help='Presence of flag disables secondary confirmation dialog',
                       default=False)
    
    args = parser.parse_args()
    
    main(args.path, args.no_dialog)





