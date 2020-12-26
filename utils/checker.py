from os import path


class Checker:
    @staticmethod
    def folder(directory):
        return path.isdir(directory)
