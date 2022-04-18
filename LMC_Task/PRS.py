# paper, rock, scissors
from random import choice
import sys

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


if __name__ == '__main__':
    print("Welcome to (R)ock, (P)aper, (S)cissors. You will try your luck against powerful AI. Let's play!")
    while True:
        human_choice = input('To play you should press R for rock, P for paper, S for scissors or F to finish the '
                             'game. \n')

        if human_choice == 'F':
            if score['total'] != 0:
                print('End of the game. This is how you played:')
                showScore(score)
            else:
                print('''So you don't want to play at all, huh?''')
            sys.exit()

        ai_choice = choice(list(choices.keys()))
        print("AI shows " + ai_choice)

        if human_choice not in choices:
            print('''Seems you pressed wrong key. Let's try again.''')
            continue
        elif human_choice == ai_choice:
            print('Tie.')
            score['tie'] += 1
            score['total'] += 1
            showScore(score)
            continue
        else:
            score = whoWon(ai_choice, human_choice, score)
            showScore(score)
            continue
