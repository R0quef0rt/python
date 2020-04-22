import os, shutil, re
from pathlib import Path

src = Path('./copyFiles')

for folderName, subFolders, fileNames in os.walk(Path(src)):
    
    count = 0

    for file in fileNames:
        fileRegex = re.compile(r'(test)(\d+)')
        mo = fileRegex.search(file)
        
        if mo.group(2) == count:
            break
        else:
            fileRename = 'test' + str(count) + '.pdf'
            shutil.move(Path(src) / file, Path(src) / fileRename)
        
        count +=1