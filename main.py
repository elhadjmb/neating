from core import execution
from utils.checker import Checker

if __name__ == '__main__':
    directory = "/home/hadj/test"
    execution.transfer_files(directory, execution.get_files(directory)) if Checker.folder(directory) else None
