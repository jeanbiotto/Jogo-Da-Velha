from random import Random
from player import HumanPlayer, RandomComputerPlayer
from time import sleep


class JogoDaVelha:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # Para criar uma tabela de 3x3 
        self.current_winner = None            # Para poder definir um vencedor

    def print_board(self):
        # Isso é para criar as linhas
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('|' + '|'.join(row) + '|')

    print('Voce é o jogador "X" e seu adversário o jogador "O" ')
    print(' ')
    sleep(0.8)
    print('Para jogar basta selecionar o numero do quadrado que deseja! ')
    print(' ')
    sleep(0.8)
    print('Veja o Exemplo abaixo ')
    print(' ')
    sleep(0.8)
    
    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 -> serve para dizer qual numero corresponde a qual caixa
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('|' + '|'.join(row) + '|')

    def available_moves(self):
        return[i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return len(self.available_moves())

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # Vence quem ter tres X ou O em sequencia... mas precisa testar todas as possibilidades
        # Primeiro verificar as linhas
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True
        
        # Checar as colunas
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        # Checar as diagonais
        # Mas apenas se o 'quadrado' ser um numero PAR (0, 2, 4, 6, 8)
        # Essa é a unica maneira de ganhar na diagonal
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]] # Diagonal da esquerda pra direira (De cima para baixo)
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]] # Diagonal da direita pra esquerda (De cima para baixo)
            if all([spot == letter for spot in diagonal2]):
                return True

        # Se isso tudo der errado
        return False


def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()

    letter = 'X'

    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)

        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(' ')
                print('O jogador ' "'" + letter + "'" f' selecionou o quadrado {square}')
                print(' ')
                game.print_board()
                print('')

            if game.current_winner:
                if print_game:
                    print('O jogador ' "'" + letter + "'" ' Venceu!!')
                return letter

            # Depois de fazer a jogada é preciso trocar de letra
            letter = 'O' if letter == 'X' else 'X'

            # Pausa entre as jogadas
            sleep(1)

    if print_game:
        print('Temos um EMPATE!!')


if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    jogo = JogoDaVelha()
    play(jogo, x_player, o_player, print_game=True)
