"""
sort_files.py

This program organizes files in a specified directory by separating them into different folders
based on their file type.

Usage:
    python sort_files.py

Requirements:
    - Python 3.x
    - os module
    - shutil module

Parameters:
    - source_dir: The directory containing the files to be organized.
        The default value is the current working directory.
    - destination_dir: The directory where the organized files will be stored.
        The default value is a subdirectory named 'organized' inside the current working directory.
    - file_types: A dictionary containing the file extensions and their corresponding folder names.

Functions:
    - sort_files(directory):
        This function takes a directory as input and organizes its files by moving them into the appropriate folders
        based on their file type.

Returns:
    None

Example:
    To organize files in the current working directory, simply run the program in the command line:
    $ python sort_files.py

Author:
    Panagiotios Zermpinios

Version:
    1.0 (April 2023)
"""

import os
import shutil
# Set the source directory to the current working directory but remember to use / instead of \
source = os.getcwd()

# Set the destination directory to a subfolder named 'organized' inside the current working directory
destination = os.getcwd() + '/organized'

# Define a dictionary that connects file extensions to folder names
file_types = {
    '.jpeg': 'Images',
    '.jpg': 'Images',
    '.JPG': 'Images',
    '.png': 'Images',
    '.gif': 'Images',
    '.mp3': 'Audio',
    '.wav': 'Audio',
    '.flac': 'Audio',
    '.mp4': 'Videos',
    '.avi': 'Videos',
    '.3gp': 'Videos',
    '.wmv': 'Videos',
    '.mov': 'Videos',
    '.pdf': 'Documents',
    '.doc': 'Documents',
    '.docx': 'Documents',
    '.txt': 'Documents',
    '.xlsx': 'Spreadsheets',
    '.zip': 'Zipped files',
    '.rar': 'Zipped files',
    '.7z': 'Zipped files',
    }


def sort_files(directory):  # Sorts files into different folders based on their file type.
    # Loop through each file in the directory
    for file in os.listdir(directory):
        # Get the file path
        file_path = os.path.join(directory, file)
        # Check if the file is a regular file (i.e., not a directory)
        if os.path.isfile(file_path):
            # Get the file extension
            file_extension = os.path.splitext(file)[1]
            # Check if the file extension is in the file_types dictionary
            if file_extension in file_types:
                # Get the folder name for the file extension
                folder_name = file_types[file_extension]
                # Create the folder if it does not exist
                folder_path = os.path.join(destination_dir, folder_name)
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)
                # Copy the file to the appropriate folder
                shutil.copy(file_path, os.path.join(folder_path, file))
        # Check if the file is a directory
        elif os.path.isdir(file_path):
            # Recursively call the sort_files function to organize the files in the subdirectory
            sort_files(file_path)


# Call the sort_files function to organize the files in the source directory
sort_files(source_dir)
