from TdP_collections.list.positional_list import PositionalList

class CircularPositionalList(PositionalList):

    def __init__(self):
        """Create an empty list."""
        self._header = self._Node(None, None, None)
        self._size = 0

    #-------------------------- public accessors --------------------------

    def _make_position(self, node):
        """Return Position instance for given node."""
        return self.Position(self, node)  # legitimate position

    """restituisce la Position dell’elemento che è identificato
     come il primo oppure None se la lista è vuota"""

    def first(self):
        if self.is_empty():
            return None
        else:
            return self._make_position(self._header)

    """Restituisce la Position dell'elemento che è identificato 
    come l'ultimo oppure None se la lista è vuota"""

    def last(self):
        if self.is_empty():
            return None
        else:
            return self._make_position(self._header._prev)

    def __len__(self):
        """Return the number of elements in the list."""
        return self._size

    def is_empty(self):
        """Return True if list is empty."""
        return self._size == 0

    def _set_header(self, e):
        self._header = self._Node(e, self._header, self._header)
        self._header._next = self._header
        self._header._prev = self._header
        self._size = 1

    def add_first(self,e):
        """Inserisce l'elemento e in testa alla lista e restituisce la Position del nuovo elemento"""
        if self.is_empty():
            self._set_header(e)
        else:
            new_node = self._Node(e, self._header._prev, self._header)
            self._header._prev._next = new_node
            self._header._prev = new_node
            self._header = new_node
            self._size += 1
        return self._make_position(self._header)


    def add_last(self, e):
        """Inserisce l'elemento e in coda alla lista e restituisce la Position del nuovo elemento"""
        if self.is_empty():
            self._set_header(e)
        else:
            new_node = self._Node(e, self._header, self._header._prev)
            self._header._prev._next = new_node
            self._header._prev = new_node
            self._size += 1
        return self._make_position(self._header._prev)


    def before(self,p):
        """Restituisce l'elemento nella Position precedente a p, None se p non ha un predecessore e
                ValueError se p non è una position della lista"""
        if self.is_empty():
            return None
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self,p):
        """Restituisce l'elemento nella Position successiva a p, None se p non ha un successore e
                ValueError se p non è una position della lista"""
        if self.is_empty():
            return None
        node = self._validate(p)
        return self._make_position(node._next)

    def copy(self):
        new_list = CircularPositionalList()
        for e in self.__iter__():
            new_list.add_last(e)
        return new_list

    def __add__(self, other):
        if type(other) is not CircularPositionalList:
            raise TypeError("The second operand is not a cascaded CircularPositionList")
        sum = CircularPositionalList()
        for e in self.__iter__():
            sum.add_last(e)
        for e in other.__iter__():
            sum.add_last(e)
        return sum

    def __contains__(self, item):
        cursor = self.first()
        for i in range(self._size):
            if cursor == item:
                return True
            cursor = self.after(cursor)
        return False

    def __iter__(self):
        cursor = self.first()
        for i in range(self._size):
            yield cursor.element()
            cursor = self.after(cursor)

    def __str__(self):
        s = ""
        for e in self.__iter__():
            s += str(e) + ", "
        s += "\nSize: " + str(self._size) + "\nFirst: " + str(self.first()) + "\nLast:  " + str(self.last()) + "\n"
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