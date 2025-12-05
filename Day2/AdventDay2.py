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
                if (str(i)[:len(str(i))//2] == str(i)[len(str(i))//2:]):
                    final_sum += i

        print(final_sum)  # Print the final sum

