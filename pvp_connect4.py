import numpy as np

ROW=6
COL=7
player1=0
player2=1
ai=1
play1=1
play2=2
playai=2
BLOCK_LEN=4
EMPTY=0

def gameboard():
    board=np.zeros((ROW,COL))
    return board

def valid(board,choice,row):
    if board[row][choice-1]==0:
        return True
    return False

def updaterow(board,choice):

    for row in range(ROW):
        if board[row][choice-1]==0:
            return row

def win(board,player):
    for j in range(COL - 3):
        for i in range(ROW):
            if board[i][j] == player and board[i][j + 1] == player and board[i][j + 2] == player and board[i][j + 3] == player:
                return True
    for j in range(COL):
        for i in range(ROW - 3):
            if board[i][j] == player and board[i + 1][j] == player and board[i + 2][j] == player and board[i + 3][j] == player:
                return True
    for j in range(COL - 3):
        for i in range(ROW - 3):
            if board[i][j] == player and board[i + 1][j + 1] == player and board[i + 2][j + 2] == player and board[i + 3][j + 3] == player:
                return True
    for j in range(COL - 3):
        for i in range(3, ROW):
            if board[i][j] == player and board[i - 1][j + 1] ==player and board[i - 2][j + 2] == player and board[i - 3][j + 3] == player:
                return True
    return False

def makemove(board,row,choice,player):
    board[row][choice-1]=player

board=gameboard()
#turn=random.randint(player1,ai)
turn=0
game_running=True


print(board)
while game_running:          
            if turn==player1:
                choice=int(input("Enter a number from 1 to 7 to play: "))
                row = updaterow(board, choice)
                if valid(board,choice,row) and 1<=choice<=7:
                    makemove(board,row,choice,play1)
                    if win(board,play1):
                        print("Congrats! Player 1 has won")
                        game_running=False
                else:
                    print("Enter Valid input")
            
            if turn==player2:
                choice=int(input("Enter a number from 1 to 7 to play: "))
                row = updaterow(board, choice)
                if valid(board,choice,row) and 1<=choice<=7:
                    makemove(board,row,choice,play2)
                    if win(board,play2):
                        print("Congrats! Player 2 has won")
                        game_running=False
                else:
                    print("Enter Valid input")
            turn+=1
            turn=turn%2
            print(print(np.flip(board,0)))