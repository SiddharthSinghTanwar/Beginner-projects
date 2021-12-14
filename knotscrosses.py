# Establishing who moves first
# Input stored in response
import random

while True:
    print('Choose who moves first')
    response = input('Type Me or You\n')
    if response.lower() not in ('Me','you','You','me'):
        print('not an appropriate choice')
    else:
        break
# Storing response as first move for user or computer
if response == 'Me' or 'me':
    f_move= 'user'
else:
    f_move = 'computer'
# Taking input on either knots or crosses
# Stored in u_symbol and c_symbol
while True:
    choice = input('Choose your symbol: O or X\n')
    if choice == 'O':
        u_symbol = 'O'
        c_symbol = 'X'
        break
    elif choice == 'X':
        u_symbol = 'X'
        c_symbol = 'O'
        break
    else:
        print('Inappropriate response')
        continue
# Board
d_board = {'tl':0, 'tm':1, 'tr':2, 'ml':0, 'c':1, 'mr':2, 'll':0, 'lm':1, 'lr':2}
top_list = ['tl','tm','tr']
mid_list = ['ml','c','mr']
bot_list = ['ll','lm','lr']
def display():
    print('The board looks like this:')
    print(f'{top_list[0]} | {top_list[1]} | {top_list[2]}')
    print('-------------')
    print(f'{mid_list[0]} | {mid_list[1]} | {mid_list[2]}')
    print('-------------')
    print(f'{bot_list[0]} | {bot_list[1]} | {bot_list[2]}')
display()
# list of moves made
c_moves = [['','',''],['','',''],['','','']]
u_moves = [['','',''],['','',''],['','','']]

# Winning Combinations
def wins():
    winner = [(top_list[0],top_list[1],top_list[2]), (top_list[0],mid_list[0],bot_list[0]), (top_list[0],mid_list[1],bot_list[2]), 
            (top_list[1],mid_list[1],bot_list[1]), (top_list[2],mid_list[2],bot_list[2]), (mid_list[0],mid_list[1],mid_list[2]),
            (bot_list[0],bot_list[1],bot_list[2]), (bot_list[0],mid_list[1],top_list[2])]
    return winner

# Editing board, called by userTurn or compTurn
def editBoard(move,symbol):
    print('move',move,'symbol',symbol,'d_board[move]',d_board[move]) # for debugging
    if move in top_list:
        top_list[d_board[move]] = symbol
        d_board.pop(move)
        #u_moves[0][d_board[move]] = symbol
    elif move in mid_list:
        mid_list[d_board[move]] = symbol
        d_board.pop(move)
        #u_moves[1][d_board[move]] = symbol
    elif move in bot_list:
        bot_list[d_board[move]] = symbol
        d_board.pop(move)
        #u_moves[2][d_board[move]] = symbol
    print(top_list, mid_list,bot_list) # for debugging

#checking for winner
def userWin():
    win = wins()
    for element in win:
        if element == (u_symbol,u_symbol,u_symbol):
            #print('element',element) #for debugging
            print('You won the game')
            return True

def compWin():
    win = wins()
    for element in win:
        if element == (c_symbol,c_symbol,c_symbol):
            #print('element',element) #for debugging
            print('Computer won the game')
            return True
# moves
def userTurn():
    print('type where you want to place your marker')
    move = input()
    while True:
        if move not in d_board:
            print('Type the place from the grid to place marker')
        else:
            break
    editBoard(move,u_symbol)
    display()

def compTurn():
    move = random.choice(list(d_board))
    print('move made by computer',move)
    editBoard(move,c_symbol)
    display()

# The game starts
for i in range(9):
    # Placing the marker and editing the board for user
    if f_move=='user':
        userTurn()
        if userWin() == True:
                break

        if d_board:
            compTurn()
            if compWin() == True:
                break

        else:
            
            print('Ran out of grid spaces')
            break
    else:     
        # Placing the marker for computer
        compTurn()
        if compWin() == True:
                break

        if d_board:
            userTurn()
            if userWin() == True:
                break

        else:
            
            print('Ran out of grid spaces')
            break
