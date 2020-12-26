"""
input: directory
works

"""

from core.file import File
from core.classifier import Classifier
from core.directory_manager import *
from os import path


def get_files(directory):
    return File.list_of_files(directory)


def class_files(list_of_files):
    return [Classifier.file_class(file) for file in list_of_files]


def create_all_folders(directory):
    for x in Classifier.file_types:
        create_folder(x, directory)


def transfer_files(directory, list_of_files):
    for file in class_files(list_of_files):
        destination = path.join(directory, file[1])
        if not (Checker.folder(destination)): create_folder(file[1], directory)
        try:
            move_file(file=file[0].file_path, source=directory, destination=destination)
        except FileExistsError:
            delete_file(file=file[0].file_path, source=directory)
            move_file(file=file[0].file_path, source=directory, destination=destination)
