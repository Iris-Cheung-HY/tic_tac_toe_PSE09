from main.main import tic_tac_toe_winner



def test_O_column_winner():
    board = [
    ['X', 'O', 'X'],
    ['O', 'O', 'X'],
    ['X', 'O', '']
    ]
    
    # act
    result = tic_tac_toe_winner(board)
    # assert
    assert result == "O"

def test_X_first_column_winner():
    board = [
    ['X', 'O', 'X'],
    ['X', 'X', 'O'],
    ['X', 'O', 'O']
    ]
    
    # act
    result = tic_tac_toe_winner(board)
    # assert
    assert result == "X"

def test_X_row_winner():
    board = [
    ['X', 'X', 'X'],
    ['O', 'X', 'O'],
    ['X', 'O', 'O']
    ]
    
    # act
    result = tic_tac_toe_winner(board)
    # assert
    assert result == "X"

def test_X_winner():
    board = [
    ['X', 'O', 'O'],
    ['O', 'X', 'O'],
    ['', '', 'X']
    ]

    
    # act
    result = tic_tac_toe_winner(board)
    # assert
    assert result == "X"


def test_tie_case():
    board = [
    ['X', 'O', 'X'],
    ['O', 'O', 'X'],
    ['X', 'X', 'O']
    ]
    
    # act
    result = tic_tac_toe_winner(board)
    # assert
    assert result == "Tie"

def test_in_progress_case():
    board = [
    ['X', '', 'O'],
    ['O', 'X', 'X'],
    ['', '', '']
    ]
    
    # act
    result = tic_tac_toe_winner(board)
    # assert
    assert result == None