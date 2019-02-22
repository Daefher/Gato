from Player import Player
from board import Board

class Game(object):
    def __init__(self):
        self.player1 = Player('O')
        self.player2 = Player('X')
        self.currentPlayer = self.player1
        self.board = Board()
        self.game_state = False

    def game_loop(self):
        print("A jugar!")
        self.board.draw()
        while not self.game_state or not self.game_state:
            self.move(self.currentPlayer)
            if self.currentPlayer.get_type() == self.player1.get_type():
                self.currentPlayer = self.player2
            else:
                self.currentPlayer = self.player1

    def move(self,player):
        print("Turno Jugador "+player.get_type())
        x = input("Ingresa la columna: ")
        y = input("ingresa la fila: ")
        x = int(x)
        y = int(y)
        if x > 2 or x < 0 or y > 2 or y < 0:
            print("Posicion Invalida, pierdes el turno")
            self.board.draw()
        else:
            self.board.put(player,x,y )
            self.game_state = self.check_state()
            if self.game_state:
                print("HAS GANADO!!")
            self.board.draw()
            player.set_state(True)
        return True


    def check_state(self):
        board = self.board.get_board()
        #Check columns
        for i in range(0,3):
            if board[i][1] != ' ' and board[i][0] != ' ' and board[i][2] != ' ':
                if board[i][0] == board[i][1] and board[i][1] == board[i][2]:
                    print(1,i)
                    return True

        #Check rows
        for i in range(0,3):
            if board[0][i] != ' ' and board[1][i] != ' ' and board[2][i] != ' ':
                if board[0][i] == board[1][i] and board[1][i] == board[2][i]:
                    print(2)
                    return True

        #diagonal top left
        if board[0][0] != ' ' and board[1][1] != ' ' and board[2][2] != ' ':
            if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
                print(3)
                return True

        #diagonal top left
        if board[0][2] != ' ' and board[1][1] != ' ' and board[2][0] != ' ':
            if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
                print(4)
                return True

        return False
