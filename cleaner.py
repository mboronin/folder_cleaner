import os
import subprocess

'''
gets an absolute path to a folder
'''
def main(arg):
    cleaner = MyCleaner(arg)
    cleaner.clean()


def check_if_folder_exists(folder: str):
    if os.path.exists(folder) and os.path.isdir(folder):
        return True
    return False


def move_file_to_folder(filename: str, folder: str):
    subprocess.run(['mv', filename, folder])


def create_folder(place, folder):
    subprocess.run(['mkdir', place + '/' + folder])


class MyCleaner:
    def __init__(self, folder):
        self.folder = folder

    def clean(self):
        extension_counter = {}
        folder_exists = check_if_folder_exists(self.folder)
        if folder_exists:
            for filename in os.listdir(self.folder):
                filepath = self.folder + '/' + filename
                if os.path.isdir(filepath):
                    continue
                name, file_extension = os.path.splitext(filename)
                extension = file_extension[1:].lower()
                extension_counter[extension] = extension_counter.get(extension, 0) + 1

            for filename in os.listdir(self.folder):
                filepath = self.folder + '/' + filename
                if os.path.isdir(filepath):
                    continue
                name, file_extension = os.path.splitext(filename)
                extension = file_extension[1:].lower()
                if extension_counter[extension]< 5:
                    continue
                ext_folder = self.folder + '/' + extension
                if check_if_folder_exists(ext_folder):
                    move_file_to_folder(filepath, ext_folder)
                else:
                    create_folder(self.folder, extension)
                    move_file_to_folder(filepath, ext_folder)

main("/home/mboronin/Downloads/Telegram Desktop")
