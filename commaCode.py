spam = ['apples', 'bananas', 'tofu', 'cats']

def output(list):
    count = 0
    joined = ''
    while count < len(list) - 2:
        joined += list[count] + ', '
        count += 1
    joined += list[-2] + ' and '
    joined += list[-1] + '.'

print(output(spam))