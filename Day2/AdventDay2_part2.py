if (__name__ == '__main__'):
    # Open the input file "input.txt" in read mode
    with open("input2.txt", "r") as f:

        line = f.readlines()  # Read all lines from the file into a list
        line = line[0].strip().split(',')  # Split the single line into commands

        # Initialize variables
        final_sum = 0  
        start = 0
        end = 0

        for interval in line:
            interval = interval.split('-')
            start = int(interval[0])
            end = int(interval[1])

            for i in range(start, end + 1):
                for divider in range(1, len(str(i))//2 + 1):
                    
                    if len(str(i)) % divider == 0:
                        if all(str(i)[k:divider+k] == str(i)[k+divider:2*divider+k] for k in range(0, len(str(i))-divider, divider)):
                            final_sum += i
                            break

        print(final_sum)  # Print the final sum

