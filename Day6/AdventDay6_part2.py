if (__name__ == '__main__'):
    # Open the input file "input.txt" in read mode
    with open("input6.txt", "r") as f:
        lines = f.readlines()  # Read all lines from the file into a list
        
        # Initialize variables
        final_sum = 0  
        product = 1
        number = ''

        signs = lines[-1].split()
        lines = lines[:-1]
        sign = signs[0]

        # Process each column in the input file
        for i in range(len(lines[0])):
            for j in range(len(lines)):
                # Extract number from the current column
                if lines[j][i].isdigit():
                    number += lines[j][i]

            # If no number found, process the sign
            if number == '':
                # If the sign is '*', add the product to final sum and reset product
                if sign == '*':
                    final_sum += product
                    product = 1
                # Update the sign for the next operation
                if(len(signs)>1):
                    signs = signs[1:]
                    sign = signs[0]

            # If the sign is '+', add the number to final sum
            elif sign == '+':
                final_sum += int(number)
            
            # If the sign is '*', multiply the product by the number
            elif sign == '*':
                product *= int(number)

            # Reset
            number = ''

        # Print the final sum
        print(final_sum)  