#! python3
# selectiveCopy.py - Walks through a folder tree and searches for files with a certain file extension, and copies these files from their location to a new folder

from pathlib import Path
import os, shutil

def filesToDelete(path, fileSize):

    path = os.path.abspath(path)
    for foldername, subfolders, filenames in os.walk(path):
        for filename in filenames:
            if os.path.getsize(f'{foldername}/{filename}') > fileSize:
                print(f'To Delete - File exceeds {int(fileSize / 1000)}KB - Path: {foldername}/{filename}')


filesToDelete(Path.home() / 'Documents/Projects/Project_Tutorials/Learn_to_Program_with_Assembly', 1000)