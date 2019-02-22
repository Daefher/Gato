class Player(object):

    def __init__(self, type):
        self.type = type
        self.state = False

    def get_type(self):
        return self.type

    def set_state(self, newState):
        self.state = newState

    def get_state(self):
        return self.state
