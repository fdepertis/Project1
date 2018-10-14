from circular_positional_list import CircularPositionalList
from datetime import date

class ScoreBoard(CircularPositionalList):
    class Score:
        def __init__(self, player_name, value, score_date):
            if type(value) is not int:
                raise TypeError("Score value must be an integer.")
            self._player_name = player_name
            self._value = value
            self._score_date = score_date

        def __str__(self):
            return self._player_name + "\t\t\t" + str(self._value) + "\t\t" + str(self._score_date)

    def __init__(self, x = 10):
        self._cpl = CircularPositionalList()
        self._x = x

    def __len__(self):
        return self._x

    def __str__(self):
        cursor = self._cpl.first()
        s = "Player Name\t\tScore\t\tDate\n"
        for i in range(self.size()):
            s += str(cursor.element()) + "\n"
            cursor = self._cpl.after(cursor)
        return s

    def size(self):
        return self._cpl._size

    def is_empty(self):
        return self._cpl._size == 0

    def insert(self, s):
        if type(s) is not ScoreBoard.Score:
            raise TypeError("Parameter must be Score typed")
        elif self.is_empty():
            self._cpl.add_last(s)
        else:
            cursor = self._cpl.first()
            added = False
            for i in range(self.size()):
                if cursor.element()._value < s._value:
                    self._cpl.add_before(cursor, s)
                    added = True
                    break
                else:
                    cursor = self._cpl.after(cursor)
            if not added:
                self._cpl.add_last(s)
            if self.size() > len(self):
                self._cpl.delete(self._cpl.last())

    def merge(self, new):
        """Fonde lo Scoreboard corrente con new selezionando i 10 migliori risultati."""
        if type(self) is not type(new):
            raise TypeError("The lists to merge are not ScoreBoard typed.")
        elif self.is_empty():
            return new
        elif new.is_empty():
            return self
        else:
            self_cursor = self._cpl.first()     #cursore per le position di self
            new_cursor = new._cpl.first()       #cursore per le position di new
            self_counter = 0                    #counter per le position di self
            new_counter = 0                     #counter per le position di new
            new_sc = ScoreBoard()
            for i in range(min(self.size() + new.size(), 10)):
                if self_cursor.element()._value > new_cursor.element()._value and self_counter < self.size() or new_counter == new.size():
                    """Aggiungi un elemento da self se è minore del primo elemento di list2 AND self non è finito
                        OR new è finito"""
                    new_sc.insert(self_cursor.element())
                    self_counter += 1
                    self_cursor = self._cpl.after(self_cursor)
                else:
                    """Altrimenti aggiungi un elemento da new"""
                    new_sc.insert(new_cursor.element())
                    new_counter += 1
                    new_cursor = new._cpl.after(new_cursor)
            return new_sc

    def top(self, i = 1):
        cursor = self._cpl.first()
        for j in range(min(self.size(), i)):
            yield cursor.element()
            cursor = self._cpl.after(cursor)

    def last(self, i = 1):
        cursor = self._cpl.last()
        for j in range(min(self.size(), i)):
            yield cursor.element()
            cursor = self._cpl.before(cursor)


if __name__ == '__main__':
    sb0 = ScoreBoard()
    sb1 = ScoreBoard()
    s01 = ScoreBoard.Score("01", 100, date.today())
    s02 = ScoreBoard.Score("02", 200, date.today())
    s03 = ScoreBoard.Score("03", 300, date.today())
    s04 = ScoreBoard.Score("04", 400, date.today())
    s05 = ScoreBoard.Score("05", 500, date.today())
    s06 = ScoreBoard.Score("06", 600, date.today())
    s11 = ScoreBoard.Score("11", 1100, date.today())
    s12 = ScoreBoard.Score("12", 1200, date.today())
    s13 = ScoreBoard.Score("13", 1300, date.today())
    s14 = ScoreBoard.Score("14", 1400, date.today())
    s15 = ScoreBoard.Score("15", 1500, date.today())
    s16 = ScoreBoard.Score("16", 1600, date.today())
    sb0.insert(s01)
    sb0.insert(s02)
    sb0.insert(s03)
    sb0.insert(s04)
    sb0.insert(s05)
    sb0.insert(s06)
    sb1.insert(s11)
    sb1.insert(s12)
    sb1.insert(s13)
    sb1.insert(s14)
    sb1.insert(s15)
    sb1.insert(s16)
    print(str(sb0))
    print(str(sb1))

    sbm = sb0.merge(sb1)
    print(str(sbm))
