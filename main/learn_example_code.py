def tic_tac_toe_winner(board):
    # Check for row win
    # Ensure we do not consider 3 empty strings a win
    for row in range(3):
        if (board[row][0] == board[row][1] 
                and board[row][1] == board[row][2]
                and board[row][0] != ''):
            return board[row][0]

    # Check for column win
    for column in range(3):
        if (board[0][column] == board[1][column] 
                and board[1][column] == board[2][column]
                and board[0][column] != ''):
            return board[0][column]

    # Check for diagonal wins
    if (board[0][0] == board[1][1] 
            and board[1][1] == board[2][2]
            and board[0][0] != ''):
        return board[0][0]
    elif (board[0][2] == board[1][1] 
            and board[1][1] == board[2][0]
            and board[0][2] != ''):
        return board[0][2]

    # If none of these conditions match, check for game in progress
    for row in board:
        # If any space is '' --> Return None for 'game in progress'
        if '' in row:
            return None
    
    # If there is no winner and no open spaces, then the game is tied
    return 'Tie'