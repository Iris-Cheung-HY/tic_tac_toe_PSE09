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
    assert result is None



# Test from Learn PSE09

def test_tic_tac_toe_winner_no_winner_returns_tie():
    # Arrange
    board =[
        ['X', 'O', 'X'],
        ['O', 'O', 'X'],
        ['X', 'X', 'O']
    ]

    # Act
    result = tic_tac_toe_winner(board)

    # Assert
    assert result == 'Tie'

def test_tic_tac_toe_winner_incomplete_no_winner_returns_none():
    # Arrange
    board =[
        ['X', 'O', 'X'],
        ['O', 'O', 'X'],
        ['X', '', 'O']
    ]

    # Act
    result = tic_tac_toe_winner(board)

    # Assert
    assert result is None

def test_tic_tac_toe_winner_empty_board_returns_none():
    # Arrange
    board = [
        ['', '', ''],
        ['', '', ''],
        ['', '', '']
    ]

    # Act
    result = tic_tac_toe_winner(board)

    # Assert
    assert result is None

def test_tic_tac_toe_winner_col_win_o():
    # Arrange
    board =[
        ['X', 'O', 'X'],
        ['O', 'O', 'X'],
        ['X', 'O', 'O']
    ]

    # Act
    result = tic_tac_toe_winner(board)

    # Assert
    assert result == 'O'

def test_tic_tac_toe_winner_row_win_x():
    # Arrange
    board =[
        ['O', 'O', 'X'],
        ['X', 'X', 'X'],
        ['O', 'X', 'O']
    ]

    # Act
    result = tic_tac_toe_winner(board)

    # Assert
    assert result == 'X'

def test_tic_tac_toe_winner_diag_win_o():
    # Arrange
    board =[
        ['O', 'O', 'X'],
        ['O', 'O', 'X'],
        ['X', 'X', 'O']
    ]

    # Act
    result = tic_tac_toe_winner(board)

    # Assert
    assert result == 'O'