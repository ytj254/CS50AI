import itertools
import random


class Minesweeper():
    """
    Minesweeper game representation
    """

    def __init__(self, height=8, width=8, mines=8):

        # Set initial width, height, and number of mines
        self.height = height
        self.width = width
        self.mines = set()

        # Initialize an empty field with no mines
        self.board = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(False)
            self.board.append(row)

        # Add mines randomly
        while len(self.mines) != mines:
            i = random.randrange(height)
            j = random.randrange(width)
            if not self.board[i][j]:
                self.mines.add((i, j))
                self.board[i][j] = True

        # At first, player has found no mines
        self.mines_found = set()

    def print(self):
        """
        Prints a text-based representation
        of where mines are located.
        """
        for i in range(self.height):
            print("--" * self.width + "-")
            for j in range(self.width):
                if self.board[i][j]:
                    print("|X", end="")
                else:
                    print("| ", end="")
            print("|")
        print("--" * self.width + "-")

    def is_mine(self, cell):
        i, j = cell
        return self.board[i][j]

    def nearby_mines(self, cell):
        """
        Returns the number of mines that are
        within one row and column of a given cell,
        not including the cell itself.
        """

        # Keep count of nearby mines
        count = 0

        # Loop over all cells within one row and column
        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):

                # Ignore the cell itself
                if (i, j) == cell:
                    continue

                # Update count if cell in bounds and is mine
                if 0 <= i < self.height and 0 <= j < self.width:
                    if self.board[i][j]:
                        count += 1

        return count

    def won(self):
        """
        Checks if all mines have been flagged.
        """
        return self.mines_found == self.mines


class Sentence():
    """
    Logical statement about a Minesweeper game
    A sentence consists of a set of board cells,
    and a count of the number of those cells which are mines.
    """

    def __init__(self, cells, count):
        self.cells = set(cells)
        self.count = count

    def __eq__(self, other):
        return self.cells == other.cells and self.count == other.count

    def __str__(self):
        return f"{self.cells} = {self.count}"

    def known_mines(self):
        """
        Returns the set of all cells in self.cells known to be mines.
        """

        # If number of cells = count, all the cells are mines
        if len(self.cells) == self.count:
            return self.cells
        return set()

    def known_safes(self):
        """
        Returns the set of all cells in self.cells known to be safe.
        """

        # If count = 0, all the cells are safe
        if self.count == 0:
            return self.cells
        return set()

    def mark_mine(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be a mine.
        """

        # Check if the cell in cells
        if cell in self.cells:

            # Update the sentence
            self.cells.remove(cell)
            self.count -= 1

    def mark_safe(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be safe.
        """

        # Check if the cell in cells
        if cell in self.cells:

            # Update the sentence
            self.cells.remove(cell)


class MinesweeperAI():
    """
    Minesweeper game player
    """

    def __init__(self, height=8, width=8):

        # Set initial height and width
        self.height = height
        self.width = width

        # Keep track of which cells have been clicked on
        self.moves_made = set()

        # Keep track of cells known to be safe or mines
        self.mines = set()
        self.safes = set()

        # List of sentences about the game known to be true
        self.knowledge = []
        # print('knowledge base', self.knowledge)

    def mark_mine(self, cell):
        """
        Marks a cell as a mine, and updates all knowledge
        to mark that cell as a mine as well.
        """
        self.mines.add(cell)
        for sentence in self.knowledge:
            print('4', sentence)
            sentence.mark_mine(cell)
            print('5', sentence)
        # print(self.knowledge)

    def mark_safe(self, cell):
        """
        Marks a cell as safe, and updates all knowledge
        to mark that cell as safe as well.
        """
        self.safes.add(cell)
        for sentence in self.knowledge:
            print('2', sentence)
            sentence.mark_safe(cell)
            print('3', sentence)
        # print(self.knowledge)

    def add_knowledge(self, cell, count):
        """
        Called when the Minesweeper board tells us, for a given
        safe cell, how many neighboring cells have mines in them.

        This function should:
            1) mark the cell as a move that has been made
            2) mark the cell as safe
            3) add a new sentence to the AI's knowledge base
               based on the value of `cell` and `count`
            4) mark any additional cells as safe or as mines
               if it can be concluded based on the AI's knowledge base
            5) add any new sentences to the AI's knowledge base
               if they can be inferred from existing knowledge
        """

        # Mark the cell as moved
        self.moves_made.add(cell)

        # Mark the cell as safe and update knowledge base
        self.safes.add(cell)
        for sentence in self.knowledge:
            sentence.mark_safe(cell)

        # Indentify nearby cells other than the given cell itself
        cells = set()
        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):

                # Ignore the cell is identified as safe or mine
                if (i, j) in self.safes:
                    continue

                # Ignore the cell is identified as mine and count - 1
                if (i, j) in self.mines:
                    count -= 1
                    continue

                # Add cells within bounds
                if 0 <= i < self.height and 0 <= j < self.width:
                    cells.add((i, j))

        s = Sentence(cells, count)
        print('1', s)
        # Add the new sentence to the AI's knowledge base
        # print(s.known_safes())
        self.knowledge.append(s)

        # Inference
        for sentence in self.knowledge:
            # print('old', sentence)
            # print('new', s)
            if s.cells > sentence.cells:
                new_sentence = Sentence((s.cells - sentence.cells), (s.count - sentence.count))
                if new_sentence not in self.knowledge:
                    self.knowledge.append(new_sentence)
                    # print('new knowledge', new_sentence)
            if sentence.cells > s.cells:
                new_sentence = Sentence((sentence.cells - s.cells), (sentence.count - s.count))
                if new_sentence not in self.knowledge:
                    self.knowledge.append(new_sentence)
                    # print('new knowledge', new_sentence)

        # Mark additional cells as safe or as mines
        for sentence in self.knowledge:
            # print(sentence)
            if sentence.known_safes():
                # print('sentence.known_safes:', sentence.known_safes())
                self.safes = self.safes.union(sentence.known_safes())
                self.knowledge.remove(sentence)
                # print('known safe:', self.safes)
            if sentence.known_mines():
                # print('sentence.known_mines:', sentence.known_mines())
                self.mines = self.mines.union(sentence.known_mines())
                self.knowledge.remove(sentence)
                # print('known mine:', self.mines)

        print('known safe:', self.safes)
        print('known mine:', self.mines)
        print('known move:', self.moves_made)
        # for sentence in self.knowledge:
        #     print('knowledge base', sentence)

    def make_safe_move(self):
        """
        Returns a safe cell to choose on the Minesweeper board.
        The move must be known to be safe, and not already a move
        that has been made.

        This function may use the knowledge in self.mines, self.safes
        and self.moves_made, but should not modify any of those values.
        """
        try:
            return random.choice(list(self.safes - self.moves_made))
        except IndexError:
            return None

    def make_random_move(self):
        """
        Returns a move to make on the Minesweeper board.
        Should choose randomly among cells that:
            1) have not already been chosen, and
            2) are not known to be mines
        """
        # Initialize a set of cells in the board
        board = set()
        for i in range(self.height):
            for j in range(self.width):
                board.add((i, j))
        try:
            return random.choice(list(board - self.moves_made - self.mines))
        except IndexError:
            return None


def main():
    cells = {(0, 0), (0, 1), (0, 2),
             (1, 0), (1, 1), (1, 2),
             (2, 0), (2, 1), (2, 2),
             }
    count = 8
    s = Sentence(cells, count)
    # print(s)
    # print('mine', s.known_mines())
    # print('safe', s.known_safes())
    # print(s.mark_mine((0, 0)))
    # print('mark mine', s)
    # print(s.mark_safe((0, 0)))
    # print('mark safe', s)
    # print('mine', s.known_mines())
    # print('safe', s.known_safes())
    ai = MinesweeperAI()
    ai.add_knowledge((2, 1), 2)
    ai.add_knowledge((0, 1), 2)
    ai.add_knowledge((0, 0), 2)
    print(ai.make_safe_move())
    print(ai.make_random_move())
    # ai.mark_safe((0, 0))
    # ai.mark_mine((1, 1))
    # print(ai.knowledge)


if __name__ == '__main__':
    main()