import zipfile, os

def backup(folder):
    folder = os.path.abspath(folder)
    
    number = 1
    while True:
        zipFile = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFile):
            break
        number +=1
    print('Creating %s...' %(zipFile))
    backup = zipfile.ZipFile(zipFile, 'w')
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s...' % (foldername))
        backup.write(foldername)
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue
            backup.write(os.path.join(foldername, filename))
    backup.close()
    print("Done")
    
    
backup("C:\Python\Book1")