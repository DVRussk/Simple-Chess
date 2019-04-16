class Piece:
    def __init__(self, profile):
        self.str = profile[0]
        self.owner = profile[1]
        self.was_moved = profile[2]
        self.cords = profile[3]

    def get_owner(self):
        return self.owner[0]

    def __str__(self):
        return self.owner[1] + self.str

    def can_move(self, cords_to, field):
        pass

    def can_attack(self, cords_to, field):
        pass

    def move(self, cords):
        self.was_moved = True
        self.cords = cords

    def is_line_free(self, cords_to, field):
        if cords_to[0] == self.cords[0] or cords_to[1] == self.cords[1] or \
                abs(cords_to[0] - self.cords[0]) == abs(cords_to[1] - self.cords[1]):
            rows_mod = cords_to[0] - self.cords[0]
            cols_mod = cords_to[1] - self.cords[1]
            if abs(rows_mod) > abs(cols_mod):
                mx = rows_mod
            else:
                mx = cols_mod
            if rows_mod != 0:
                rows_mod //= abs(rows_mod)
            if cols_mod != 0:
                cols_mod //= abs(cols_mod)
            print(rows_mod, cols_mod)
            for i in range(1, abs(mx)):
                if field[self.cords[0] + i * rows_mod][self.cords[1] + i * cols_mod].get_owner() != 'Empty':
                    return False, f"Line isn't free. There is " \
                        f"{field[self.cords[0] + i][self.cords[1] + i].get_owner()}'s" \
                        f" piece on {(self.cords[0] + i * rows_mod, self.cords[1] + i * cols_mod)}"
                pass
            return True, ''
        else:
            return False, f'There id no line between {self.cords} and {cords_to}'
