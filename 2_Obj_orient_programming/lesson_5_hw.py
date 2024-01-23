class TicTacToe:
    def __init__(self):
        self.board = [' '] * 9
        self.current_player = 'X'

    def display_board(self):
        for i in range(0, 9, 3):
            print(f"{self.board[i]} | {self.board[i + 1]} | {self.board[i + 2]}")
            if i < 6:
                print("-" * 9)

    def make_move(self, position):
        if self.board[position] == ' ':
            self.board[position] = self.current_player
            return True
        else:
            print("Эта клетка уже занята. Выберите другую.")
            return False

    def check_winner(self):
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                                (0, 3, 6), (1, 4, 7), (2, 5, 8),
                                (0, 4, 8), (2, 4, 6)]

        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] == self.current_player:
                return True

        return False

    def is_board_full(self):
        return ' ' not in self.board

game = TicTacToe()

while True:
    game.display_board()
    position = int(input(f"Ход игрока {game.current_player}. Введите номер клетки (0-8): "))

    if 0 <= position <= 8:
        if game.make_move(position):
            if game.check_winner():
                game.display_board()
                print(f"Игрок {game.current_player} победил!")
                break
            elif game.is_board_full():
                game.display_board()
                print("Ничья!")
                break
            game.current_player = 'O' if game.current_player == 'X' else 'X'
    else:
        print("Введите число от 0 до 8.")
