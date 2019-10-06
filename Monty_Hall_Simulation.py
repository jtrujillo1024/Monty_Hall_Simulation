import random

def choose():
    return random.randint(1, 3)
    
def stay_game():
    win_door = choose()
    chosen_door = choose()
    wrong_door = choose()
    while wrong_door == win_door or wrong_door == chosen_door:
        wrong_door = choose()
    if win_door == chosen_door:
        return True

def change_game():
    win_door = choose()
    chosen_door = choose()
    wrong_door = choose()
    while wrong_door == win_door or wrong_door == chosen_door:
        wrong_door = choose()
    chosen_door = 6 - chosen_door - wrong_door #1+2+3=6, subtracting chosen_door and wrong_door from 6 equals the remaining door's value
    if win_door == chosen_door:
        return True

def main():
    stay_win_count = 0
    for x in range(100000):
        if stay_game():
            stay_win_count = stay_win_count + 1
    print("Stay Win Rate: {} percent".format(stay_win_count / 100000))

    change_win_count = 0
    for x in range(100000):
        if change_game():
            change_win_count = change_win_count + 1
    print("Change Win Rate: {} percent".format(change_win_count / 100000))




if __name__ == '__main__':
    main()