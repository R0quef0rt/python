import re

def dateDetection(date):
    dateRegex = re.compile(r'([0-3][0-9])\/([0-1][0-2])\/([1-2][0-9]{3})')
    mo = dateRegex.search(date)
    day, month, year = mo.groups()
dateDetection('01/11/1988')