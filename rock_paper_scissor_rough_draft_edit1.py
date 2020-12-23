from cpu_random_choice import cpu_options

import random



user_starting_score = 0
cpu_starting_score = 0
round_counter = 1


done = False

user_name = input('Let\'s play rock, paper, scissor! What\'s you\'re name?'
                  '\nEnter name HERE:          ')



hello_to_user= print('\nHello, ' + user_name + '!')


def user_choice(choice):
    r_ = 'rock'
    p_ = 'paper'
    s_ = 'scissors'
    return_user_selection = ''
    choice_of_user = choice
    if choice_of_user == 'r':
        print('You have chosen: ' + r_)
        return return_user_selection + choice_of_user
    elif choice_of_user == 'p':
        print('You have chosen: ' + p_)
        return  return_user_selection + choice_of_user
    elif choice_of_user == 's':
        print('You have chosen: ' + s_)
        return return_user_selection + choice_of_user
    else:
        print("\nERROR! Invalid input. Please try again.")
        user_choice(input('\nRock, paper, or scissor?'
                          '\n(TYPE either \'r\' for rock, \'p\' for paper, or \'s\' for scissors)'
                          '\n'
                          '\n'
                          'Enter HERE: ').lower())

user_choice(input('\nRock, paper, or scissor?'
                    '\n(TYPE either \'r\' for rock, \'p\' for paper, or \'s\' for scissors)'
                    '\n'
                    '\n'
                    'Enter HERE: ').lower())






done = False


while not done:

    if user_starting_score != 3 and cpu_starting_score != 3:
        print('\nROUND ' + str(round_counter) + '')
    else:
        break

    if user_starting_score == 3:
        break

    if cpu_starting_score == 3:
        break

    if cpu_starting_score == 2 and user_starting_score == 2:
        input('SUDDEN DEATH! (Press ENTER to continue.)')
    if cpu_starting_score == 2 or user_starting_score == 2 and not (cpu_starting_score == 2 and user_starting_score == 2):
        input('ONE POINT TO GAME! (Press ENTER to continue.)')

    cpu_choice = random.choice(cpu_options)
    user_choice = input('\nRock, paper, or scissor?'
                    '\n(TYPE either \'r\' for rock, \'p\' for paper, or \'s\' for scissors)'
                    '\n'
                    '\n'
                    'You have chosen: ').lower()

    if user_choice == 'r':
        if cpu_choice == 'scissor':
            cpu_has_chosen = str(cpu_choice)
            cpu_choice_display = ('Your opponent has chosen: ' + str(cpu_choice) + '.')
            print(cpu_choice_display)
            print('You WON the round!')
            user_starting_score += 1
        elif cpu_choice == 'paper':
            cpu_choice = str(cpu_choice)
            cpu_choice_display = ('Your opponent has chosen: ' + str(cpu_choice) + '.')
            print(cpu_choice_display)
            print('You LOST the round!')
            cpu_starting_score += 1
        elif cpu_choice == 'rock':
            cpu_choice = str(cpu_choice)
            cpu_choice_display = ('Your opponent has chosen: ' + str(cpu_choice) + '.')
            print(cpu_choice_display)
            print('The round has ended in a STALEMATE.')
    if user_choice == 'p':
        if cpu_choice == 'scissor':
            cpu_has_chosen = str(cpu_choice)
            cpu_choice_display = ('Your opponent has chosen: ' + str(cpu_choice) + '.')
            print(cpu_choice_display)
            print('You LOST the round!')
            cpu_starting_score += 1
        elif cpu_choice == 'paper':
            cpu_choice = str(cpu_choice)
            cpu_choice_display = ('Your opponent has chosen: ' + str(cpu_choice) + '.')
            print(cpu_choice_display)
            print('The round has ended in a STALEMATE.')
        elif cpu_choice == 'rock':
            cpu_choice = str(cpu_choice)
            cpu_choice_display = ('Your opponent has chosen: ' + str(cpu_choice) + '.')
            print(cpu_choice_display)
            print('You WON the round!')
            user_starting_score += 1

    if user_choice == 's':
        if cpu_choice == 'scissor':
            cpu_has_chosen = str(cpu_choice)
            cpu_choice_display = ('Your opponent has chosen: ' + str(cpu_choice) + '.')
            print(cpu_choice_display)
            print('The round has ended in a STALEMATE.')
        elif cpu_choice == 'paper':
            cpu_choice = str(cpu_choice)
            cpu_choice_display = ('Your opponent has chosen: ' + str(cpu_choice) + '.')
            print(cpu_choice_display)
            print('You WON the round!')
            user_starting_score += 1
        elif cpu_choice == 'rock':
            cpu_choice = str(cpu_choice)
            cpu_choice_display = ('Your opponent has chosen: ' + str(cpu_choice) + '.')
            print(cpu_choice_display)
            print('You LOST the round!')
            cpu_starting_score += 1


    input('\n\nScore:'
          '\n'+ user_name + ':' + ' ' + str(user_starting_score) + ''
          '\nOppenent: ' + str(cpu_starting_score) + ''
          '\n'
          '\n(Press ENTER to continue.)')

    round_counter += 1


if user_starting_score == 3:
    print('\nCONGRATULATIONS! You WIN! Let\'s play again!')
elif cpu_starting_score == 3:
    print('\nYour opponent is the winner! You LOSE! Let\'s play again!')






