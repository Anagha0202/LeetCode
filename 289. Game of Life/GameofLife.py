class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        """
        Infinite board:
        infinite board can be imagined as a graph with row,col as x,y co-ordinates and it has a active part of the board of size rows,cols
        Since it is infinite, rows-cols i.e edges not known so cannot begin traversing from any corner. 
        We were finding the live_count of a cell using the surrouding cells. 
        Now using this cell, we'll update the count of surrounding cells by 1, implying that the neighbour cell has 1 adjoining cell that is alive. 
        Using these counts, if a cell was dead and count==3 => live
        if cell was alive and count<2 or >3 =>dead

        t: O(no of alives initially)
        s: O(no of alives)
        """
        def get_all_alive(rows, cols):
            alive = set()
            for row in range(rows):
                for col in range(cols):
                    if board[row][col] == 1:
                        alive.add((row,col))
            return alive
        
        def update_live_counts(row, col, live_counts):
            #count all 8 directions and itself also
            directions = [(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,0)]
            for dr_row, dr_col in directions:
                new_row, new_col = row+dr_row, col+dr_col
                live_counts[(new_row,new_col)] += 1


        rows, cols = len(board), len(board[0])
        live_counts = collections.defaultdict(int)
        alive = get_all_alive(rows, cols)

        for row,col in alive:
            update_live_counts(row, col, live_counts)
        
        for cell, count in live_counts.items():
            row, col = cell[0], cell[1]
            if row in range(rows) and col in range(cols):
                if board[row][col]==0 and count==3:
                    board[row][col] = 1
                if (count<3 or count>4): # since itself is also considered as one count
                    board[row][col] = 0
        

        """
        1 - live, 0- dead
        8 directions 
        rules:
        1 -> live_count<2 => 0
        1 -> live_count=2or3  => same 1
        1 -> live_count>3 => 0
        0 -> live_count==3 => 1

        transformations:
        1->0 => 2
        1->1
        0->0
        0->1 => 3

        since we need to alter in place, cannot update the state of each cell and then compute the state of next cell.
        alter into intermediate value, replace intermediate value after all transformations

        t: O(n^2)
        s: O(1)
        """
        def get_live_count(row, col, board):
            directions = [(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]
            live_count = 0
            for dr_row, dr_col in directions:
                new_row, new_col = row+dr_row, col+dr_col
                if (new_row in range(rows) and 
                    new_col in range(cols) and
                    (board[new_row][new_col] == 1 or board[new_row][new_col] == 2)): #if it is alive or was alive then count it
                    live_count+=1
            return live_count

        rows, cols = len(board), len(board[0])
        for row in range(rows):
            for col in range(cols):
                live_count = get_live_count(row, col, board)
                if  board[row][col]==1 and (live_count<2 or live_count>3):
                    board[row][col] = 2
                elif live_count==3 and board[row][col]==0:
                    board[row][col] = 3   
        
        for row in range(rows):
            for col in range(cols):
                if board[row][col]==3:
                    board[row][col] = 1
                elif board[row][col] == 2:
                    board[row][col] = 0
        