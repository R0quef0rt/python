from pathlib import Path
import os, re

def madLibs():
    
    templateFile = open('madLibs.txt', 'r')
    content = templateFile.read()
    templateFile.close()

    regex = re.compile(r'(NOUN|VERB|ADVERB|ADJECTIVE)')
    matches = regex.findall(content)

    for match in matches:
        sub = input('Enter a ' + match + ': ')
        content = content.replace(match, sub, 1)

    outFile = open('madLibsOut.txt', 'w')
    outFile.write(content)
    outFile.close()

madLibs()