if (__name__ == '__main__'):
    # Open the input file "input.txt" in read mode
    with open("input3.txt", "r") as f:

        lines = f.readlines()  # Read all lines from the file into a list

        # Initialize variables
        voltage_sum = 0  
        voltage = 0  

        for line in lines:
            line =line.strip()
            
            # Find the maximum two-digit number from the line
            for i in range(len(line)-1):
                for j in range(i+1, len(line)):
                    if int(line[i]+line[j])>voltage:
                        voltage = int(line[i]+line[j])

            # Add the voltage from this line to the total sum
            voltage_sum += voltage
            # Reset voltage for the next line
            voltage = 0  

        # Print the total voltage sum
        print(voltage_sum)  