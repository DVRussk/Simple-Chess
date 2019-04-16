from Board import *


class Game:
    def __init__(self, profile):
        self.size, self.players, self.players_forces = profile.size, profile.players, profile.players_forces
        self.turn = profile.turn
        self.board = Board(self.size, self.players, self.players_forces)

    def start(self):
        while True:
            self.board.render()
            while True:
                try:
                    move_from, move_to = self.input_move()
                except ValueError:
                    self.error(('IncorrectInput', "Incorrect cords"))
                    continue
                except IndexError:
                    self.error(('IncorrectInput', "Incorrect cord's type"))
                    continue

                if move_from == move_to:
                    self.error(('IncorrectInput', "Start square and Finish square can't be the same square"))
                else:
                    if self.board.cell(move_from).get_owner() == self.get_current_turn():
                        move_response = self.board.move(move_from, move_to, self.get_current_turn())
                        if move_response[0]:
                            if self.board.checkmate_check():
                                self.endgame()
                            self.change_turn()
                            break
                        else:
                            self.error(('IncorrectMove', move_response[1]))
                    else:
                        self.error(('IncorrectInput',
                                    f"This piece is not {self.get_current_turn()}'s piece, "
                                    f"it is {self.board.cell(move_from).get_owner()}'s piece"))

    def input_move(self):
        # TODO exit
        while True:
            rt = input().split()
            rt[0], rt[1] = self.transform((rt[0], rt[1]))
            rt[2], rt[3] = self.transform((rt[2], rt[3]))
            test1, test2 = self.cor_coor(rt[0], rt[1]), self.cor_coor(rt[2], rt[3])
            if test1[0] and test2[0]:
                break
            else:
                if not test1[0]:
                    self.error(test1[1])
                if not test2[0]:
                    self.error(test2[1])
        return (rt[0], rt[1]), (rt[2], rt[3])

    def cor_coor(self, row, col):
        if (0 <= row <= self.size.rows - 1 and isinstance(row, int)) and (
                0 <= col <= self.size.columns - 1 and isinstance(col, int)):
            return True, ''
        else:
            return False, ('IncorrectInput', f'Incorrect coordinates {(row, col)}')

    def get_current_turn(self):
        return self.players[self.turn]

    def error(self, error):
        # error[0] - Error Type
        # error[1] - Error Text
        print('|' + str(error[0]) + '|' + error[1])

    def change_turn(self):
        self.turn += 1
        if self.turn >= len(self.players):
            self.turn -= len(self.players)

    def transform(self, cords):
        return self.size.rows - int(cords[0]), ord(cords[1].lower()) - ord('a')

    def endgame(self):
        # TODO
        # Here we will stop game in case of checkmate
        pass
