import os, shutil
from pathlib import Path

src = Path('./')

for folderName, subFolders, fileNames in os.walk(Path(src)):
    print('The current folder is ' + folderName)

    for file in fileNames:
        fileSize = os.path.getsize(Path(folderName) / file)

        if int(fileSize) > 100000000:
            os.unlink(Path(folderName) / file)