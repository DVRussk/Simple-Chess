from Pieces import *


class Size:
    def __init__(self, rows, columns):
        self.rows, self.columns = rows, columns


class Base:
    def __init__(self):
        self.size = Size(8, 8)
        self.players = ['WHITE', 'BLACK']
        self.players_forces = {
            'WHITE': [Pawn(('WHITE', 'w'), False, self.transform((2, chr(i + ord('a') - 1)))) for i in range(1, 9)] +
                     [Castle(('WHITE', 'w'), False, self.transform((3, 'd')))],
            'BLACK': [Pawn(('BLACK', 'b'), False, self.transform((7, chr(i + ord('a') - 1)))) for i in range(1, 9)] +
                     []}
        self.turn = 0

    def transform(self, cords):
        return self.size.rows - int(cords[0]), ord(cords[1].lower()) - ord('a')
