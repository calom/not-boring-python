# paper, rock, scissors
import random, sys
import numpy as np

print("Welcome to (R)ock, (P)aper, (S)cissors. You will try your luck against powerful AI. Let's play!")
clue = "To play you should press R for rock, P for paper, S for scissors or F to finish the game."
score = {'tie': 0, 'loss': 0, 'win': 0, 'total': 0}
rock = 'rock'
paper = 'paper'
scissors = 'scissors'
choices = {'R': rock, 'P': paper, 'S': scissors}


def whoWon(ai, real_player, score):
    result = ''
    # Computer winning combinations
    if choices[real_player] == rock and choices[ai] == paper or choices[real_player] == scissors and choices[
        ai] == rock or choices[real_player] == paper and choices[ai] == scissors:
        result = ai + ' beats ' + real_player + '. You Lost!'
        score['loss'] += 1
    # Human player winning combinations
    else:
        result = real_player + ' beats ' + ai + '. You Win!'
        score['win'] += 1
    score['total'] += 1

    print(result)
    return score


def showScore(score):
    print(f"""Your score after game no.{score['total']}: 
        loss: {score['loss']} 
        win: {score['win']}
        tie: {score['tie']}""")


while True:
    human_choice = input(clue + '\n')

    if human_choice == 'F':
        if score['total'] != 0:
            print('End of the game. This is how you played:')
            showScore(score)
        else:
            print('''So you don't want to play at all, huh?''')
        sys.exit()

    ai_choice = random.choice(list(choices.keys()))
    print("I choose " + ai_choice)

    if human_choice not in choices:
        print('Seems you pressed wrong key.')
        continue
    elif human_choice == ai_choice:
        print('Tie, again?')
        score['tie'] += 1
        score['total'] += 1
        showScore(score)
        continue
    else:
        score = whoWon(ai_choice, human_choice, score)
        showScore(score)
        continue
