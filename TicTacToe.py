board = {'1': ' ', '2': ' ', '3': ' ',
         '4': ' ', '5': ' ', '6': ' ',
         '7': ' ', '8': ' ', '9': ' '}


def printBoard(board):
    print(board['1'] + ' | ' + board['2'] + ' | ' + board['3'])
    print('--|---|--')
    print(board['4'] + ' | ' + board['5'] + ' | ' + board['6'])
    print('--|---|--')
    print(board['7'] + ' | ' + board['8'] + ' | ' + board['9'])


def won(board):
    if board['1'] == board['2'] == board['3'] != " ":
        print(f"Player {board['1']} won")
        exit()

    elif board['4'] == board['5'] == board['6'] != " ":
        print(f"Player {board['4']} won")
        exit()

    elif board['7'] == board['8'] == board['9'] != " ":
        print(f"Player {board['7']} won")
        exit()

    elif board['7'] == board['5'] == board['3'] != " ":
        print(f"Player {board['7']} won")
        exit()

    elif board['9'] == board['5'] == board['1'] != " ":
        print(f"Player {board['9']} won")
        exit()

    elif board['1'] == board['4'] == board['7'] != " ":
        print(f"Player {board['1']} won")
        exit()

    elif board['2'] == board['5'] == board['8'] != " ":
        print(f"Player {board['2']} won")
        exit()

    elif board['3'] == board['6'] == board['9'] != " ":
        print(f"Player {board['3']} won")
        exit()

    else:
        return


player_1 = "X"
player_2 = "O"

print(f"player_1 is {player_1}, player_2 is {player_2}")

printBoard(board)


def moves(board):
    turn = 'X'
    counter = 0

    while True:
        # for i in range(1, 10):
        #     print(i)
        print(f' {turn} its your move: ')
        move = input()

        # if turn == 'X' or 'O':

        try:
            if board[move] == ' ':
                board[move] = turn
                counter += 1
                printBoard(board)

                if turn == 'X':
                    turn = 'O'
                else:
                    turn = 'X'

            else:
                print("already taken.\nenter different number?")

            if counter > 4:
                won(board)
            if counter == 9:
                print("Its a tie")
                exit()
        except KeyError:
            print("enter only integers ")

if __name__ == '__main__':
    moves(board)
