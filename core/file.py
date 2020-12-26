from os import path
from os import listdir
from os.path import isfile, join


class File:
    '''
    File defining class
    '''

    def __init__(self, **kwargs):
        self.file_path = kwargs["file_path"]
        self.file = self.file()
        self.file_full_name = self.full_name()
        self.file_name = self.name()
        self.file_extension = self.extension()

    def file(self):
        return open(self.file_path, "r")

    def name(self):
        return path.splitext(self.file_full_name)[0]

    def extension(self):
        return path.splitext(self.file_full_name)[1]

    def full_name(self):
        return path.basename(self.file_path)

    @staticmethod
    def find_files(directory):
        return [file for file in listdir(directory) if isfile(join(directory, file))]

    @staticmethod
    def list_of_files(directory):
        return [File(file_path=path.join(directory, file)) for file in [file for file in listdir(directory) if isfile(join(directory, file))]]
