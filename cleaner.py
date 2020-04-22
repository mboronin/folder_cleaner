#!/usr/bin/env python3

import os
import subprocess
import sys

#TODO Add quiet mode
#TODO Add logging
#TODO Add filetypes not extensions only
#TODO Allow several folders
#TODO Add tests


'''
gets an absolute path to a folder
'''
def main(path):
    try:
        folder = find_folder(path)
    except FileNotFoundError:
        print("Could not locate your folder\nTerminating!")
        return
    cleaner = MyCleaner(folder)
    cleaner.clean()
    print("Cleaning is now complete")


def check_if_folder_exists(folder: str):
    if os.path.exists(folder) and os.path.isdir(folder):
        return True
    return False


def find_folder(path: str):
    if os.path.isabs(path):
        if check_if_folder_exists(path):
            return path
        else:
            raise FileNotFoundError
    elif check_if_folder_exists(os.path.abspath(path)):
        path = os.path.abspath(path)
        print("Did you mean " + path + " [y/n]?")
        answer = input()
        if answer == "y":
            return path
        else:
            raise FileNotFoundError
    else:
        homedir = os.path.expanduser("~")
        path = homedir + '/' + path
        if(check_if_folder_exists(path)):
            print("Did you mean " + path + " [y/n]?")
            answer = input()
            if answer == "y":
                return path
            else:
                raise FileNotFoundError



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
                ext_folder = self.folder + '/' + extension
                if extension_counter[extension] < 5 and not check_if_folder_exists(ext_folder):
                    continue
                if check_if_folder_exists(ext_folder):
                    move_file_to_folder(filepath, ext_folder)
                else:
                    create_folder(self.folder, extension)
                    move_file_to_folder(filepath, ext_folder)


if len(sys.argv) < 2:
    print("Path not provided")
else:
    main(sys.argv[1])
