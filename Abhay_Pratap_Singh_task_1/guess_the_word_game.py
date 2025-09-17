import random as r
words = ["python", "machine", "learning", "data", "science"]
comp = r.choices(words)
length = len(comp[0])

chances = 6
progress = []
for word in comp:
    for i in word:
        progress.append(i)

def trackProgress(letter, chances):
    flag = 0
    for i in range(0, length):
        if letter in progress:
            flag = 1
            progress.remove(letter)
            return -1
    if progress == []:
        print('Guess Correctly. You Won. Word was',comp[0])
        return True
    print()
            
def showProgress(progress):
    for char in comp[0]:
        if char in progress:
            print('_', end="")
        else:
            print(char, end="")
    print()



while chances > 0:
    num = len(progress)
    letter = str(input('Guess a character: '))
    isWon = trackProgress(letter, chances)
    if isWon == True:
        break
    elif isWon == -1:
        print('Correct Guess. Chances left: ',chances)
    else:
        print('Wrong Guess. Chances left: ',chances)
        chances -= 1
    showProgress(progress)
    print()



