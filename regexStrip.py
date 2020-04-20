import re

def regexStrip(string, char):
    if char == '':
        stripWhitespace = re.compile(r'(\S.*)')
        mo = stripWhitespace.search(string)
        print(mo.group(1))
    elif char:
        stripWhitespace = re.compile(r'([char].*)')
        mo = stripWhitespace.search(string)
        print(mo.group(1))

regexStrip('   sadfsadfsd   ', 's')