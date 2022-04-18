## each cell in puzzle
class Cell:
    def __init__(self, x, y, domain=None, value='_'):
        if domain is None:
            self.domain = ['w', 'b']
        else:
            self.domain = domain
        self.x = x
        self.y = y
        self.value = value