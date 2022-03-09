
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
    while(puz[row][col] != 0):
        if(col < 8):
            col += 1
        else:
            if(row == 8):
                return True
            col = 0
            row += 1

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
    print("Python")
    main()
