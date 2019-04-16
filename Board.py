from Pieces import *


class Board:
    def __init__(self, size, players, players_forces):
        self.size, self.players, self.players_forces = size, players, players_forces
        self.field = [[Empty() for i in range(self.size.columns)] for i in range(self.size.rows)]
        for y in self.players:
            for i in self.players_forces[y]:
                self.field[i.cords[0]][i.cords[1]] = i

    def render(self):
        print(f'        +{"+".join(["----" for i in range(self.size.columns)])}+')
        for row in range(self.size.rows):
            print(' ', str(self.size.rows - row) + '(' + str(row) + ')', end='  ')
            for col in range(self.size.columns):
                print('|', self.cell((row, col)), end=' ')
            print('|')
            print(f'        +{"+".join(["----" for i in range(self.size.columns)])}+')
        print(end='         ')
        for col in range(self.size.rows):
            print(chr(ord('a') + col) + '(' + str(col) + ')', end=' ')
        print()

    def cell(self, cords):
        return self.field[cords[0]][cords[1]]

    def move(self, move_from, move_to, current_turn):
        # TODO
        cell_to = self.cell(move_to)
        cell_from = self.cell(move_from)
        if cell_to.get_owner() == 'Empty':
            can_move = cell_from.can_move(move_to, self.field)
            if can_move[0]:
                self.field[move_to[0]][move_to[1]] = self.field[move_from[0]][move_from[1]]
                self.field[move_to[0]][move_to[1]].move(move_to)
                self.field[move_from[0]][move_from[1]] = Empty()
                return True, ''
            else:
                return False, can_move[1]
        elif cell_to.get_owner() != cell_from.get_owner():
            can_attack = cell_from.can_attack(move_to, self.field)
            if can_attack[0]:
                self.field[move_to[0]][move_to[1]] = self.field[move_from[0]][move_from[1]]
                self.field[move_to[0]][move_to[1]].move(move_to)
                self.field[move_from[0]][move_from[1]] = Empty()
                return True, ''
            else:
                return False, can_attack[1]
        else:
            return False, "You can't move on your pieces"
        # move_response (succes_bool, error_text)

    def checkmate_check(self):
        # TODO
        # Here we will check if there is check, mate or checkmate
        return False
