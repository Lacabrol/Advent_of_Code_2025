if (__name__ == '__main__'):
    # Open the input file "input.txt" in read mode
    with open("input1.txt", "r") as f:

        lines = f.readlines()  # Read all lines from the file into a list
        position = 50  # Initialize the starting position
        final_sum = 0  # Initialize the final sum to zero

        for line in lines:
            # Check if the line starts with 'L'
            if line[0] == 'L':  
                # Move left by the specified amount
                position -= int(line[1:])  
                # If position goes below 0
                if position < 0:  
                    # Wrap around to the end (100)
                    position=(100 + position)%100  

            # Check if the line starts with 'R'
            elif line[0] == 'R':  
                # Move right by the specified amount
                position += int(line[1:])
                # Wrap around to the start (0)  
                position=position%100  
            
            # Count how many times we stopped at position 0
            if position == 0:
                final_sum += 1

        print(final_sum)  # Print the final sum