import sys


class Tetris:
    def __init__(self):
        self.board = []
        self.figures = {
            'I': [[1, 1, 1, 1]],

            'Q': [[1, 1],
                  [1, 1]],

            'T': [[1, 1, 1],
                  [0, 1, 0]],

            'Z': [[1, 1, 0],
                  [0, 1, 1]],

            'S': [[0, 1, 1],
                  [1, 1, 0]],

            'L': [[1, 0],
                  [1, 0],
                  [1, 1]],

            'J': [[0, 1],
                  [0, 1],
                  [1, 1]]}

    def newRow(self):
        return [0 for _ in range(10)]

    def does_figure_fit(self, row, figure_name, pos):
        # checks to see if a piece fits on the row at given position
        # check bottom to the top
        piece = self.figures[figure_name]
        for i in range(len(piece)):
            figure_row = piece[-1 * (1 + i)]
            if i + row == len(self.board):
                return True
            boardRow = self.board[i + row]
            for j in range(len(figure_row)):
                if figure_row[j] and boardRow[pos + j]:
                    return False
        return True

    def remove_completed_rows(self, startRow, numRows):
        # removes full rows from the board
        # only checks rows between startRow and startRow+numRows
        fullRows = [i + startRow
                    for i in range(numRows)
                    if all(self.board[i + startRow])]
        for fullRow in sorted(fullRows, reverse=True):
            del self.board[fullRow]

    def add_figure_at(self, row, figure_name, pos):
        # Adds piece at this row.
        piece = self.figures[figure_name]
        for i in range(len(piece)):
            pieceRow = piece[-1 * (1 + i)]

            if i + row == len(self.board):
                self.board += self.newRow(),
            boardRow = self.board[i + row]
            for j in range(len(pieceRow)):
                if pieceRow[j]:
                    boardRow[pos + j] = pieceRow[j]
        self.remove_completed_rows(row, len(piece))

    def add_figure(self, figure_name, pos):
        # 1.find the first row where piece is blocked
        # 2.Add the piece at the row above it
        blockedByRow = None
        for row in range(len(self.board) - 1, -1, -1):
            if not self.does_figure_fit(row, figure_name, pos):
                blockedByRow = row
                break

        targetRow = 0 if blockedByRow == None else blockedByRow + 1
        self.add_figure_at(targetRow, figure_name, pos)

    def add_figures(self, figures: list):
        for piece in figures.split(','):
            self.add_figure(piece[0], int(piece[1]))
        return len(self.board)


if __name__ == '__main__':
    import fileinput

    t = Tetris()
    args = sys.argv[1:]
    for input_row in fileinput.input(args):
        print(t.add_figures(input_row))
