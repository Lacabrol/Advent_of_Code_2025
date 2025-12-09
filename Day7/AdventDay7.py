import numpy as np

def is_valid_move(array, row, col):
    if 0 <= row < array.shape[0] and 0 <= col < array.shape[1]:
        return True
    return False

if (__name__ == '__main__'):
    # Open the input file "input.txt" in read mode
    with open("input7.txt", "r") as f:
        lines = f.readlines()  # Read all lines from the file into a list
        # Initialize variables
        final_sum = 0
        array = np.array([])
        stack = []
        beam_row, beam_col = -1, -1
        for line in lines:
            line = list(line.strip())
            # Append the line to the array
            array = np.append(array, line)
        # Reshape the array and rotate it
        array = array.reshape((len(lines), len(line)))
        # Find the starting position 'S'
        beam_row, beam_col = np.where(array == 'S')
        # Start the beam traversal
        stack.append((beam_row[0], beam_col[0]))
        # Traverse the array using a stack
        while len(stack) > 0:
            # Pop the current position from the stack
            beam_row, beam_col = stack.pop()
            # Check if it is possible to move down
            if is_valid_move(array, beam_row+1, beam_col):
                # If the position below is empty
                if (array[beam_row+1][beam_col] == '.'):
                    stack.append((beam_row+1, beam_col))
                    # Mark as visited
                    array[beam_row+1][beam_col] = '|' 

                # If the position below is a splitter
                elif (array[beam_row+1][beam_col] == '^'):
                    # Increment the final sum for each splitter encountered
                    final_sum += 1
                    # Add both diagonal positions to the stack if valid
                    if is_valid_move(array, beam_row+1, beam_col+1) and (beam_row+1, beam_col+1) not in stack:
                        stack.append((beam_row+1, beam_col+1))
                        # Mark as visited
                        array[beam_row+1][beam_col+1] = '|'  
                    if is_valid_move(array, beam_row+1, beam_col-1) and (beam_row+1, beam_col-1) not in stack:
                        stack.append((beam_row+1, beam_col-1))
                        # Mark as visited
                        array[beam_row+1][beam_col-1] = '|' 

        print(final_sum)
                    