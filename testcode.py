
def test_is_bounded():
    board = make_empty_board(8)
    y = 5; x = 4; d_y=1; d_x =-1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "b");
    print_board(board);
    y = 4; x = 5; d_y=1; d_x =-1; length = 1
    put_seq_on_board(board, y, x, d_y, d_x, length, "w");
    print_board(board);    
    y_end = 7
    x_end = 2

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'CLOSED':
        print("TEST CASE for is_bounded PASSED")
    else:
        print("TEST CASE for is_bounded FAILED")
            
def test_is_bounded():
    board = make_empty_board(8)
    y = 3; x = 2; d_y=1; d_x =-1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "b");
    print_board(board);
    y = 2; x = 3; d_y=1; d_x =-1; length = 1
    put_seq_on_board(board, y, x, d_y, d_x, length, "w");
    print_board(board);    
    y_end = 5
    x_end = 0

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'CLOSED':
        print("TEST CASE for is_bounded PASSED")
    else:
        print("TEST CASE for is_bounded FAILED")

def test_is_bounded():
    board = make_empty_board(8)
    y = 2; x = 0; d_y=1; d_x =-1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "b");
    print_board(board);
    
    y_end = 5
    x_end = 0

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'CLOSED':
        print("TEST CASE for is_bounded PASSED")
    else:
        print("TEST CASE for is_bounded FAILED")
        
def test_is_bounded():
    board = make_empty_board(8)
    y = 6; x = 7; d_y=1; d_x =-1; length = 2
    put_seq_on_board(board, y, x, d_y, d_x, length, "b");
    print_board(board);
    
    y_end = 7
    x_end = 6

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'CLOSED':
        print("TEST CASE for is_bounded PASSED")
    else:
        print("TEST CASE for is_bounded FAILED")
def test_is_bounded():
    board = make_empty_board(8)
    y = 0; x = 6; d_y=1; d_x =1; length = 2
    put_seq_on_board(board, y, x, d_y, d_x, length, "b");
    print_board(board);
    
    y_end = 1
    x_end = 7

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'CLOSED':
        print("TEST CASE for is_bounded PASSED")
    else:
        print("TEST CASE for is_bounded FAILED")
    
def test_is_bounded():
    board = make_empty_board(8)
    y = 6; x =7; d_y=1; d_x =-1; length = 2
    put_seq_on_board(board, y, x, d_y, d_x, length, "b");
    print_board(board);
    
    y_end = 7
    x_end = 6

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'CLOSED':
        print("TEST CASE for is_bounded PASSED")
    else:
        print("TEST CASE for is_bounded FAILED")