board = [' 'for x in range(10)]

MIN, MAX = -1000, 1000

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
    values = [let]
    print("The optimal value is :", minimax(2, 0, True, values, MIN, MAX))
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
    # values = [let]
    # print("The optimal value is :", minimax(2, 0, True, values, MIN, MAX))
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


def minimax(depth, nodeIndex, maximizingPlayer,
            values, alpha, beta):

    if depth == 3:
        return values[nodeIndex]

    if maximizingPlayer:

        move = MIN

        possible_moves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
        # move = 0

        for let in ['O', 'X']:
            # for i in range(0, 2):
            for i in possible_moves:
                boardCopy = board[:]
                boardCopy[i] = let

                val = minimax(depth + 1, nodeIndex * 2 + i,
                          False, values, alpha, beta)
                move = max(move, val)
                alpha = max(alpha, move)

            # Alpha Beta Pruning
                if beta <= alpha:
                    break

        return move

    else:
        move = MAX
        possible_moves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
        # move = 0
        # Recur for left and
        # right children
        # for i in range(0, 2):
        for let in ['O', 'X']:
            # for i in range(0, 2):
            for i in possible_moves:
                boardCopy = board[:]
                boardCopy[i] = let

                val = minimax(depth + 1, nodeIndex * 2 + i,
                          True, values, alpha, beta)
                best = min(move, val)
                beta = min(beta, best)
                values = [let]
                print("The optimal value is :", minimax(2, 0, True, values, MIN, MAX))

                if beta <= alpha:
                    break

    return move


# if __name__ == "__main__":
#3, 5, 6, 9, 1, 2, 0, -1
values = [3, 5, 6, 9, 1, 2, 0, -1]
print("The optimal value is :", minimax(2, 0, True, values, MIN, MAX))







