from TdP_collections.list.positional_list import PositionalList

class CircularPositionalList(PositionalList):

    def __init__(self):
        """Create an empty list."""
        self._header = self._Node(None, None, None)
        #self._header._next = self._trailer  # trailer is after header
        #self._trailer._prev = self._header  # header is before trailer
        self._size = 0

    #-------------------------- public accessors --------------------------
    def _make_position(self, node):
        """Return Position instance for given node."""
        return self.Position(self, node)  # legitimate position
    """
    def _validate(self, p):
        Return position's node, or raise appropriate error if invalid.
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node is None:  # convention for deprecated nodes
            raise ValueError('p is no longer valid')
        return p._node
    """

    """restituisce la Position dell’elemento che è identificato
     come il primo oppure None se la lista è vuota"""

    def first(self):
        if self.is_empty():
            return None
        return self._make_position(self._header)

    """Restituisce la Position dell'elemento che è identificato 
    come l'ultimo oppure None se la lista è vuota"""

    def last(self):

        if self.is_empty():
            return None
        return self._make_position(self._header._prev)


    def before(self,p):
        """Restituisce l'elemento nella Position precedente a p, None se p non ha un predecessore e
                ValueError se p non è una position della lista"""
        if self.is_empty():
            return None
        return super().before(p)

    def after(self,p):
        """Restituisce l'elemento nella Position psuccessiva a p, None se p non ha un successore e
                ValueError se p non è una position della lista"""
        if self.is_empty():
            return None
        return super().after(p)

    def is_empty(self):
        """Return True if list is empty."""
        return self._size == 0

    def is_sorted(self):
        """Restituisce True se la lista è ordinata e False altrimenti"""
        return True

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

    def add_before(self, p, e):
        """Inserisce un nuovo (elemento e) prima del nodo nella (Position p) e restituisce la position
                del nuovo elemento"""
        return super().add_before(p,e)

    def add_after(self, p, e):
        """Inserisce un nuovo(elemento e) dopo del nodo nella(Position p) e restituisce la position
                del nuovo elemento """
        return super().add_after(p,e)

    def find(self, e):
        """Restituisce una Position contenente la prima occorrenza dell'elemento e nella lista
                o None se non e' presente"""
        cursor = self.first()
        for n in range(self._size):
            if cursor.element() == e:
                return cursor
            cursor = self.after(cursor)
        return None

    def replace(self, p, e):
        """Sostituisce l'elemento in Position p con l'elemento e e restituisce il vecchio elemento"""
        return super().replace(p ,e)

    def delete(self, p):
        """Rimuove e restituisce l'elemento in Position p dalla lista e invalida p"""
        return super().delete(p)

    def clear(self):
        """Rimuove tutti gli elementi della lista invalidando le corrispondeti position"""
        cursor = self.last()
        #cursor_up = cursor
        for i in range(self._size):
            print("SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS")
            print(self.to_string())
            print("SSSSSSSSSSSSSSSSSSssssssssssssssssssssssssssssssssssssssss")
            self.delete(cursor)
            cursor = self.before(cursor)

    def count(self, e):
        """Restituisce il numero di occorrenze di e nella lista"""
        counter=0
        for obj in self.__iter__():
            if obj == e:
                counter += 1
        return counter

    def reverse(self):
        """Inverte l'ordine degli elementi nella lista"""
        first_cursor = self.first()
        last_cursor = self.last()
        print(last_cursor.element(),self.before(last_cursor).element(),self.before(self.before(last_cursor)).element(),self.before(self.before(self.before(last_cursor))).element())
        for k in range(self._size):
            print(k, first_cursor.element(), last_cursor.element() ,self.before(last_cursor).element())
            first_cursor._node._element = last_cursor._node._element
            first_cursor = self.after(first_cursor)
            last_cursor = self.before(last_cursor)


    def __len__(self):
        """Return the number of elements in the list."""
        return self._size









    def to_string(self):
        w=self._header
        first = self._header._next
        print("LISTA - Size-->"+str(self._size)+":\nElementoHeader:"+str(self._header)+" Precedente:"+str(self._header._prev)+" Successore:"+str(self._header._next))
        i = 1
        print("Elemento" + str(i) + ":" + str(first) + " Precedente:" + str(first._prev) + " Successore:" + str(first._next))
        while first._next._element != w._element:
            first = self._make_position(first)
            after = self.after(first)
            i += 1
            print("Elemento"+str(i)+":" + str(after.element()) + " Precedente:" + str(after._node._prev._element) + " Successore:" + str(after._node._next._element))
            first=self._validate(after)




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
        s += "\nSize: " + str(self._size) + "\nFirst: " + str(self.first()) +", " + "\nLast:  " + str(self.last()) +", "+ "\n"
        return s








"""
    def append(self,x):
    def extend(self, iterable):
    def insert(self, i, x):
    def remove(self, x):
    def pop(self,i=None):
    def clear(self):
    def index(self, x,start=None, end=None):
    def count(self, x):
    def sort(self, key=None, reverse=False):
    def reverse(self):
    def copy(self):	
    def __add__():
    def __iadd__():
    def __le__():
    def __eq__():
    def __ne__():
    def __ge__():
    def __gt__():
    def __eq__():
    def __ne__():
    def __contains__():
    def __delitem__():
    def __getitem__():
    def __setitem__():
    def __del__():
    def __str__():
    def __bool__():
"""
if __name__ == '__main__':
    list2 = CircularPositionalList()
    list2.add_first(2)
    print("1-ELEMENTO AGGIUNTO IN TESTA, LISTA INIZIALMENTE VUOTA")
    print("primo elemento--->", list2.first().element())
    print("ultimo elemento--->", list2.last().element())
    print("CORRETTO PERCHE' SE LA LISTA ERA INIZIALMENTE VUOTA ALL'INSERIMENTO DEL PRIMO ELEMENTO\nQUESTO SARÀ SIA LA TESTA CHE LA CODA DELLA LISTA")
    print("predecessore del primo elemento sarà sempre l'ultimo (ultimo == primo siccome c'è un solo elemento) --->",list2.before(list2.first()).element())
    print("succcessore del primo elemento (ultimo == primo siccome c'è un solo elemento) --->",list2.after(list2.first()).element())
    list2.add_first(5)
    print("2-NUOVO ELEMENTO AGGIUNTO IN TESTA")
    print("primo elemento--->", list2.first().element())
    print("ultimo elemento--->", list2.last().element())
    print("predecessore del primo elemento sarà sempre l'ultimo --->",list2.before(list2.first()).element())
    print("succcessore del primo elemento in questo caso sarà l'ultimo siccome ci sono solamente 2 elementi --->",list2.after(list2.first()).element())

    list2.add_first(6)
    print("3-NUOVO ELEMENTO AGGIUNTO IN TESTA")
    print("primo elemento--->", list2.first().element())
    print("ultimo elemento--->", list2.last().element())
    print("predecessore del primo elemento --->",list2.before(list2.first()).element())
    print("succcessore del primo elemento in questo caso sarà l'ultimo siccome ci sono solamente 2 elementi --->",list2.after(list2.first()).element())
    print("-------------------------------------------------------------------")
    list2.to_string()
    list2.add_before(list2.first(),10)
    list2.to_string()
    list2.add_after(list2.first(),20)
    list2.to_string()
    print("Cerca 10 nella lista:")
    if list2.find(10) is None:
        print("Elemento non trovato")
    else:
        print("Elemento trovato")
        print("Cerca 50 nella lista:")
    if list2.find(50) is None:
        print("Elemento non trovato")
    else:
        print("Elemento trovato")
    list2.replace(list2.find(10),70)
    list2.to_string()
    list2.delete(list2.find(20))
    list2.to_string()
    list2.delete(list2.find(5))
    list2.to_string()
    list2.delete(list2.find(2))
    list2.to_string()
    list2.delete(list2.find(6))
    list2.to_string()
    list2.clear()
    list2.to_string()
    print("-------------------------------------------------------------------")
    list2.add_last(1)
    print("ELEMENTO AGGIUNTO IN CODA, LISTA INIZIALMENTE VUOTA")
    print("primo elemento--->", list2.first().element())
    print("ultimo elemento--->", list2.last().element())
    print("CORRETTO PERCHE' SE LA LISTA ERA INIZIALMENTE VUOTA ALL'INSERIMENTO DEL PRIMO ELEMENTO\nQUESTO SARÀ SIA LA TESTA CHE LA CODA DELLA LISTA")
    list2.add_last(2)
    print("NUOVO ELEMENTO AGGIUNTO IN CODA")
    print("primo elemento--->", list2.first().element())
    print("ultimo elemento--->", list2.last().element())
    list2.add_last(3)
    print("NUOVO ELEMENTO AGGIUNTO IN CODA")
    print("primo elemento--->", list2.first().element())
    print("ultimo elemento--->", list2.last().element())



