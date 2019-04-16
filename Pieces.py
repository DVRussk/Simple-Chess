from Piece import *


class Empty(Piece):
    def __init__(self):
        super().__init__((' ', ('Empty', ' '), False, (-1, -1)))


class Pawn(Piece):
    def __init__(self, owner, moved, cords):
        super().__init__(('P', (owner[0], owner[1]), moved, cords))
        # owner variable example ('WHITE', 'w')
        if owner[0] == 'WHITE':
            self.sign = -1
        else:
            self.sign = 1

    def can_move(self, cords_to, field):
        if cords_to == (self.cords[0] + self.sign, self.cords[1]):
            return True, ''
        elif cords_to == (self.cords[0] + 2 * self.sign, self.cords[1]) and \
                field[self.cords[0] + self.sign][self.cords[1]].get_owner() == 'Empty' \
                and not self.was_moved:
            return True, ''
        else:
            return False, 'Illegal move'

    def can_attack(self, cords_to, field):
        if cords_to == (self.cords[0] + self.sign, self.cords[1] + 1) or \
                cords_to == (self.cords[0] + self.sign, self.cords[1] - 1):
            return True, ' '
        else:
            return False, 'Illegal move'


class Castle(Piece):
    def __init__(self, owner, moved, cords):
        super().__init__(('C', (owner[0], owner[1]), moved, cords))

    def can_move(self, cords_to, field):
        return self.can_attack(cords_to, field)

    def can_attack(self, cords_to, field):
        if cords_to[0] == self.cords[0] or cords_to[1] == self.cords[1]:
            return self.is_line_free(cords_to, field)
        else:
            return False, 'Illegal move'


class Bishop(Piece):
    def __init__(self, owner, moved, cords):
        super().__init__(('B', (owner[0], owner[1]), moved, cords))

    def can_move(self, cords_to, field):
        return self.can_attack(cords_to, field)

    def can_attack(self, cords_to, field):
        if abs(cords_to[0] - self.cords[0]) == abs(cords_to[1] - self.cords[1]):
            return self.is_line_free(cords_to, field)
        else:
            return False, 'Illegal move'


class Queen(Piece):
    def __init__(self, owner, moved, cords):
        super().__init__(('Q', (owner[0], owner[1]), moved, cords))

    def can_move(self, cords_to, field):
        return self.can_attack(cords_to, field)

    def can_attack(self, cords_to, field):
        if cords_to[0] == self.cords[0] or cords_to[1] == self.cords[1] or \
                abs(cords_to[0] - self.cords[0]) == abs(cords_to[1] - self.cords[1]):
            return self.is_line_free(cords_to, field)
        else:
            return False, 'Illegal move'
