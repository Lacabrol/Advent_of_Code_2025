if __name__ == '__main__':
    # Open the input file "input.txt" in read mode
    with open("input5.txt", "r") as f:

        lines = f.readlines() # Read all lines from the file into a list

        # Initialize variables
        rules, new_rules = []
        final_sum = 0
        merged = False

        # Process each line in the input file
        for line in lines:
            # Split the line by '-' and process
            line = line.strip().split('-')
            # Check if the length of line is 2
            if len(line) == 2:
                # Parse start and end of the interval
                start, end = int(line[0]), int(line[1])
                # Reset new_rules for merging
                new_rules = []
                # Try to merge with existing rules
                for rule in rules:
                    # If no overlap, keep the rule
                    if end < rule[0] - 1 or start > rule[1] + 1:
                        new_rules.append(rule)

                    # If overlap, merge intervals
                    else:
                        start = min(start, rule[0])
                        end = max(end, rule[1])
                        merged = True

                # If merged, add the new merged interval
                new_rules.append([start, end])
                rules = sorted(new_rules)
                merged = False

            else:
                break

        # Calculate the total count of numbers covered by the merged rules
        for rule in rules:
            final_sum += rule[1] - rule[0] + 1

        print(final_sum)
