from Pieces import *


class Board:
    def __init__(self, size, players, players_forces, warlords_cords):
        self.warlords_cords = warlords_cords
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

    def move(self, move_from, move_to):
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
                self.players_forces[self.field[move_to[0]][move_to[1]].get_owner()].remove(
                    self.field[move_to[0]][move_to[1]])
                self.field[move_to[0]][move_to[1]] = self.field[move_from[0]][move_from[1]]
                self.field[move_to[0]][move_to[1]].move(move_to)
                self.field[move_from[0]][move_from[1]] = Empty()
                return True, ''
            else:
                return False, can_attack[1]
        else:
            return False, "You can't move on your pieces"
        # move_response (success_bool, error_text)

    def checkmate_check(self):
        for i in self.players:
            result = self.check_check(i)
            if result[0]:
                result = self.check_mate(result[1])
                if result[0]:
                    return True, result[1]
        return False, []

    def check_check(self, player):
        checked = []
        chk = False
        if self.warlords_cords[player] is None:
            return False, checked
        for i in self.warlords_cords[player]:
            if self.check_cell_check(i):
                if i not in checked:
                    chk = True
                    checked.append(i)

        return chk, checked

    def check_cell_check(self, cords):
        for enemy in set(self.players) - {self.field[cords[0]][cords[1]].get_owner()}:
            for enemy_piece in self.players_forces[enemy]:
                if enemy_piece.can_attack(cords, self.field)[0]:
                    return True
        return False

    def check_mate(self, checked):
        mated = []
        return False, mated
