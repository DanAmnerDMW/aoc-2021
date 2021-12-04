from typing import List
import numpy as np


class Board:
    def __init__(self, values) -> None:
        # Create numpy array to represent board
        for i, row in enumerate(values):
            values[i] = [int(x) for x in row]
        self.board = np.array(values)

    def mark_board(self, number):
        # Set to -1 when matched
        self.board[self.board == number] = -1

    def check_board(self) -> bool:
        # Check rows for matches
        for i in range(self.board.shape[0]):
            match = np.all(self.board[i] == -1)

            if match:
                return True

            # Check columns for matches by transposing array
            trans_board = self.board.T
            for i in range(trans_board.shape[0]):
                match = np.all(trans_board[i] == -1)

                if match:
                    return True

        return match


def part1(values):
    values = [x.strip() for x in values]

    draw = [int(x) for x in values[0].split(",")]
    boards = create_boards(values)

    match = False

    for number in draw:
        for board in boards:
            board.mark_board(number)
            match = board.check_board()

            if match:
                # Set all matches as 0, so doesn't affect the sum
                board.board[board.board == -1] = 0
                return np.sum(board.board) * number


def part2(values):

    values = [x.strip() for x in values]

    draw = [int(x) for x in values[0].split(",")]
    boards = create_boards(values)
    matches = []

    for number in draw:
        for board in list(boards):
            board.mark_board(number)
            match = board.check_board()

            if match:
                # Create list of matches, and remove board from checking so no multi-matches
                matches.append({"board": board.board, "number": number})
                boards.remove(board)

    last_board = matches[-1]
    last_board["board"][last_board["board"] == -1] = 0
    return np.sum(last_board["board"]) * last_board["number"]


def create_boards(values: List[str]) -> List[Board]:
    boards = []

    for i in range(2, len(values) - 1, 6):
        raw_board = [x.split() for x in values[i : i + 5]]
        board = Board(raw_board)
        boards.append(board)

    return boards


if __name__ == "__main__":
    input = open("day4/input.txt", "r")
    values = input.readlines()

    print(f"Part 1: {part1(values)}")
    print(f"Part 2: {part2(values)}")
