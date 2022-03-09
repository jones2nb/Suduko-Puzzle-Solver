
"""
    Name: Nicholas Jones
    This is a back tracking algorithm to solve any solvable sudoku puzzle.    
"""

# is_Valid will check the row and column to make sure there isn't any conflicting
# numbers it will also check the 3x3 box that the current square is in to make sure
# there aren't any conflicts. 
def is_Valid(puz, row, col, num):
    for c in range(0, 9):
        if(puz[row][c] == num):
            return False

    for r in puz:
        if(r[col] == num):
            return False

    if(row < 3):
        if(col < 3):
            for r in range(0, 3):
                for c in range(0, 3):
                    if(puz[r][c] == num):
                        return False
        elif(col < 6):
            for r in range(0, 3):
                for c in range(3, 6):
                    if(puz[r][c] == num):
                        return False
        else:
            for r in range(0, 3):
                for c in range(6, 9):
                    if(puz[r][c] == num):
                        return False
    elif(row < 6):
        if(col < 3):
            for r in range(3, 6):
                for c in range(0, 3):
                    if(puz[r][c] == num):
                        return False
        elif(col < 6):
            for r in range(3, 6):
                for c in range(3, 6):
                    if(puz[r][c] == num):
                        return False
        else:
            for r in range(3, 6):
                for c in range(6, 9):
                    if(puz[r][c] == num):
                        return False
    else:
        if(col < 3):
            for r in range(6, 9):
                for c in range(0, 3):
                    if(puz[r][c] == num):
                        return False
        elif(col < 6):
            for r in range(6, 9):
                for c in range(3, 6):
                    if(puz[r][c] == num):
                        return False
        else:
            for r in range(6, 9):
                for c in range(6, 9):
                    if(puz[r][c] == num):
                        return False
    
    return True


def solve_puzzle(puz, row, col):
    # if the current square isn't empty that means it was predetermined and it
    # cannot be changed so we will advance to the next square.
    while(puz[row][col] != 0):
        if(col < 8):
            col += 1
        else:
            if(row == 8):
                return True
            col = 0
            row += 1

    # check every number 1 through 9 starting at 1 and if it is valid put that
    # number into the current square and recursivly check the rest of the puzzle.
    # if the rest of the puzzle can be solved the number will stay in the square
    # otherwise it is replaced with zero and we continue checking the range 1-9.
    for i in range(1, 10):
        if(is_Valid(puz, row, col, i)):
            puz[row][col] = i
            if(solve_puzzle(puz, row, col)):
                return True
            puz[row][col] = 0

    if(puz[row][col] == 0):
        return False

    return True


def main():
    solve_puzzle(puzzle, 0, 0)

    for row in range(0, 9):
        for col in range(0, 9):
            print(puzzle[row][col], end=" ")
        print()


puzzle = [
    [0, 9, 6, 0, 0, 0, 0, 3, 0],
    [0, 0, 8, 0, 0, 0, 0, 0, 0],
    [0, 5, 0, 2, 0, 4, 0, 9, 0],
    [0, 0, 1, 6, 7, 2, 0, 0, 0],
    [8, 0, 0, 0, 0, 0, 3, 0, 0],
    [0, 0, 9, 0, 0, 0, 0, 0, 0],
    [0, 0, 2, 0, 1, 0, 8, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 4],
    [0, 0, 0, 0, 0, 8, 1, 6, 5]
]

if __name__ == "__main__":
    main()
