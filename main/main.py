def tic_tac_toe_winner(board):

    for row in board:
        if row[0] == row[1] == row[2]:
            return row[0]
        elif board[0][0] == board[1][0] == board[2][0]:
            return board[0][0]
        elif board[0][1] == board[1][1] == board[2][1]:
            return board[0][1]
        elif board[0][2] == board[1][2] == board[2][2]:
            return board[0][2]
        elif board[0][0] == board[1][1] == board[2][2]:
            return board[0][0]
        elif board[2][0] == board[1][1] == board[0][2]:
            return board[2][0]
        else:
            if row[0] == "" or row[1] == "" or row[2] == "":
                return None
            return "Tie"



