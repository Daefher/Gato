
class Board(object):

    __board = []

    def __init__(self):
        #self.showBoard()
        self.board = self.createBoard()

    def draw(self):
        print("--"+"|"+"-0-"+"|"+"-1-"+"|"+"-2-"+"|")
        print("--+---+---+---+")
        print("0"+" | "+str(self.board[0][0])+" | "+str(self.board[0][1])+" | "+str(self.board[0][2])+" |")
        print("--"+"+"+"---"+"+"+"---"+"+"+"---"+"+")
        print("1"+" | "+str(self.board[1][0])+" | "+str(self.board[1][1])+" | "+str(self.board[1][2])+" |")
        print("--"+"+"+"---"+"+"+"---"+"+"+"---"+"+")
        print("2"+" | "+str(self.board[2][0])+" | "+str(self.board[2][1])+" | "+str(self.board[2][2])+" |")


    def createBoard(self):
        v = 0
        tmp = []
        board = []
        for i in range(0,3):
            for j in range(0,3):
                tmp.append(' ')
            board.append(tmp)
            tmp = []
        return board

    def put(self, player, posX, posY):
        if self.board[posX][posY] != ' ':
            return print("Ese espacio ya esta ocupado")
        self.board[posX][posY] = player.get_type()

    def get_board(self):
        return self.board





# board = Board()
#
# board.draw()
# player = Player('X')
# board.move()
