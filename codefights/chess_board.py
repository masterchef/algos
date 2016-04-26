def ChessboardShapes(squares):
    if len(squares) == 0:
        return 1
    # Map columns to letters for lookup
    column_map = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    board = [[0 for x in range(8)] for y in range(8)]
    # initialize board with black squares
    last_value = False
    for row in range(0, len(board)):
        for col in range(0, len(board)):
            key = column_map[col] + str(9 - (row+1))
            # Mark square as True if we have it colored in
            if key in squares:
                board[row][col] = True
            else:
                board[row][col] = last_value
                
            if last_value:
                last_value = False
            else:
                last_value = True
        if last_value:
            last_value = False
        else:
            last_value = True
    #print board
    checked = {}
    largest_count = 0
    # Run deapth first search from every black square and count the largest area
    for row in range(0, len(board)):
        for col in range(0, len(board)):
            # if we found a black square we haven't checked yet traverse the graph and compute
            # largest area
            moves = []
            if board[row][col] and (str(row) + '-' + str(col)) not in checked.keys():
                moves.append([row, col])
                count = 0
                while True:
                    if len(moves) == 0:
                        break
                    # Update count with self
                    count += 1
                    current_step = moves.pop(0)
                    current_row = current_step[0]
                    current_col = current_step[1]
                    #print current_row, current_col, count
                    # Update that we checked it
                    checked[str(current_row) + '-' + str(current_col)] = 1
                    # Check down
                    key = str(current_row+1) + '-' + str(current_col)
                    if current_row + 1 < len(board) and board[current_row+1][current_col] and key not in checked.keys() and [current_row+1, current_col] not in moves:
                        moves.append([current_row+1, current_col])
                    # Check up
                    key = str(current_row-1) + '-' + str(current_col)
                    if current_row - 1 >= 0 and board[current_row-1][current_col] and key not in checked.keys() and [current_row-1, current_col] not in moves:
                        moves.append([current_row-1, current_col])
                    # Check left
                    key = str(current_row) + '-' + str(current_col-1)
                    if current_col - 1 >= 0 and board[current_row][current_col-1] and key not in checked.keys() and [current_row, current_col-1] not in moves:
                        moves.append([current_row, current_col-1])
                    # Check right
                    key = str(current_row) + '-' + str(current_col+1)
                    if current_col + 1 < len(board) and board[current_row][current_col+1] and key not in checked.keys() and [current_row, current_col+1] not in moves:
                        moves.append([current_row, current_col+1])
                    #print moves
                if count > largest_count:
                    largest_count = count
    return largest_count