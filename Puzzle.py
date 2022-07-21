# Ethan Berman

# Shortest path in grid with Obstacles.
# Can start from any vertex, and end in any specified vertex.
# Solved using BFS algorithm.


def check_source_destination_vertices(board, source, destination, row_col_lengths):
    '''Checks that source and destination vertices are valid'''

    # unpack tuple values for row/col lengths
    row_length = row_col_lengths[0]
    col_length = row_col_lengths[1]

    # x and y vertices of the source ordered pair
    source_x = source[0]
    source_y = source[1]

    # x and y vertices of the destination ordered pair
    destination_x = destination[0]
    destination_y = destination[1]

    # raise error if out of valid index range, or if source/destination vertex is a barrier
    if (source_x < 0 or source_x > row_length) or (source_y < 0 or source_y > col_length):
        raise IndexError("invalid source vertex")

    if (destination_x < 0 or destination_x > row_length) or (destination_y < 0 or destination_y > col_length):
        raise IndexError("invalid destination vertex")

    if board[source_x-1][source_y-1] == '#' or board[destination_x-1][destination_y-1] == '#':
        raise ValueError("cannot have source or destination be a barrier (#)")
    


def check_valid_board_dimensions(board):

    # given the matrix has the same col and row lengths, retrieve the length of either
    board_dimension_row = len(board[0])
    board_dimension_col = len([row[0] for row in board])

    # matrix must be at least 3x3
    if board_dimension_row < 3 or board_dimension_col < 3:
        raise ValueError("invalid board dimensions")

    return board_dimension_row, board_dimension_col

def check_bottom_cell(current_vertex, row_col_lengths, board, visited, queue, next_move_cells):

    # unpack x and y coordinates
    current_vertex_x = current_vertex[0]
    current_vertex_y = current_vertex[1]

    # unpack column length
    col_length = row_col_lengths[1]

    # update bottom
    if (current_vertex_x + 1 <= col_length - 1) and \
        (board[current_vertex_x+1][current_vertex_y] != '#') and \
        (visited[current_vertex_x+1][current_vertex_y] != True):
            queue.append([current_vertex_x + 1, current_vertex_y])
            visited[current_vertex_x + 1][current_vertex_y] = True
            next_move_cells += 1
    
    return next_move_cells

def check_top_cell(current_vertex, board, visited, queue, next_move_cells):

    # unpack x and y coordinates
    current_vertex_x = current_vertex[0]
    current_vertex_y = current_vertex[1]

    # update top
    if (current_vertex_x - 1 >= 0) and \
        (board[current_vertex_x-1][current_vertex_y] != '#') and \
        (visited[current_vertex_x-1][current_vertex_y] != True):
            queue.append([current_vertex_x - 1, current_vertex_y])
            visited[current_vertex_x - 1][current_vertex_y] = True
            next_move_cells += 1
    
    return next_move_cells

def check_right_cell(current_vertex, row_col_lengths, board, visited, queue, next_move_cells):

    # unpack x and y coordinates
    current_vertex_x = current_vertex[0]
    current_vertex_y = current_vertex[1]

    # unpack column length
    row_length = row_col_lengths[0]

    # update right
    if (current_vertex_y + 1 <= row_length - 1) and \
        (board[current_vertex_x][current_vertex_y+1] != '#') and \
        (visited[current_vertex_x][current_vertex_y+1] != True):
            queue.append([current_vertex_x, current_vertex_y + 1])
            visited[current_vertex_x][current_vertex_y + 1] = True
            next_move_cells += 1
    
    return next_move_cells

def check_left_cell(current_vertex, board, visited, queue, next_move_cells):
    
    # unpack x and y coordinates
    current_vertex_x = current_vertex[0]
    current_vertex_y = current_vertex[1]
       
    # update left
    if (current_vertex_y - 1 >= 0) and \
        (board[current_vertex_x][current_vertex_y-1] != '#') and \
        (visited[current_vertex_x][current_vertex_y-1] != True):
            queue.append([current_vertex_x, current_vertex_y - 1])
            visited[current_vertex_x][current_vertex_y - 1] = True
            next_move_cells += 1
    
    return next_move_cells

def solve_puzzle(board, source, destination):
    '''Finds shortest path to destination by avoiding barriers'''

    # initialize visited matrix with False values
    visited = [[False for cell in row] for row in board]
    current_move_cells = 1
    next_move_cells = 0
    moves_made = 0

    # get row and col lengths, if valid
    row_col_lengths = check_valid_board_dimensions(board)

    # verifies source and destination vertices are valid
    check_source_destination_vertices(board, source, destination, row_col_lengths)

    # adjust source and destination for 0 indexing
    source = [source[0]-1, source[1]-1]
    destination = [destination[0]-1, destination[1]-1]

    # initialize empty queue
    queue = []
    
    # append source node vertex into queue
    queue.append(source)

    # initialize source vertex cell of visited matrix with True
    visited[source[0]][source[1]] = True
    
    while len(queue) != 0:

        # pop 0th index vertex from queue
        current_vertex = queue.pop(0)

        # if current vertex is destination vertex, return number of moves made
        if current_vertex == destination:
            return moves_made 
        
        # for the following, check if surrounding vertices of current_vertex are either in bounds, True in visited matrix, 
        # or if they equal a # on the board. If condition executes, append vertex to queue, 
        # change visited vertex value to True, and increment next_move_cells.

        next_move_cells = check_top_cell(current_vertex, board, visited, queue, next_move_cells)
        next_move_cells = check_bottom_cell(current_vertex, row_col_lengths, board, visited, queue, next_move_cells)
        next_move_cells = check_left_cell(current_vertex, board, visited, queue, next_move_cells)
        next_move_cells = check_right_cell(current_vertex, row_col_lengths, board, visited, queue, next_move_cells)
        
        current_move_cells -= 1

        # do not count first move from source, otherwise do increment moves_made
        if current_move_cells == 0 and current_vertex == source:
            current_move_cells = next_move_cells
            next_move_cells = 0
        elif current_move_cells == 0 and current_vertex != source:
            moves_made += 1
            current_move_cells = next_move_cells
            next_move_cells = 0

    return None

# if __name__ == "__main__":

#     B = [['-','-','-','-','-'],
#         ['-','-','#','-','-'],
#         ['-','-','-','-','-'],
#         ['#','-','#','#','-'],
#         ['-','#','-','-','-']]

#     print(solve_puzzle(B, [1,1], [5,5]))