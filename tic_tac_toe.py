import tkinter as tk
from typing import Optional, List, Tuple, Dict
from functools import lru_cache

class TicTacToe:
    def __init__(self):
        self.size = 4
        self.board: List[List[Optional[str]]] = [[None] * self.size for _ in range(self.size)]
        self.cache: Dict[Tuple[Tuple[Optional[str], ...], str], int] = {}

    def is_losing_move(self, player: str, r: int, c: int) -> bool:
        self.board[r][c] = player
        lines = []
        n = self.size
        for i in range(n):
            lines.append(self.board[i])
            lines.append([self.board[r][i] for r in range(n)])
        lines.append([self.board[i][i] for i in range(n)])
        lines.append([self.board[i][n-1-i] for i in range(n)])
        lose = False
        for line in lines:
            for i in range(n-3):
                if all(cell is not None for cell in line[i:i+4]):
                    lose = True
                    break
            if lose:
                break
        self.board[r][c] = None
        return lose

    def get_possible_moves(self) -> List[Tuple[int, int]]:
        return [(r, c) for r in range(self.size) for c in range(self.size) if self.board[r][c] is None]

    def board_key(self) -> Tuple[Tuple[Optional[str], ...], ...]:
        return tuple(tuple(row) for row in self.board)

    def minimax(self, player: str, maximizing: bool, alpha: int = -2, beta: int = 2) -> int:
        key = (self.board_key(), player)
        if key in self.cache:
            return self.cache[key]

        moves = self.get_possible_moves()
        if not moves:
            return 0

        opponent = 'player' if player == 'ai' else 'ai'

        if maximizing:
            best = -2
            for r, c in moves:
                if self.is_losing_move(player, r, c):
                    continue
                self.board[r][c] = player
                score = self.minimax(opponent, False, alpha, beta)
                self.board[r][c] = None
                best = max(best, score)
                alpha = max(alpha, best)
                if beta <= alpha:
                    break
                if best == 1:
                    break
            if best == -2:
                best = -1
        else:
            best = 2
            for r, c in moves:
                if self.is_losing_move(player, r, c):
                    continue
                self.board[r][c] = player
                score = self.minimax(opponent, True, alpha, beta)
                self.board[r][c] = None
                best = min(best, score)
                beta = min(beta, best)
                if beta <= alpha:
                    break
                if best == -1:
                    break
            if best == 2:
                best = 1

        self.cache[key] = best
        return best

    def select_move(self, player: str) -> Optional[Tuple[int, int]]:
        best_score = -2
        best_move = None
        opponent = 'player' if player == 'ai' else 'ai'

        for r, c in self.get_possible_moves():
            if self.is_losing_move(player, r, c):
                continue
            self.board[r][c] = player
            score = self.minimax(opponent, False)
            self.board[r][c] = None
            if score > best_score:
                best_score = score
                best_move = (r, c)
            if best_score == 1:
                break

        if best_move is None:
            return self.get_possible_moves()[0]

        return best_move


class TicTacToeUI:
    def __init__(self, root):
        self.game = TicTacToe()
        self.root = root
        self.root.title("Tic Tac Toe 4x4 Misère")
        self.buttons = [[None]*self.game.size for _ in range(self.game.size)]
        self.create_ui()

    def create_ui(self):
        for r in range(self.game.size):
            for c in range(self.game.size):
                btn = tk.Button(self.root, text="", width=6, height=3,
                                font=('Helvetica', 20), command=lambda r=r, c=c: self.on_click(r, c))
                btn.grid(row=r, column=c)
                self.buttons[r][c] = btn

    def on_click(self, r, c):
        if self.game.board[r][c] or not self.game.get_possible_moves():
            return
        if self.game.is_losing_move('player', r, c):
            self.end_game('Przegrywa: Gracz')
            self.game.board[r][c] = 'player'
            self.update_ui()
            return
        self.game.board[r][c] = 'player'
        self.update_ui()
        self.root.after(100, self.ai_turn)

    def ai_turn(self):
        move = self.game.select_move('ai')
        r, c = move
        if move is None:
            self.end_game('Remis!')
            self.game.board[r][c] = 'ai'
            self.update_ui()
            return

        if self.game.is_losing_move('ai', r, c):
            self.end_game('Przegrywa: AI')
            self.game.board[r][c] = 'ai'
            self.update_ui()
            return
        self.game.board[r][c] = 'ai'
        self.update_ui()

    def update_ui(self):
        for r in range(self.game.size):
            for c in range(self.game.size):
                owner = self.game.board[r][c]
                if owner:
                    self.buttons[r][c]['text'] = 'X'
                    self.buttons[r][c]['fg'] = 'blue' if owner=='player' else 'green'
                else:
                    self.buttons[r][c]['text'] = ''

    def end_game(self, message: str):
        for r in range(self.game.size):
            for c in range(self.game.size):
                self.buttons[r][c]['state'] = 'disabled'
        label = tk.Label(self.root, text=message, font=('Helvetica', 16))
        label.grid(row=self.game.size, column=0, columnspan=self.game.size)

if __name__ == '__main__':
    root = tk.Tk()
    app = TicTacToeUI(root)
    root.mainloop()
