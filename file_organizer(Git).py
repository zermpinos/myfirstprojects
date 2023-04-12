"""
sort_files.py

This program organizes files in a specified directory by separating them into different folders
based on their file type.

Requirements:
    - Python 3.x
    - os module
    - shutil module

Parameters:
    - source: The directory containing the files to be organized.
        The default value is the current working directory.
    - destination: The directory where the organized files will be stored.
        The default value is a subdirectory named 'organized' inside the current working directory.
    - file_types: A dictionary containing the file extensions and their corresponding folder names.

Functions:
    - sort_files(directory):
        This function takes a directory as input and organizes its files by moving them into the appropriate folders
        based on their file type.


Author:
    Panagiotis Zermpinos

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
    '.pdf': 'Documents',
    '.doc': 'Documents',
    '.docx': 'Documents',
    '.txt': 'Documents',
    '.xlsx': 'Spreadsheets',
    '.zip': 'Zipped files',
    '.rar': 'Zipped files',
    '.7z': 'Zipped files',
    }


def sort_files(directory):
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(file)[1]
            if file_extension in file_types:
                folder_name = file_types[file_extension]
                folder_path = os.path.join(destination, folder_name)
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)
                shutil.copy(file_path, os.path.join(folder_path, file))
        elif os.path.isdir(file_path):
            sort_files(file_path)


sort_files(source)
