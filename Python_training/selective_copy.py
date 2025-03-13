import os, shutil


def copy_files(folder, extension, dest):
    for foldername, subfolders, filenames in os.walk(folder):
        print('Searching in %s' %(foldername))
        for filename in filenames:
            if filename.endswith(extension) and foldername !=dest:
                shutil.copy(filename, dest)


copy_files("C:\Python\Book1", ".txt", "C:\Python\Book1\extension")