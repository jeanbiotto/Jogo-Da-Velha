import math
import random
from traceback import print_tb

class Player:
    def __init__(self, letter):
        # letter é X ou O
        self.letter = letter


    # Todos precisam ter a chance de jogar ao iniciar o jogo
    def get_move(sefl, game):
        pass


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        # Para ter um espaço disponivel para a proxima jogada
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            print(' ')
            square = input('Jogador ' "'" + self.letter + "'" ' é sua vez, escolha um lugar para jogar (0-8): ')
            # Checar se o valor é válido por um numero inteiro
            # se não for ou se lugar não está disponivel
            # retornar como jogada inválida
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Jogada inválida, tente novamente!')
        return val

