import random

def coinFlip(answerNumber):
    if answerNumber == 1:
        return 'H'
    elif answerNumber == 2:
        return 'T'

coinResults = []

def coinTest(totalFlips):
    while totalFlips > 0:
        global coinResults
        coinResult = coinFlip(random.randint(1,2))
        coinResults.append(coinResult)
        totalFlips -= 1

coinTest(10000)

def coinStreak(list):
    streakStart, streakEnd = 0,0
    firstItem = 0

    for item in range(1, len(list)):
        if list[item] != coinResults[item - 1] + 1:
            streakStart = firstItem
        if (item - firstItem) > (streakEnd - streakStart):
            streakStart, streakEnd = firstItem, item

    return streakEnd - streakStart, list[streakStart], list[streakEnd]

print(coinResults)
coinStreak(coinResults)
