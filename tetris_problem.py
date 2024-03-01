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

    def new_row(self):
        return [0 for _ in range(10)]

    def does_figure_fit(self, row, figure_name, pos):
        piece = self.figures.get(figure_name)
        #iterate through figure row to determine if fits on board
        for i in range(len(piece)):
            figure_row = piece[-1 * (1 + i)]
            #check if current row is last row on board
            if i + row == len(self.board):
                return True
            board_row = self.board[i + row]
            for j in range(len(figure_row)):
                if figure_row[j] and board_row[pos + j]:
                    return False
        return True

    def remove_completed_rows(self, start_row, num_rows):
        # removes full rows from the board
        # only checks rows between start_row and start_row+numRows
        full_rows = [i + start_row
                    for i in range(num_rows)
                    if all(self.board[i + start_row])]
        for completed_row in sorted(full_rows, reverse=True):
            del self.board[completed_row]

    def add_figure_at(self, row, figure_name, pos):
        piece = self.figures.get(figure_name)
        for i in range(len(piece)):
            piece_row = piece[-1 * (1 + i)]

            if i + row == len(self.board):
                self.board += self.new_row(),
            board_row = self.board[i + row]
            for j in range(len(piece_row)):
                if piece_row[j]:
                    board_row[pos + j] = piece_row[j]
        self.remove_completed_rows(row, len(piece))

    def add_figure(self, figure_name, pos):

        blocked_by_row = None
        for row in range(len(self.board) - 1, -1, -1):
            if not self.does_figure_fit(row, figure_name, pos):
                blocked_by_row = row
                break

        target_row = 0 if blocked_by_row == None else blocked_by_row + 1
        self.add_figure_at(target_row, figure_name, pos)

    def add_figures(self, figures: list):
        #parse input row to get figures
        for piece in figures.split(','):
            self.add_figure(piece[0], int(piece[1]))
        return len(self.board)

    @property
    def view_board(self):
        for line in enumerate(self.board[::-1]):
            print(line)


if __name__ == '__main__':
    import fileinput

    t = Tetris()
    args = sys.argv[1:][0]
    # Take input from stin, should be a file name
    with open(args) as f:
        lines = f.readlines()
    for input_row in lines:
        print(t.add_figures(input_row))

