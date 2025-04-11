

def game():
    print('Playing game')
    score = 100
    f = open('hi-score.txt')
    r = int(f.read())
    print(r)
    f.close()
    if score>r:
        f = open('hi-score.txt',"+w")
        highscore = str(score)
        f.write(highscore)
    elif r>score:
        print('Highscore does not need to be updated')
        f = open('hi-score.txt','r')
        r = highscore
    print(highscore)

game()