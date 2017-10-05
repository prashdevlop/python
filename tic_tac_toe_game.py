theBoard = {'1': ' ', '2': ' ', '3': ' ', '4': ' ', '5': ' ', '6': ' ', '7': ' ', '8': ' ', '9': ' '}
def printBoard(board):
            print(board['1'] + '|' + board['2'] + '|' + board['3'])
            print('-+-+-')
            print(board['4'] + '|' + board['5'] + '|' + board['6'])
            print('-+-+-')
            print(board['7'] + '|' + board['8'] + '|' + board['9'])
print("please enter your player choice:")
print("1. O")
print("2. X")
choice=int(input())
if choice == 1:
    turn = 'O'
if choice == 2:
    turn = 'X'
def decide_winner(turn):
    if theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':
        print("Player " + theBoard['2'] + " Win")
        exit()
    elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':
        print("Player " + theBoard['5'] + " Win")
        exit()
    elif theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':
        print("Player " + theBoard['8'] + " Win")
        exit()
    elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':
        print("Player " + theBoard['5'] + " Win")
        exit()
    elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ':
        print("Player " + theBoard['4'] + " Win")
        exit()
    elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ':
        print("Player " + theBoard['5'] + " Win")
        exit()
    elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ':
        print("Player " + theBoard['6'] + " Win")
        exit()
    elif theBoard['3'] == theBoard['5'] == theBoard['7'] != ' ':
        print("Player " + theBoard['5'] + " Win")
        exit()
for i in range(10):
            printBoard(theBoard)
            print("Please enter positions from 1 to 9")
            decide_winner(turn)
            print('Turn for ' + turn + '. Move on which space?')
            move = input()
            print(turn)
            theBoard[move] = turn
            if turn == 'X':
                turn = 'O'
            else:
                turn = 'X'


printBoard(theBoard)
