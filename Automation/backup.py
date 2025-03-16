import os
import shutil
import datetime
import schedule
import time

source_dir = "C:/Python 2.0/filemanipulating"
destination_dir = "C:/Arduino"


def copy_folder_to_directory(source,dest):
    today = datetime.date.today()
    dest_dir = os.path.join(dest, str(today))
    print(dest_dir)

    try:
        shutil.copytree(source, dest_dir)
        print(f"Folder copied to: {dest_dir}")
    except FileExistsError:
        print(f"Folder already exists in: {dest}")


copy_folder_to_directory(source_dir, destination_dir)

# schedule.every().day.at("18:57").do(lambda: copy_folder_to_directory(source_dir, destination_dir))


while True:
    schedule.run_pending()
    time.sleep(60)

