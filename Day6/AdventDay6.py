import numpy as np

if (__name__ == '__main__'):
    # Open the input file "input.txt" in read mode
    with open("input6.txt", "r") as f:
        lines = f.readlines()  # Read all lines from the file into a list
        # Initialize variables
        final_sum = 0  
        array = np.array([])
        product = 1

        # Process each line in the input file
        for line in lines:
            line = line.strip().split()
            # Append the line to the array
            array = np.append(array, line)

        # Reshape the array and rotate it
        array = np.rot90(array.reshape((len(lines), len(line))))

        # Calculate the final sum based on the last element of each row
        for i in range(array.shape[0]):
            # Check the last element to determine operation
            if array[i][-1] == '+':
                # Sum all but the last element
                final_sum += sum(array[i][:-1].astype(int))
            elif array[i][-1] == '*':
                # Multiply all but the last element
                product = 1
                for num in array[i][:-1].astype(int):
                    product *= num
                final_sum += product

        # Print the final sum
        print(final_sum)  