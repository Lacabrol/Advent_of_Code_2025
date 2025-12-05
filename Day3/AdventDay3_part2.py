if (__name__ == '__main__'):
    # Open the input file "input.txt" in read mode
    with open("input3.txt", "r") as f:

        lines = f.readlines()  # Read all lines from the file into a list

        # Initialize variables
        voltage_sum = 0  
        voltage = []  
        to_remove = 0 
        stack = []  

        for line in lines:
            min_value = 1
            voltage =[int(x) for x in line.strip()]

            # Determine how many digits need to be removed
            to_remove = len(voltage) - 12  
            stack = []

            for num in voltage:

                # Remove smaller digits to maximize the number
                while len(stack) > 0 and to_remove > 0 and stack[-1] < num:
                    stack.pop()
                    to_remove -= 1
                stack.append(num)

            # Remove remaining digits if needed
            while to_remove > 0:
                stack.pop()
                to_remove -= 1
            # Calculate the voltage from the remaining digits
            voltage_sum += int(''.join(map(str, stack)))
                
        print(voltage_sum)  # Print the total voltage sum