from circular_positional_list import CircularPositionalList
import datetime


class ScoreBoard:
    class Score:
        def __init__(self, player_name, value, date):
            """Crea uno Score.
            :param player_name: rappresenta il nome del player
            :param value: rappresenta lo score conseguito
            :param score_date: rappresenta la data in cui lo score è stato conseguito
            """
            if type(player_name) is not str:
                raise TypeError("must be string.")
            if type(value) is not int and type(value) is not float:
                raise TypeError("Score value must be an integer.")
            if type(date) is not datetime.date:
                raise TypeError("Score date must be an datetime.date .")
            self._player_name = player_name
            self._value = value
            self._date = date

        def __str__(self):
            """
            :return: Restituisce una stringa che rappresenta gli attributi di un singolo Score.
            """
            return self._player_name + "\t\t" + str(self._value) + "\t\t" + str(self._date)

        def __eq__(self, other):
            """Operatore equal
            :param other: score
            :return: True if equal otherwise False
            """
            if self._player_name == other._player_name and self._value == other._value and self._date == other._score_date:
                return True
            else:
                return False

    #------------------------Public-Methods-----------------------------
    def __init__(self, x = 10):
        """Crea uno Scoreboard di dimensione x.
        :param x: rappresenta la dimensione massima dello Scoreboard
        """
        self._cpl = CircularPositionalList()
        self._max = x

    def __len__(self):
        """
        :return: Restituisce la dimensione dello Scoreboard.
        """
        return self._max

    def __str__(self):
        """
        :return: Restituisce una stringa che rappresenta una tabella contenente tutti gli Score presenti nella Scoreboard.
        """
        cursor = self._cpl.first()
        s = "------------------TOP-10-BEST-100m-----------------\n----\t-----------\t\t\t-----\t\t-----------\n||||\tPlayer Name\t\t\tScore\t\tDate\n----\t-----------\t\t\t-----\t\t-----------\n"
        for i in range(self.size()):
            i += 1
            s += str(i) + "°  \t" + str(cursor.element()) + "\n"
            cursor = self._cpl._next(cursor)
        return s
    #------------------------Private-Methods----------------------------
    def _copy(self):
        """
        Restituisce una copia dello score board
        :return: a copy of scoreboard"""
        new_score = ScoreBoard(self._max)
        for e in self._cpl:
            new_score.insert(e)
        return new_score
    #------------------------Public-Methods-----------------------------
    def size(self):
        """
        :return: Restituisce il numero di Score presenti nello Scoreboard.
        """
        return self._cpl._size

    def is_empty(self):
        """
        :return: Restituisce True se non ci sono Score nello Scoreboard e False altrimenti.
        """
        return self._cpl._size == 0

    def insert(self, s):
        """
        Inserisce un nuovo Score nello ScoreBoard se e solo se non è peggiore dei risultati correntemente salvati.
        Non incrementa la dimensione dello Scoreboard.
        :param s: L'oggetto score da inserire.
        """
        if type(s) is not ScoreBoard.Score:
            raise TypeError("Parameter must be Score typed")
        """for e in self._cpl:
            if e == s:
                return"""
        if self.is_empty():
            self._cpl.add_last(s)
        else:
            cursor = self._cpl.first()
            added = False
            for i in range(self.size()):
                if cursor.element() == s:
                    return
                elif cursor.element()._value > s._value:
                    self._cpl.add_before(cursor, s)
                    added = True
                    break
                else:
                    cursor = self._cpl._next(cursor)
            if not added and self.size() < len(self):
                self._cpl.add_last(s)
            elif self.size() > len(self):
                self._cpl.delete(self._cpl.last())

    def merge(self, new):
        """
        :param new: Rappresenta la lista che verrà accoppiata con self.
        :return: Fonde lo Scoreboard corrente con new selezionando i 10 migliori risultati.
        """
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
            new_sc = ScoreBoard() #10
            for i in range(self.size() + new.size()):
                if self_cursor.element()._value > new_cursor.element()._value and self_counter < self.size() or new_counter == new.size():
                    """Aggiungi un elemento da self se è minore del primo elemento di list2 AND self non è finito
                        OR new è finito"""
                    new_sc.insert(self_cursor.element())
                    self_counter += 1
                    self_cursor = self._cpl._next(self_cursor)
                else:
                    """Altrimenti aggiungi un elemento da new"""
                    new_sc.insert(new_cursor.element())
                    new_counter += 1
                    new_cursor = new._cpl._next(new_cursor)
            return new_sc

    def top(self, i = 1):
        """
        :param i: Il numero di risultati da ritornare.
        :return: Restituisce i migliori i Score nello Scoreboard.
        """
        cursor = self._cpl.first()
        new_list = CircularPositionalList()
        for j in range(min(self.size(), i)):
            new_list.add_last(cursor.element())
            cursor = self._cpl._next(cursor)
        return new_list

    def last(self, i = 1):
        """
        :param i: Il numero di risultati da ritornare.
        :return: Restituisce i peggiori i Score nello Scoreboard.
        """
        cursor = self._cpl.last()
        new_list = CircularPositionalList()
        for j in range(min(self.size(), i)):
            new_list.add_last(cursor.element())
            cursor = self._cpl._prev(cursor)
        return new_list

