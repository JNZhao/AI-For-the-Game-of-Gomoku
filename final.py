
def is_empty(board):
    for i in range (len(board)):
        for j in range (len(board[i])):
            if board[i][j]!=" ":
                return False
    return True
    
    
def is_bounded(board, y_end, x_end, length, d_y, d_x):
    if d_y == 1 and d_x == 0:
        if y_end == 7:
            if length - y_end == 1:
                return "CLOSED"
            if board[y_end-length][x_end]==" ":
                return "SEMIOPEN"
            if board[y_end-length][x_end]!=" ":
                return "CLOSED"
            
        if length - y_end == 1:
            if board[y_end+1][x_end] !=" ":
                return "CLOSED"
            if board[y_end+1][x_end] ==" ":
                 return "SEMIOPEN"
        if board[y_end+1][x_end] !=" ":
            if board[y_end-length][x_end]!=" ":
                return "CLOSED"
            else:
                return "SEMIOPEN"
        if board[y_end+1][x_end] ==" ":
            if board[y_end-length][x_end]!=" ":
                return "SEMIOPEN"
            else:
                return "OPEN"
                
    if d_y == 0 and d_x == 1:
        if x_end == 7:
            if length - x_end ==1:
                return "CLOSED"
            if board[y_end][x_end-length]==" ":
                return "SEMIOPEN"
            if board[y_end][x_end-length]!=" ":
                return "CLOSED"
        if length - x_end ==1:
            if board[y_end][x_end+1]==" ":
                return "SEMIOPEN"
            if board[y_end][x_end+1]!=" ":
                return "CLOSED"
            
            
            
        if board[y_end][x_end+1]!=" ":
            if board[y_end][x_end-length]!=" ":
                return "CLOSED"
            else:
                return "SEMIOPEN"
        if board[y_end][x_end+1]==" ":
            if board[y_end][x_end-length]!=" ":
                return "SEMIOPEN"
            else:
                return "OPEN"
                
                
                
    if d_y == 1 and d_x == -1:
            
        
        if x_end == 0:
            if length - y_end == 1:
                return "CLOSED"
            if board[y_end-length][x_end+length]==" ":
                return "SEMIOPEN"
            if board[y_end-length][x_end+length]!=" ":
                return "CLOSED"
        if y_end == 7:
            if x_end+length == 8:
                 return "CLOSED"
            if board[y_end-length][x_end+length]==" ":
                return "SEMIOPEN"
            if board[y_end-length][x_end+length]!=" ":
                return "CLOSED"
        if length-y_end==1:
            if board[y_end+1][x_end-1]==" ":
                return "SEMIOPEN"
            if board[y_end+1][x_end-1]!=" ":
                return "CLOSED"
        if x_end + length == 8:
            if board[y_end+1][x_end-1]==" ":
                return "SEMIOPEN"
            if board[y_end+1][x_end-1]!=" ":
                return "CLOSED"
                
        if board[y_end+1][x_end-1]!=" ":
            if board[y_end-length][x_end+length]!=" ":
                return "CLOSED"
            else:
                return "SEMIOPEN"
        if board[y_end+1][x_end-1]==" ":
            if board[y_end-length][x_end+length]!=" ":
                return "SEMIOPEN"
            else:
                return "OPEN"
        
    if d_y == 1 and d_x == 1:
        if y_end ==7:
            if length - x_end == 1:
                return "CLOSED"
            if board[y_end-length][x_end-length]==" ":
                return "SEMIOPEN"
            if board[y_end-length][x_end-length]!=" ":
                return "CLOSED"
        
        if x_end == 7:
            if length-y_end == 1:
                return "CLOSED"
            if board[y_end-length][x_end-length]==" ":
                return "SEMIOPEN"
            if board[y_end-length][x_end-length]!=" ":
                return "CLOSED"
        if length - y_end ==1:
            if board[y_end+1][x_end+1]==" ":
                return "SEMIOPEN"
            if board[y_end+1][x_end+1]!=" ":
                return "CLOSED"
        if length - x_end == 1:
            if board[y_end+1][x_end+1]==" ":
                return "SEMIOPEN"
            if board[y_end+1][x_end+1]!=" ":
                return "CLOSED"
        if board[y_end+1][x_end+1]!=" ":
            if board[y_end-length][x_end-length]!=" ":
                return "CLOSED"
            else:
                return "SEMIOPEN"
        if board[y_end+1][x_end+1]==" ":
            if board[y_end-length][x_end-length]!=" ":
                return "SEMIOPEN"
            else:
                return "OPEN"   
                
                 
def detect_row(board, col, y_start, x_start, length, d_y, d_x):
    count = 0
    open_seq_count, semi_open_seq_count = 0,0
    while x_start < 8 and y_start< 8:
        if board[y_start][x_start] == col:
            count+=1
        if board[y_start][x_start] != col:

            if count == length:
                x_start-=d_x
                y_start-=d_y
                if is_bounded(board, y_start, x_start, length, d_y, d_x) == "OPEN":
                    open_seq_count+=1
                if is_bounded(board, y_start, x_start, length, d_y, d_x) == "SEMIOPEN":
                    semi_open_seq_count+=1
                count = 0
            else:
                count = 0
        x_start+=d_x
        y_start+=d_y
        
    if count == length:
        x_start-=d_x
        y_start-=d_y
        if is_bounded(board, y_start, x_start, length, d_y, d_x) == "OPEN":
            open_seq_count+=1
        if is_bounded(board, y_start, x_start, length, d_y, d_x) == "SEMIOPEN":
            semi_open_seq_count+=1
            
    return open_seq_count, semi_open_seq_count

# 
# def detect_row(board, col, y_start, x_start, length, d_y, d_x):
#     open_seq_count, semi_open_seq_count = 0, 0
# 
#     count = 0
#     
#     end_y = y_start
#     end_x = x_start
#     
#     while end_y < (y_start + d_y*len(board)-1) or end_x < (x_start + d_x*len(board)-1):
#        # print ("y")
#         while ( end_y < len(board)-1 and end_x < len(board)-1 ) and board[end_y][end_x] != col :
#            # print ("yo")
#             #count == 0
#             end_y += d_y
#             end_x += d_x
#             
#         while( end_y < len(board) and end_x < len(board) ) and board[end_y][end_x] == col:
#            # print ("hi")
#             #print (end_y, end_x, col)
#             count += 1
#             end_y += d_y
#             end_x += d_x
#         
#         #print (count)
#         if count == length:
#             pattern = is_bounded(board, end_y-d_y, end_x-d_x, count, d_y, d_x)
#         
#             if pattern == "OPEN":
#                 open_seq_count += 1
#             elif pattern == "SEMIOPEN":
#                 semi_open_seq_count += 1
# 
#         count = 0
#         end_y += d_y
#         end_x += d_x
#     return open_seq_count, semi_open_seq_count
#     
    
def detect_rows(board, col, length):
    open_seq_count, semi_open_seq_count = 0, 0
    open,semi = 0,0

    for i in range (len(board)):
        open,semi = detect_row(board, col, 0, i, length, 1, 0)
        open_seq_count += open
        semi_open_seq_count += semi
        
        open,semi =detect_row(board, col, i, 0, length, 0, 1)
        open_seq_count += open
        semi_open_seq_count += semi
                
    for j in range (1,len(board)):
        open,semi =detect_row(board, col, 0, j, length, 1, -1)
        open_seq_count += open
        semi_open_seq_count += semi 
        
        open,semi =detect_row(board, col, j, 7, length, 1, -1)
        open_seq_count += open
        semi_open_seq_count += semi 
        
        open,semi =detect_row(board, col, j, 0, length, 1, 1)
        open_seq_count += open
        semi_open_seq_count += semi                  
        
    
    for k in range (len(board)-1):
        open,semi =detect_row(board, col, 0, k, length, 1, 1)
        open_seq_count += open
        semi_open_seq_count += semi        
        
    return open_seq_count, semi_open_seq_count
    
def search_max(board):
    temp=-1000000
    tempx,tempy=0,0
    for i in range (len(board)):
        for j in range (len(board[i])):
            if board[i][j]==" ":
                board[i][j]="b"
                if score(board)>temp:
                    temp = score(board)
                    tempx = j
                    tempy = i
                board[i][j]=" "

    move_y = tempy
    move_x = tempx
                
    return move_y, move_x
    
def score(board):
    MAX_SCORE = 100000
    
    open_b = {}
    semi_open_b = {}
    open_w = {}
    semi_open_w = {}
    
    for i in range(2, 6):
        open_b[i], semi_open_b[i] = detect_rows(board, "b", i)
        open_w[i], semi_open_w[i] = detect_rows(board, "w", i)
        
    
    if open_b[5] >= 1 or semi_open_b[5] >= 1:
        return MAX_SCORE
    
    elif open_w[5] >= 1 or semi_open_w[5] >= 1:
        return -MAX_SCORE
        
    return (-10000 * (open_w[4] + semi_open_w[4])+ 
            500  * open_b[4]                     + 
            50   * semi_open_b[4]                + 
            -100  * open_w[3]                    + 
            -30   * semi_open_w[3]               + 
            50   * open_b[3]                     + 
            10   * semi_open_b[3]                +  
            open_b[2] + semi_open_b[2] - open_w[2] - semi_open_w[2])

    
def is_win(board):
    w_open,w_semi= detect_rows(board, "w", 5)
        
    b_open,b_semi= detect_rows(board, "b", 5)
    
    if w_open>=1 or w_semi >=1:
        return "White won"
    if b_open>=1 or b_semi>=1:
        return "Black won"

    if is_full(board)==True:
        return "Draw"
    else:
        return "Continue playing"


def is_full(board):
    for i in range (len(board)):
        for j in range (len(board[i])):
            if board[i][j]==" ":
                return False
    return True

def print_board(board):
    
    s = "*"
    for i in range(len(board[0])-1):
        s += str(i%10) + "|"
    s += str((len(board[0])-1)%10)
    s += "*\n"
    
    for i in range(len(board)):
        s += str(i%10)
        for j in range(len(board[0])-1):
            s += str(board[i][j]) + "|"
        s += str(board[i][len(board[0])-1]) 
    
        s += "*\n"
    s += (len(board[0])*2 + 1)*"*"
    
    print(s)
    

def make_empty_board(sz):
    board = []
    for i in range(sz):
        board.append([" "]*sz)
    return board
                


def analysis(board):
    for c, full_name in [["b", "Black"], ["w", "White"]]:
        print("%s stones" % (full_name))
        for i in range(2, 6):
            open, semi_open = detect_rows(board, c, i);
            print("Open rows of length %d: %d" % (i, open))
            print("Semi-open rows of length %d: %d" % (i, semi_open))
        
    
    

        
    
def play_gomoku(board_size):
    board = make_empty_board(board_size)
    board_height = len(board)
    board_width = len(board[0])
    
    while True:
        print_board(board)
        if is_empty(board):
            move_y = board_height // 2
            move_x = board_width // 2
        else:
            move_y, move_x = search_max(board)
            
        print("Computer move: (%d, %d)" % (move_y, move_x))
        board[move_y][move_x] = "b"
        print_board(board)
        analysis(board)
        
        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res
            
            
        
        
        
        print("Your move:")
        move_y = int(input("y coord: "))
        move_x = int(input("x coord: "))
        board[move_y][move_x] = "w"
        print_board(board)
        analysis(board)
        
        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res
        
            
            
def put_seq_on_board(board, y, x, d_y, d_x, length, col):
    for i in range(length):
        board[y][x] = col        
        y += d_y
        x += d_x


def test_is_empty():
    board  = make_empty_board(8)
    if is_empty(board):
        print("TEST CASE for is_empty PASSED")
    else:
        print("TEST CASE for is_empty FAILED")

def test_is_bounded():
    board = make_empty_board(8)
    x = 5; y = 3; d_x = 1; d_y = 0; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    
    y_end = 3
    x_end = 7

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'SEMIOPEN':
        print("TEST CASE for is_bounded PASSED")
    else:
        print("TEST CASE for is_bounded FAILED")

def test_detect_row():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_row(board, "w", 0,x,length,d_y,d_x) == (1,0):
        print("TEST CASE for detect_row PASSED")
    else:
        print("TEST CASE for detect_row FAILED")

def test_detect_rows():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_rows(board, col,length) == (1,0):
        print("TEST CASE for detect_rows PASSED")
    else:
        print("TEST CASE for detect_rows FAILED")

def test_search_max():
    board = make_empty_board(8)
    x = 5; y = 0; d_x = 0; d_y = 1; length = 4; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    x = 6; y = 0; d_x = 0; d_y = 1; length = 4; col = 'b'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    print_board(board)
    if search_max(board) == (4,6):
        print("TEST CASE for search_max PASSED")
    else:
        print("TEST CASE for search_max FAILED")

def easy_testset_for_main_functions():
    test_is_empty()
    test_is_bounded()
    test_detect_row()
    test_detect_rows()
    test_search_max()

def some_tests():
    board = make_empty_board(8)

    board[0][5] = "w"
    board[0][6] = "b"
    y = 5; x = 2; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    analysis(board)
    
    # Expected output:
    #       *0|1|2|3|4|5|6|7*
    #       0 | | | | |w|b| *
    #       1 | | | | | | | *
    #       2 | | | | | | | *
    #       3 | | | | | | | *
    #       4 | | | | | | | *
    #       5 | |w| | | | | *
    #       6 | |w| | | | | *
    #       7 | |w| | | | | *
    #       *****************
    #       Black stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 0
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    #       White stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 1
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    
    y = 3; x = 5; d_x = -1; d_y = 1; length = 2
    
    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    print_board(board)
    analysis(board)
    
    # Expected output:
    #        *0|1|2|3|4|5|6|7*
    #        0 | | | | |w|b| *
    #        1 | | | | | | | *
    #        2 | | | | | | | *
    #        3 | | | | |b| | *
    #        4 | | | |b| | | *
    #        5 | |w| | | | | *
    #        6 | |w| | | | | *
    #        7 | |w| | | | | *
    #        *****************
    #
    #         Black stones:
    #         Open rows of length 2: 1
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 0
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #         White stones:
    #         Open rows of length 2: 0
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 1
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #     
    
    y = 5; x = 3; d_x = -1; d_y = 1; length = 1
    put_seq_on_board(board, y, x, d_y, d_x, length, "b");
    print_board(board);
    analysis(board);
    
    #        Expected output:
    #           *0|1|2|3|4|5|6|7*
    #           0 | | | | |w|b| *
    #           1 | | | | | | | *
    #           2 | | | | | | | *
    #           3 | | | | |b| | *
    #           4 | | | |b| | | *
    #           5 | |w|b| | | | *
    #           6 | |w| | | | | *
    #           7 | |w| | | | | *
    #           *****************
    #        
    #        
    #        Black stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0
    #        White stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0


  
            
if __name__ == '__main__':
    
    #play_gomoku(8)
    #print(test_detect_rows())
    #print(some_tests())
    # board = make_empty_board(8)
    # board =[[' ', 'b', ' ', ' ', ' ', 'w', 'b', ' '],
    #         [' ', 'b', ' ', ' ', 'w', ' ', ' ', ' '],
    #         [' ', 'b', ' ', 'w', ' ', ' ', ' ', ' '],
    #         [' ', 'b', 'w', 'w', ' ', 'b', ' ', ' '],
    #         [' ', ' ', ' ', ' ', 'b', ' ', 'b', ' '],
    #         [' ', ' ', 'w', 'b', ' ', 'w', ' ', 'b'],
    #         [' ', ' ', 'w', ' ', ' ', 'w', ' ', ' '],
    #         [' ', ' ', 'w', ' ', ' ', 'w', ' ', ' ']]
    # print_board(board)
    # if detect_row(board, "b", 3,5,3,1,-1) == (0,1):
    #     print("TEST CASE for detect_row PASSED")
    # else:
    #     print("TEST CASE for detect_row FAILED")  
    
    #board = make_empty_board(8)
    #board[4][4] = "b"
    #board[3][3] = "b"
    #board[4][3] = "w"
    #print_board(board)
    #detect_row(board,"b", 0, 0, 2, 1, 1)
    #detect_rows(board,"b",2)
    # board = make_empty_board(8)
    # board[0][5]="w"
    # board[1][4]="w"
    # board[2][3]="w"
    # board[3][2]="w"
    # detect_rows(board, "w", 4)
    # print(analysis(board))
    # board = make_empty_board(8)
    # board=[['w', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    #        [' ', 'w', ' ', ' ', ' ', ' ', ' ', ' '],
    #        [' ', ' ', 'w', ' ', ' ', ' ', ' ', ' '],
    #        [' ', ' ', ' ', 'b', ' ', ' ', ' ', ' '],
    #        [' ', ' ', ' ', ' ', 'b', ' ', ' ', ' '],
    #        [' ', ' ', ' ', ' ', ' ', 'b', ' ', ' '],
    #        [' ', ' ', ' ', ' ', ' ', ' ', 'b', ' '],
    #        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
    # print(analysis(board))
    easy_testset_for_main_functions()
