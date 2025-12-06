if (__name__ == '__main__'):
    # Open the input file "input.txt" in read mode
    with open("input5.txt", "r") as f:

        lines = f.readlines()  # Read all lines from the file into a list
        # Initialize variables
        final_sum = 0
        rules = []

        # Process each line in the input file
        for line in lines:
            # Split the line by '-' and process
            line = line.strip().split('-')
            # Check if the first part is not empty
            if(line[0] != '' ):
                # If there are two parts, it's a rule; otherwise, it's a number to check
                if len(line) == 2:
                    rules.append((int(line[0]), int(line[1])))
                else:
                    # Check if the number falls within any of the rules
                    for rule in rules:
                        # If the number is within the rule range, increment final sum
                        if rule[0] <= int(line[0]) <= rule[1]:
                            final_sum += 1
                            break
                        
        print(final_sum)  # Print the final sum
