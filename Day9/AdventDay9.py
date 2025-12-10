

if __name__ == '__main__':
    with open("input9.txt") as f:
         # Open the input file "input.txt" in read mode
        lines = f.readlines()  # Read all lines from the file into a list
        red_tiles = [(int(line.split(',')[0]), int(line.split(',')[1])) for line in lines]
        largest_area = 0


        for i in range(len(red_tiles)):
            x1, y1 = red_tiles[i]
            for j in range(len(red_tiles)):
                
                x2, y2 = red_tiles[j]
                
                largest_area = max((abs(x2 - x1)+1) * (abs(y2 - y1)+1), largest_area)

        print(largest_area)
