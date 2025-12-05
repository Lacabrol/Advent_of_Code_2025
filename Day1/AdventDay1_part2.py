if __name__ == '__main__':
    # Open the input file "input.txt" in read mode
    with open("input1.txt", "r") as f:
        lines = f.readlines() # Read all lines from the file into a list

        # Initialize variables
        position = 50
        final_sum = 0
        step = 0

        for line in lines:
            
            # Determine direction
            if line[0] == "L":
                step = -1 
            elif line[0] == "R":
                step = 1

            # Simulate each click
            for i in range(int(line[1:])):
                position = (position + step) % 100
                # Check if we stopped at position 0
                if position == 0:
                    final_sum += 1

        print(final_sum)
