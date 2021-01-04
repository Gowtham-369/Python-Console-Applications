
########################## MINMAX strategy ########################
import numpy as np
board = np.array([['-','-','-'],['-','-','-'],['-','-','-']])
p1_sym = 'X'
p2_sym = 'O'
turn = 0
def check_rows(symbol):
    for r in range(3): #0,1,2
        count = 0
        for c in range(3):
            if(board[r][c] == symbol):
                count+=1
        if(count == 3):
            print(symbol,"Won!!")
            return True
    return False #No win
    
def check_cols(symbol):
    for c in range(3): #0,1,2
        count = 0
        for r in range(3):
            if(board[r][c] == symbol):
                count+=1
        if(count == 3):
            print(symbol,"Won!!")
            return True
    return False #No win

def check_diagonals(symbol):
    if(board[0][0] == symbol and board[1][1]==symbol and board[2][2] == symbol):
        print(symbol,"Won!!")
        return True
    elif(board[0][2] == symbol and board[1][1]==symbol and board[2][0] == symbol):
        print(symbol,"Won!!")
        return True
    else:
        return False
    
def won(symbol):
    #check that symbol is across each row or colomn or in any of diagonals
    return check_diagonals(symbol) or check_rows(symbol) or check_cols(symbol)

def place(symbol):
    print(np.matrix(board))
    while(True):
        row = int(input("Enter row number : 1 or 2 or 3 : "))
        col = int(input("Enter colomn number : 1 or 2 or 3 : "))
        if(row>0 and row<4 and col>0 and col<4 and board[row-1][col-1] == '-'):
            break
        else:
            print("Invalid input,Try Again!")
    board[row-1][col-1] = symbol

def play():
    global turn
    for i in range(9):
        if(turn%2 == 0):
            #p1 turn at turn = 0,2,4,6,8
            print("'X' turn ")
            place(p1_sym)
            if won(p1_sym):
                break
        else:
            #p2 turn
            print("'O' turn ")
            place(p2_sym)
            if won(p2_sym):
                break
        turn+=1
    if not(won(p1_sym)) and not(won(p2_sym)):
        print("Game Results in Draw")
        
play()