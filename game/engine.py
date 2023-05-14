from random import randint
from os import system
from rich.console import Console
from rich.text import Text

console = Console()

class Game:
    def __init__(self, one_player: bool = True) -> None:
        self.one_player = one_player
        self.table = [["#" for _ in range(3)] for _ in range(3)]
        self.winner = False

    def verify_winner(self, data: list):
        if data.count("X") == 3:
            self.winner = "X"
            return True
        elif data.count("O") == 3:
            self.winner = "O"
            return True
        else:
            return False

    def verify_vertical(self):
        for x in range(3):
            data = [self.table[y][x] for y in range(3)]
            if self.verify_winner(data):
                break

    def verify_horizontal(self):
        for y in range(3):
            data = self.table[y]
            if self.verify_winner(data):
                break

    def verify_diagonal(self):
        # Left to Right
        data = [self.table[y][y] for y in range(3)]
        self.verify_winner(data)
        # Right to Left
        data = [self.table[y][-1-y] for y in range(3)]
        self.verify_winner(data)
    
    def set_position(self, x: int, y: int, char: str):
        if self.table[y][x] == "#":
            self.table[y][x] = char
            return True
        return False

    def render_table(self):
        system("cls")
        print("    1   2   3")
        for y in range(3):
            text = Text()
            text.append(f"{y+1} | ")
            for x in self.table[y]:
                if x == "X":
                    color = "blue"
                elif x == "O":
                    color = "red"
                else:
                    x = " "
                    color = "yellow"
                text.append(x, style="bold "+color)
                text.append(" | ")
            console.print(text)
    
    def get_input(self, char: str):
        correct = False
        while not correct:
            x, y = [int(n)-1 for n in input(f"\n{char} > ").split()]
            correct = self.set_position(x, y, char)

    def start(self):
        self.render_table()
        char = ["X", "O"][randint(0, 1)]
        while not self.winner:
            self.get_input(char)
            self.render_table()
            self.verify_vertical()
            self.verify_horizontal()
            self.verify_diagonal()
            char = "X" if char == "O" else "O"
            if sum([line.count("#") for line in self.table]) <= 1:
                break
        if self.winner:
            print(f"O Vencedor foi o {self.winner} !")
        else:
            print("O jogo deu Velha")

    def reset_game(self):
        self.table = [["#" for _ in range(3)] for _ in range(3)]
        self.winner = False