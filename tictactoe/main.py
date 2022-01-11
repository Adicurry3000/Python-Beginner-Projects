board = [' 'for x in range(10)]


def insert_letter(letter, pos):
    board[pos] = letter


def space_is_free(pos):
    return board[pos] == " "

def print_board(board):
    print('   |   |')
    print(' ' + board[1]+ " | "+ board[2]+ ' | '+ board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + " | " + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + " | " + board[8] + ' | ' + board[9])
    print('   |   |')

def is_winner(bo, le):
    return (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or (bo[1] == le and bo[2] == le and bo[3] == le) or (bo[1] == le and bo[4] == le and bo[7] == le) or (bo[2] == le and bo[5] == le and bo[8] == le) or (bo[3] == le and bo[6] == le and bo[9] == le) or (bo[1] == le and bo[5] == le and bo[9] == le) or(bo[3] == le and bo[5] == le and bo[7] == le)

def is_board_full(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def player_move():
    run = True
    while run:
        move = input("Please select a position to place an 'X'  (1-9): ")
        try:
            move= int(move)
            if move>0 and move<10:
                if space_is_free(move):
                    run = False
                    insert_letter("X", move)
                else:
                    print('Sorry this space is occupied!')
            else:
                print('Please type a number within the range!')
        except:
            print('Please type a number!')


def comp_move():
    possible_moves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possible_moves:
            boardCopy = board[:]
            boardCopy[i] = let
            if is_winner(boardCopy, let):
                move = i
                return move
    corner_open = []
    for i in possible_moves:
        if i in[1,3,7,9]:
            corner_open.append(i)
    if len(corner_open)>0:
        move = select_random(corner_open)
        return move

    if 5 in possible_moves:
        move = 5
        return move

    edge_open = []
    for i in possible_moves:
        if i in [2, 4, 6, 8]:
            edge_open.append(i)
    if len(edge_open) > 0:
        move = select_random(edge_open)

    return move


def select_random(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]

def main():
    print('welcome to tic tac toe')
    print_board(board)

    while not (is_board_full(board)):
        if not (is_winner(board, 'O')):
            player_move()
            print_board(board)
        else:
            print('sorry, O\'s won this time!')
            break

        if not (is_winner(board, 'X')):
            move = comp_move()
            if move == 0:
                print('Tie Game!')
            else:
                insert_letter('O', move)
                print("Computer placed an 'O' in", move)
                print_board(board)
        else:
            print('X\'s won this time!, Good Job!')
            break
    if is_board_full(board):
        print('Tie Game!')

main()

# def minimax(pos, depth, max_player, game):
#     if depth == 0 or is_winner() != None:
#         return comp_move().evaluate(), position
#
#     if max_player:
#         maxEval = float('-inf')
#         best_move = None
#         if space_is_free(pos) == True:
#             evaluation = minimax(comp_move(), depth-1, False, game)[0]
#             maxEval = max(maxEval, evaluation)
#             if maxEval == evaluation:
#                 best_move = comp_move()
#         return maxEval, best_move
#     else:
#         minEval = float('inf')
#         best_move = None
#         if space_is_free(pos) == True:
#             evaluation = minimax(move, depth - 1, True, game)[0]
#             minEval = min(minEval, evaluation)
#             if minEval == evaluation:
#                 best_move = move
#         return minEval, best_move
#
# def simulate_move(piece, move, board, game, skip):
#     board.move(piece, move[0], move[1])
#     if skip:
#         board.remove(skip)
#     return board
#
# def get_all_moves(board, color, game):
#     moves = []
#     for piece in board.get_all_pieces(color):
#         valid_moves = board.get_valid_moves(piece)
#         for move, skip in valid_moves.items():
#             temp_board = deepcopy(board)
#             temp_piece = temp_board.get_piece(piece.row, piece.col)
#             new_board = simulate_move(temp_piece, move, temp_board, game, skip)
#             moves.append(new_board)
#
#     return moves






