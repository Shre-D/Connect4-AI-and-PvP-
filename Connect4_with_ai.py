import numpy as np
import random
import math

ROW=6
COL=7
player1=0
player2=1
ai=1
play1=1
play2=2
BLOCK_LEN=4
EMPTY=0

def gameboard():
    board=np.zeros((ROW,COL))
    return board

def valid(board,choice):
    if board[5][choice-1]==0:
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
    
def evaluation(block,player):
    score=0
    opponent=player1
    if player==player1:
        player==play2
        
    if block.count(player)==4:
        score+=100
    elif block.count(player)==3 and block.count(EMPTY)==1:
        score+=10
    elif block.count(player)==2 and block.count(EMPTY)==2:
        score+=1
    if block.count(opponent)==3 and block.count(EMPTY)==1:
        score-=5
        
    return score
    
def score_system(board,player):
    score=0
    #preference for the centre
    center_array = [int(i) for i in list(board[:, COL//2])]
    center_count = center_array.count(player)
    score=score+center_count*3
	
    #creating blocks of 4
    
    #horizontal systems
    
    for i in range (ROW):
        row_vals = board[i]
        for j in range (COL-3):
            block=list(row_vals[j:j+BLOCK_LEN])
            score=score+evaluation(block,player)
            
    #vertical systems
    
    for j in range (COL):
        col_vals=board.T[i]
        for i in range (COL-3):
            block=list(col_vals[i:i+BLOCK_LEN])
            score=score+evaluation(block,player)  
             
    #positive diagonal systems
    
    for i in range(ROW-3):
        for j in range(COL-3):
            block=[board[i+k][j+k] for k in range(BLOCK_LEN)]
            score=score+evaluation(block,player)
            
    #negative diagonal systems
    
    for i in range(ROW-3):
        for j in range(COL-3):
            block=[board[i+3-k][j+k] for k in range(BLOCK_LEN)]
            score=score+evaluation(block,player)
    return score

def valid_for_ai(board):
	valid_locations = []
	for choice in range(COL):
		if valid(board, choice):
			valid_locations.append(choice)
	return valid_locations

def terminal(board):
    return win(board,play1) or win(board,play2) or len(valid_for_ai(board))==0
    

def AI_minimax(board, depth, alpha, beta, maximizingPlayer):
        valid_locations=valid_for_ai(board)
        is_terminal = terminal(board)
        if depth == 0 or is_terminal:
            if is_terminal:
                if win(board, play2):
                    return (None, math.inf)
                elif win(board, play1):
                    return (None,-math.inf)
                else: 
                    return (None, 0)
            else: 
                return (None, score_system(board, play2))
        if maximizingPlayer:
            value = -math.inf
            column = random.choice(valid_locations)
            for col in valid_locations:
                row = updaterow(board, col)
                duplicate = board.copy()
                makemove(duplicate, row, col, play2)
                new_score = AI_minimax(duplicate, depth-1, alpha, beta, False)[1]
                if new_score > value:
                    value = new_score
                    column = col
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
            return column, value

        else:
            value = math.inf
            column = random.choice(valid_locations)
            for col in valid_locations:
                row = updaterow(board, col)
                duplicate = board.copy()
                makemove(duplicate, row, col, play1)
                new_score = AI_minimax(duplicate, depth-1, alpha, beta, True)[1]  #returns val
                if new_score < value:
                    value = new_score
                    column = col
                beta = min(beta, value)
                if alpha >= beta:
                    break
            return column, value
        
board=gameboard()
game_running=True
select=input("PvP or AI?, p for pvp, a for ai: ")

print(board)
if select=="p":
    turn=0
    while game_running:          
                if turn==player1:
                    choice=int(input("Enter a number from 1 to 7 to play: "))
                    row = updaterow(board, choice)
                    if valid(board,choice) and 1<=choice<=7:
                        makemove(board,row,choice,play1)
                        if win(board,play1):
                            print("Congrats! Player 1 has won")
                            game_running=False
                    else:
                        print("Enter Valid input")
                
                if turn==player2:
                    choice=int(input("Enter a number from 1 to 7 to play: "))
                    row = updaterow(board, choice)
                    if valid(board,choice) and 1<=choice<=7:
                        makemove(board,row,choice,play2)
                        if win(board,play2):
                            print("Congrats! Player 2 has won")
                            game_running=False
                    else:
                        print("Enter Valid input")
                turn+=1
                turn=turn%2
                
                print(print(np.flip(board,0)))
if select=="a":
    turn=random.randint(player1,ai)
    while game_running:
            if turn==player1:
                    choice=int(input("Enter a number from 1 to 7 to play: "))
                    row = updaterow(board, choice)
                    if valid(board,choice) and 1<=choice<=7:
                        makemove(board,row,choice,play1)
                        print("Wait for ai!!")
                        if win(board,play1):
                            print("Congrats! Player 1 has won")
                            game_running=False
                    else:
                        print("Enter Valid input")
                    
            elif turn==ai:                
                choice, minimax_score = AI_minimax(board, 5, -math.inf, math.inf, True)
                if valid(board,choice):
                    row=updaterow(board,choice)
                    makemove(board, row, choice, play2)
                    if win(board, play2):
                        print("Computer wins!!")
                        game_running=False
            turn+=1
            turn=turn%2
            
            print(print(np.flip(board,0)))
            