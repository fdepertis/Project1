from TdP_collections.list.positional_list import PositionalList

class CircularPositionalList(PositionalList):

    def __init__(self):
        """Crea una lista vuota"""
        self._header = None
        self._size = 0

    def _make_position(self, node):
        """Ritorna la Position del nodo dato"""
        return self.Position(self, node)

    def first(self):
        """Restituisce la Position dell’elemento che è identificato
             come il primo oppure None se la lista è vuota"""
        if self.is_empty():
            return None
        else:
            return self._make_position(self._header)

    def last(self):
        """Restituisce la Position dell'elemento che è identificato
            come l'ultimo oppure None se la lista è vuota"""
        if self.is_empty():
            return None
        else:
            return self._make_position(self._header._prev)

    def before(self, p):
        """Restituisce l'elemento nella Position precedente a p, None se p non ha un predecessore e
            ValueError se p non è una position della lista"""
        if self.is_empty():
            return None
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self, p):
        """Restituisce l'elemento nella Position successiva a p, None se p non ha un successore e
            ValueError se p non è una position della lista"""
        if self.is_empty():
            return None
        node = self._validate(p)
        return self._make_position(node._next)

    def is_empty(self):
        """Restituisce True se la lista è vuota e False altrimenti"""
        return self._size == 0

    def _set_header(self, e):
        """Metodo privato utilizzato da add_first e add_last per settare il primo elemento della lista"""
        self._header = self._Node(e, self._header, self._header)
        self._header._next = self._header
        self._header._prev = self._header
        self._size = 1
        return self._make_position(self._header)

    def add_first(self, e):
        """Inserisce l'elemento e in testa alla lista e restituisce la Position del nuovo elemento"""
        if self.is_empty():
            return self._set_header(e)
        else:
            header_position = self.add_before(self.first(), e)
            self._header = self._validate(header_position)
            return header_position

    def add_last(self, e):
        """Inserisce l'elemento e in coda alla lista e restituisce la Position del nuovo elemento"""
        if self.is_empty():
            return self._set_header(e)
        else:
            return self.add_after(self.last(), e)

    def add_before(self, p, e):
        """Inserisce un nuovo (elemento e) prima del nodo nella (Position p)
            e restituisce la position del nuovo elemento"""
        return super().add_before(p, e)

    def add_after(self, p, e):
        """Inserisce un nuovo(elemento e) dopo del nodo nella(Position p)
            e restituisce la position del nuovo elemento """
        return super().add_after(p, e)

    def find(self, e):
        """Restituisce una Position contenente la prima occorrenza dell'elemento e nella lista
            o None se non è presente"""
        cursor = self.first()
        for i in range(self._size):
            if cursor.element() == e:
                return cursor
            else:
                cursor = self.after(cursor)
        return None

    def replace(self, p, e):
        """Sostituisce l'elemento in Position p con l'elemento e e restituisce il vecchio elemento"""
        return super().replace(p, e)

    def delete(self, p):
        """Rimuove e restituisce l’elemento in Position p dalla lista e invalida p"""
        if p == self.first() and self._size>1:
            self._header = self._header._next
        return super().delete(p)

    def clear(self):
        """Rimuove tutti gli elementi della lista invalidando le corrispondenti Position"""
        cursor = self.last()
        for i in range(self._size):
            next_cursor = self.before(cursor)
            self.delete(cursor)
            cursor = next_cursor

    def count(self, e):
        """Restituisce il numero di occorrenze di e nella lista"""
        counter = 0
        for obj in self.__iter__():
            if obj == e:
                counter += 1
        return counter

    def reverse(self):
        """Inverte l'ordine degli elementi nella lista"""
        left_cursor = self.first()
        copy = self.copy()
        right_cursor = copy.last()
        for i in range(self._size):
            left_cursor._node._element = right_cursor._node._element
            left_cursor = self.after(left_cursor)
            right_cursor = copy.before(right_cursor)

    def copy(self):
        """Restituisce una nuova CircularPositionalList che contiene gli stessi elementi
            della lista corrente memorizzati nello stesso ordine"""
        new_list = CircularPositionalList()
        for e in self.__iter__():
            new_list.add_last(e)
        return new_list

    #------------------------ OPERATORS ----------------------

    def __add__(self, other):
        """Crea una lista con tutti gli elementi di x e tutti gli elementi di y
            inseriti dopo l’ultimo elemento di x"""
        if type(other) is not CircularPositionalList:
            raise TypeError("The second operand is not a cascaded CircularPositionList")
        sum = CircularPositionalList()
        for e in self.__iter__():
            sum.add_last(e)
        for e in other.__iter__():
            sum.add_last(e)
        return sum

    def __contains__(self, item):
        """Restituisce True se p è presente nella lista e False altrimenti"""
        cursor = self.first()
        for i in range(self._size):
            if cursor == item:
                return True
            cursor = self.after(cursor)
        return False

    def __getitem__(self, item):
        """Restituisce l’elemento contenuto nella position p"""
        node = self._validate(item)
        return node._element

    def __len__(self):
        """Restituisce il numero di elementi contenuti in x"""
        return self._size

    def __setitem__(self, key, value):
        """Sostituisce l’elemento nella position p con e"""
        node = self._validate(key)
        node._element = value

    def __del__(self, item):
        """Rimuove l’elemento nella position p invalidando la position"""
        self.delete(item)

    def __iter__(self):
        """Generatore che restituisce gli elementi della lista a partire da quello che è
            identificato come primo fino a quello che è identificato come ultimo"""
        cursor = self.first()
        for i in range(self._size):
            yield cursor.element()
            cursor = self.after(cursor)

    def __str__(self):
        """Rappresenta il contenuto della lista come una sequenza di elementi,
            separati da virgole, partendo da quello che è identificato come primo"""
        s = ""
        for e in self.__iter__():
            s += str(e) + ", "
        #s += "\nSize: " + str(self._size) + "\nFirst: " + str(self.first()) + "\nLast:  " + str(self.last()) + "\n"
        return s

if __name__ == '__main__':
    cpl = CircularPositionalList()
    print(str(cpl))
    cpl.add_first(1)
    print(str(cpl))
    cpl.add_first(2)
    print(str(cpl))
    cpl.add_first(3)
    print(str(cpl))
    cpl.add_first(4)
    print(str(cpl))
    cpl.add_last(5)
    print(str(cpl))
    cpl.add_last(6)
    print(str(cpl))
    cpl.add_last(7)
    print(str(cpl))
    print("cpl contiente first? ", cpl.first() in cpl)
    print("cpl contiente last? ", cpl.last() in cpl)
    print("cpl contiene None?", None in cpl)
    print("creo una nuova lista chiamata cpl2 con gli stessi elementi di cpl")
    cpl2 = cpl.copy()
    print(cpl2.first())
    print(str(cpl2))
    print("cpl2 è uguale a cpl?", cpl2 == cpl)
    print("Sia cpl3 = cpl + cpl2")
    cpl3 = cpl + cpl2
    print(str(cpl3))
    print("Quanti 1 ci sono in cpl3? ", cpl3.count(1))
    print("Quanti 9 ci sono in cpl3? ", cpl3.count(9))
    print("------------")
    print(str(cpl))
    cpl.reverse()
    print(str(cpl))
    cpl.delete(cpl.last())
    print(str(cpl))
    cpl.delete(cpl.first())
    print(str(cpl))
    print("Svuoto cpl:")
    cpl.clear()
    print(str(cpl))
    cpl.add_last(10)
    cpl.add_last(20)
    cpl.add_last(30)
    cpl.add_last(40)
    print("Il primo è:", cpl[cpl.first()])
    print("L'ultimo è:", cpl[cpl.last()])
    print(str(cpl))
    print("Sostituisco 40 a 50")
    cpl[cpl.last()]=50
