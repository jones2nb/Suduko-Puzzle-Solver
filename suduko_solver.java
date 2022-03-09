public class syduko_solver{

    static int [][] puzzle = {
        {0, 9, 6, 0, 0, 0, 0, 3, 0},
        {0, 0, 8, 0, 0, 0, 0, 0, 0},
        {0, 5, 0, 2, 0, 4, 0, 9, 0},
        {0, 0, 1, 6, 7, 2, 0, 0, 0},
        {8, 0, 0, 0, 0, 0, 3, 0, 0},
        {0, 0, 9, 0, 0, 0, 0, 0, 0},
        {0, 0, 2, 0, 1, 0, 8, 0, 0},
        {0, 0, 0, 0, 0, 0, 0, 0, 4},
        {0, 0, 0, 0, 0, 8, 1, 6, 5}
    };
    public static void main(String[] args){
        solve_puzzle(puzzle, 0, 0);
        for(int[]r : puzzle){
            for(int c : r){
                System.out.print(c + "  ");
            }
            System.out.println();
        }
    }

    static boolean solve_puzzle(int [][] puz, int row, int col){

        while(puz[row][col] != 0){
            if(col < 8){
                col++;
            } else {
                if(row == 8){
                    return true;
                }
                col = 0;
                row++;  
            }
        }
        for(int i = 1; i < 10; i++){
            if(is_Valid(puz, row, col, i)){
                puz[row][col] = i;
                if(solve_puzzle(puz, row, col)){
                    return true;
                }
                puz[row][col] = 0;
            }
        }

        if(puz[row][col] == 0){
            return false; 
        }

        return true;
    }

    static boolean is_Valid(int [][] puz, int row, int col, int num){
        //check above and below for the same number
        for(int c: puz[row]){
            if(c == num){
                return false;
            }
        }
        //check left and right for the same number
        for(int[] r: puz){
            if(r[col] == num){
                return false;
            }
        }
        //check in the box for the same number
        if(row < 3){
            if(col < 3){
                for(int r = 0; r < 3; r++){
                    for(int c = 0; c < 3; c++){
                        if(puz[r][c] == num){
                            return false;
                        }
                    }
                }
            } else if(col < 6){
                for(int r = 0; r < 3; r++){
                    for(int c = 3; c < 6; c++){
                        if(puz[r][c] == num){
                            return false;
                        }
                    }
                }
            } else {
                for(int r = 0; r < 3; r++){
                    for(int c = 6; c < 9; c++){
                        if(puz[r][c] == num){
                            return false;
                        }
                    }
                }
            }
        } else if(row < 6){
            if(col < 3){
                for(int r = 3; r < 6; r++){
                    for(int c = 0; c < 3; c++){
                        if(puz[r][c] == num){
                            return false;
                        }
                    }
                }
            } else if(col < 6){
                for(int r = 3; r < 6; r++){
                    for(int c = 3; c < 6; c++){
                        if(puz[r][c] == num){
                            return false;
                        }
                    }
                }
            } else {
                for(int r = 3; r < 6; r++){
                    for(int c = 6; c < 9; c++){
                        if(puz[r][c] == num){
                            return false;
                        }
                    }
                }
            }
        } else {
            if(col < 3){
                for(int r = 6; r < 9; r++){
                    for(int c = 0; c < 3; c++){
                        if(puz[r][c] == num){
                            return false;
                        }
                    }
                }
            } else if(col < 6){
                for(int r = 6; r < 9; r++){
                    for(int c = 3; c < 6; c++){
                        if(puz[r][c] == num){
                            return false;
                        }
                    }
                }
            } else {
                for(int r = 6; r < 9; r++){
                    for(int c = 6; c < 9; c++){
                        if(puz[r][c] == num){
                            return false;
                        }
                    }
                }
            }
        }
        return true;
    }
}