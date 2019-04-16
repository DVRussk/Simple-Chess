from Pieces import *


class Size:
    def __init__(self, rows, columns):
        self.rows, self.columns = rows, columns


class Base:
    def __init__(self):
        self.size = Size(8, 8)
        self.players = ['WHITE', 'BLACK']
        self.warlords_cords = {
            'WHITE': None,
            'BLACK': [self.transform((3, 'd'))]
        }
        self.players_forces = {
            'WHITE': [Pawn(('WHITE', 'w'), False, self.transform((2, chr(i + ord('a') - 1)))) for i in range(1, 9)] +
                     [Castle(('WHITE', 'w'), False, self.transform((1, 'a'))),
                      Castle(('WHITE', 'w'), False, self.transform((1, 'h')))] +
                     [Bishop(('WHITE', 'w'), False, self.transform((1, 'c'))),
                      Bishop(('WHITE', 'w'), False, self.transform((1, 'f')))] +
                     [Queen(('WHITE', 'w'), False, self.transform((1, 'd')))],
            'BLACK': [Pawn(('BLACK', 'b'), False, self.transform((7, chr(i + ord('a') - 1)))) for i in range(1, 9)] +
                     [Castle(('BLACK', 'b'), False, self.transform((8, 'a'))),
                      Castle(('BLACK', 'b'), False, self.transform((8, 'h')))] +
                     [Bishop(('BLACK', 'b'), False, self.transform((8, 'c'))),
                      Bishop(('BLACK', 'b'), False, self.transform((8, 'f')))] +
                     [Queen(('BLACK', 'b'), False, self.transform((8, 'e')))]}
        self.turn = 0

    def transform(self, cords):
        return self.size.rows - int(cords[0]), ord(cords[1].lower()) - ord('a')
