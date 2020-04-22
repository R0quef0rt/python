import os, shutil
from pathlib import Path

src = Path.cwd() / Path('copyFiles')
dest = Path.cwd() / Path('newFiles')

for folderName, subFolders, fileNames in os.walk(Path(src)):
    print('The current folder is ' + folderName)

    for file in fileNames:
        shutil.copy(Path(folderName) / file, dest)
