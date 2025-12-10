import numpy as np

def is_valid_move(array, row, col):
    # Check if the move is within the bounds of the array
    return 0 <= row < array.shape[0] and 0 <= col < array.shape[1]

def count_paths(row, col, array, memo): 

    # Initialize position and total paths
    pos = (row, col)
    total = 0

    # If out of bounds, this path ends
    if row >= array.shape[0]:
        return 1  

    # Check if already computed
    if pos in memo:
        return memo[pos]

    # If the position is empty, continue downwards
    if array[row][col] == '.':
        total = count_paths(row + 1, col, array, memo)

    # If the position is a splitter, branch left and right
    elif array[row][col] == '^':
        if is_valid_move(array, row, col - 1):
            total += count_paths(row, col - 1, array, memo)
        if is_valid_move(array, row, col + 1):
            total += count_paths(row, col + 1, array, memo)

    # Memoize the result
    memo[pos] = total
    
    return total

if __name__ == '__main__':
    with open("input7.txt") as f:
         # Open the input file "input.txt" in read mode
        lines = f.readlines()  # Read all lines from the file into a list

        # Initialize variables
        final_sum = 0
        memo = {}
        array = np.array([])

        for line in lines:
            line = list(line.strip())
            # Append the line to the array
            array = np.append(array, line)
        # Reshape the array 
        array = array.reshape((len(lines), len(line)))

        # Find the starting position 'S'
        beam_row, beam_col = np.where(array == 'S')

        # Start counting paths from the position below 'S'
        final_sum = count_paths(beam_row[0]+1, beam_col[0], array, memo)
        print(final_sum)
