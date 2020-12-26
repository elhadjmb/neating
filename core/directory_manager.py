"""
Creates directories, opens files...etc
"""

from os import mkdir, path, remove
from shutil import copy2, move
from utils.constants import *
from utils.checker import Checker


def create_folder(folder_name="folder", directory=DEFAULT_PATH):
    """Actions: make directory"""
    folder = path.join(directory, folder_name)
    mkdir(folder) if not(Checker.folder(folder)) else None


def copy_file(file="", source="", destination=""):
    """Actions: copy file"""
    copy2(path.join(source, file), destination)


def delete_file(file="", source=""):
    '''Action: delete file (usually after copy)'''
    remove(path.join(source, file))


def move_file(file="", source="", destination=""):
    """action: move (copy-paste) file"""
    move(path.join(source,file), destination)