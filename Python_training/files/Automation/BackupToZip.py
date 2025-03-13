import zipfile, os
def backupToZip(folder):
    folder = os.path.abspath(folder)
    print(folder)
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        print(f'zipFilename: {zipFilename}')
        if not os.path.exists(zipFilename):
            break
        number = number + 1

    print('Creating of file %s...' % (zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files from directory %s...' %(foldername))
        backupZip.write(foldername)
        print(f'subfolder {subfolders}')
        for filename in filenames:
            print('Filename', filename)
            print('\n')
            newBase = os.path.basename(folder) + '_'
            print('Basename', newBase)
            print('\n')
            if filename.startswith(newBase) and filename.endswith('.zip'):
                print('Existing basename', filename)
                continue

            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print("Done")



backupToZip('C:\Python 2.0/filemanipulating')
