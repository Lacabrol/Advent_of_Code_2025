if (__name__ == '__main__'):
    # Open the input file "input.txt" in read mode
    with open("input4.txt", "r") as f:

        lines = f.readlines()  # Read all lines from the file into a list
        
        # Initialize variables
        neighbours = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        nb_neighbours = 0
        final_sum = 0
        current_line=""
        removed = -1

        # Repeat the process until no more '@' can be removed
        while removed != 0:
            # Initialize the count of removed '@' characters
            removed = 0
            for i in range(len(lines)):
                # Process each line to count '@' characters with 3 or fewer neighbors
                current_line = lines[i].strip()
                for j in range(len(current_line)):
                    # Check if the current character is '@'
                    if current_line[j] == '@':
                        # Check all 8 possible neighbors
                        for x_neighbour, y_neighbour in neighbours:
                            x, y = j + x_neighbour, i + y_neighbour
                            # Ensure neighbor is within bounds
                            if 0 <= x < len(current_line) and 0 <= y < len(lines):
                                # Check if the neighbor character is '@'
                                if lines[y].strip()[x] == '@':
                                    nb_neighbours += 1
                                    
                        # If 3 or fewer neighbors, remove the '@' and increment removed count
                        if nb_neighbours <= 3:
                            lines[i] = lines[i][:j] + '.' + lines[i][j+1:]
                            removed += 1
                        nb_neighbours = 0
                        
            # Add the number of removed '@' characters to the final sum
            final_sum += removed

        print(final_sum)  

