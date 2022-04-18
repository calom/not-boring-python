# paper, rock, scissors
from random import choice
import sys

stats = {'tie': 0, 'loss': 0, 'win': 0, 'total': 0}
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

    print(result + '\n')
    return score


def showScore(score):
    print(f"""Your score after game no.{score['total']}: 
        loss: {score['loss']} 
        win: {score['win']}
        tie: {score['tie']} \n""")


if __name__ == '__main__':
    print("Welcome to (R)ock, (P)aper, (S)cissors. You will try your luck against powerful AI. Let's play!")
    while True:
        human_choice = input('To play press R for rock, P for paper, S for scissors or F to finish the '
                             'game. \n')
        if human_choice == 'F':
            if stats['total'] == 0:
                print('''So you don't want to play at all, huh?''')
            else:
                print('End of the game. This is how you played:')
                showScore(stats)
            sys.exit()

        ai_choice = choice(list(choices.keys()))
        print("AI shows " + ai_choice)

        if human_choice not in choices:
            print('''Seems you pressed wrong key. Let's try again.\n''')
            continue
        elif human_choice == ai_choice:
            print('Tie.\n')
            stats['tie'] += 1
            stats['total'] += 1
            showScore(stats)
            continue
        else:
            stats = whoWon(ai_choice, human_choice, stats)
            showScore(stats)
            continue
