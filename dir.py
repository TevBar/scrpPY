

import os


def list_files_and_subdirectories(directory):
    try:
        with os.scandir(directory) as entries:
            for entry in entries:
                if entry.is_dir():
                    print(f"Directory: {entry.name}")
                elif entry.is_file():
                    print(f"file: {entry.name}")
    except FileNotFoundError: 
        print(f"Error: the Directory '{directory}' does not exist.")
    except PermissionError:
        print(f"Error: You do not have permission to access the directory '{directory}' .")
    except Exception as e: 
        print(f"An unexpected error occurred: {e}")

directory_path = input("Enter the directory path to list its contents: ")

list_files_and_subdirectories(directory_path)


