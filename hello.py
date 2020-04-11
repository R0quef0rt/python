# This program says hello and asks for my name.

print('What is your name?')
myName = input()
print('What is your age?')
myAge = int(input())
if myName == 'Ryan' and myAge == 31:
    print('Success!')
else:
    print('Failure!')

i = 0
while myName == 'Ryan' and i < 5:
    print('Hooray!')
    i = i + 1

for n in range(len(myName)):
    print(str(n) + ' Boops!')