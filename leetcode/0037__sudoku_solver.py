"""
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

1. Each of the digits 1-9 must occur exactly once in each row.
2. Each of the digits 1-9 must occur exactly once in each column.
3. Each of the digits 1-9 must occur exactly once in each of the 9 3x3
   sub-boxes of the grid.

The '.' character indicates empty cells.

Approach: Use sets to model the possible values in each cell.

Initialize already-filled-in cells as sets of single values.

Initialize blank cells as the set difference of all values minus the union of
the row values, column values, and box values.

>>> s = Solution()
>>> board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
>>> s.solveSudoku(board)
>>> print(board)
[['5', '3', '4', '6', '7', '8', '9', '1', '2'], ['6', '7', '2', '1', '9', '5', '3', '4', '8'], ['1', '9', '8', '3', '4', '2', '5', '6', '7'], ['8', '5', '9', '7', '6', '1', '4', '2', '3'], ['4', '2', '6', '8', '5', '3', '7', '9', '1'], ['7', '1', '3', '9', '2', '4', '8', '5', '6'], ['9', '6', '1', '5', '3', '7', '2', '8', '4'], ['2', '8', '7', '4', '1', '9', '6', '3', '5'], ['3', '4', '5', '2', '8', '6', '1', '7', '9']]
"""
ALL_VALUES = { "1", "2", "3", "4", "5", "6", "7", "8", "9" }
class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        self.solveSudoku1(board)

    def solveSudoku1(self, board: list[list[str]]) -> None:
        workingBoard = self.generateWorkingBoard(board)

        hasAtLeastOneUnsolvedCell = True
        while hasAtLeastOneUnsolvedCell:
            hasAtLeastOneUnsolvedCell = False
            for x in range(9):
                for y in range(9):
                    if len(workingBoard[y][x]) > 1:
                        otherValues = self.getRowValuesSet(workingBoard, x, y) | \
                        self.getColumnValuesSet(workingBoard, x, y) | \
                        self.getSquareValuesSet(workingBoard, x, y)
                        workingBoard[y][x] = workingBoard[y][x] - otherValues
                        if len(workingBoard[y][x]) > 1:
                            hasAtLeastOneUnsolvedCell = True
        self.populateSolutionBoard(workingBoard, board)

    def generateWorkingBoard(self, board: list[list[str]]) -> \
        list[list[set[str]]]:
        workingBoard = [[set() for x in range(9)] for y in range(9)]

        # populate all given squares with sets of single elements
        for x in range(9):
            for y in range(9):
                if board[y][x] in ALL_VALUES:
                    workingBoard[y][x].add(board[y][x])

        # populate all empty squares with sets consisting of
        # the set difference of all values minus the row, column, and square

        for x in range(9):
            for y in range(9):
                if board[y][x] == '.':
                    otherValues = self.getRowValuesSet(workingBoard, x, y) | \
                        self.getColumnValuesSet(workingBoard, x, y) | \
                        self.getSquareValuesSet(workingBoard, x, y)
                    workingBoard[y][x] = ALL_VALUES - otherValues
        return workingBoard

    def getRowValuesSet(self, workingBoard: list[list[set[str]]], cellX: int, cellY: int) -> set[str]:
        values = set()
        for x in range(9):
            if x == cellX:
                continue
            elif len(workingBoard[cellY][x]) == 1:
               values.update(workingBoard[cellY][x])
        return values

    def getColumnValuesSet(self, workingBoard: list[list[set[str]]], cellX: int, cellY: int) -> set[str]:
        values = set()
        for y in range(9):
            if y == cellY:
                continue
            elif len(workingBoard[y][cellX]) == 1:
                values.update(workingBoard[y][cellX])
        return values

    def getSquareValuesSet(self, workingBoard: list[list[set[str]]], cellX: int, cellY: int) -> set[str]:
        xStart = 0
        xEnd = 0
        yStart = 0
        yEnd = 0
        if cellX < 3:
            xStart = 0
            xEnd = 3
        elif cellX < 6:
            xStart = 3
            xEnd = 6
        else:
            xStart = 6
            xEnd = 9

        if cellY < 3:
            yStart = 0
            yEnd = 3
        elif cellY < 6:
            yStart = 3
            yEnd = 6
        else:
            yStart = 6
            yEnd = 9

        values = set()
        for x in range(xStart, xEnd):
            for y  in range(yStart, yEnd):
                if x == cellX and y == cellY:
                    continue
                elif len(workingBoard[y][x]) == 1:
                    values.update(workingBoard[y][x])
        return values

    def populateSolutionBoard(self, workingBoard: list[list[set[str]]],
                              board: list[list[str]]) -> None:
        for x in range(9):
            for y in range(9):
                board[y][x] = workingBoard[y][x].pop()

if __name__ == '__main__':
    import doctest
    doctest.testmod()
