def tic_tac_toe_winner(board):
    rows = len(board)
    cols = len(board[0])

    #check row
    for row in range(rows):
        if (board[row][0] == board[row][1]== board[row][2] and
            board[row][0] != ''):
            return board[row][0]
    
    #check col
    for col in range(cols):
        if (board[0][col] == board[1][col] == board[2][col] and 
            board[0][col] != ''):
            return board[0][col]
        
    #check Dianoal
    if (board[0][0] == board[1][1] == board[2][2] and 
        board[0][0] != ''):
            return board[0][0]
    if (board[0][2] == board[1][1] == board[2][0] and
        board[0][2] != ''):
            return board[0][2]
    
    #check Tie or None
    for row in board:
        if '' in row:
            return None
        
    return 'Tie'
    


#     if not check_empty_values(board) and not check_winner(board):
#         return "Tie"
#     elif check_empty_values(board) and not check_winner(board):
#         return None
#     else:
#         return check_winner(board)

# def check_empty_values(board):
#     for row in board:
#         if "" in row:
#             return True

# def check_winner(board):
#     for row in board:
#         for item in row:
#             if item == "X" or item == "O":
#                 if row[0] == row[1] == row[2]:
#                     return row[0]
#                 elif board[0][0] == board[1][0] == board[2][0]:
#                     return board[0][0]
#                 elif board[0][1] == board[1][1] == board[2][1]:
#                     return board[0][1]
#                 elif board[0][2] == board[1][2] == board[2][2]:
#                     return board[0][2]
#                 elif board[0][0] == board[1][1] == board[2][2]:
#                     return board[0][0]
#                 elif board[2][0] == board[1][1] == board[0][2]:
#                     return board[2][0]






