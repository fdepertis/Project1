from TdP_collections.list.positional_list import PositionalList

class CircularPositionalList(PositionalList):

    class Position(PositionalList.Position):
        """An abstraction representing the location of a single element.

        Note that two position instaces may represent the same inherent
        location in the list.  Therefore, users should always rely on
        syntax 'p == q' rather than 'p is q' when testing equivalence of
        positions.
        """
        def __init__(self, container, node):

            """Constructor should not be invoked by user."""
            super(CircularPositionalList.Position, self).__init__(container, node)

        def element(self):
            """Return the element stored at this Position."""
            return super(CircularPositionalList.Position,self).element()

        def __eq__(self, other):
            """Return True if other is a Position representing the same location."""
            return super(CircularPositionalList.Position, self).Position.__eq__(other)

        def __ne__(self, other):
            """Return True if other does not represent the same location."""
            return super(CircularPositionalList.Position, self).Position.__ne__(other)  # opposite of __eq__

    def __init__(self):
        """Create an empty list."""
        self._header = self._Node(None, None, None)
        #self._header._next = self._trailer  # trailer is after header
        #self._trailer._prev = self._header  # header is before trailer

        self._size = 0

    #-------------------------- public accessors --------------------------
    def _make_position(self, node):
        """Return Position instance for given node."""
        if node is self._header:
            return self.Position(self,self._header) # boundary violation
        else:
            return self.Position(self, node)  # legitimate position
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

    def __len__(self):
        """Return the number of elements in the list."""
        return self._size

    def is_empty(self):
        """Return True if list is empty."""
        return self._size == 0


    def add_first(self,e):
        """Inserisce l'elemento e in testa alla lista e restituisce la Position del nuovo elemento"""
        if self.is_empty():
            self._header = self._Node(e,self._header,self._header)
            #riaggiorno i puntatori di header siccome prima di istanziare la classe questi puntavano a none mentre io
            # voglio che ora puntino al nodo aggiornato di header
            self._header._next = self._header
            self._header._prev = self._header
            self._size = 1
            return self._make_position(self._header)
        if self.__len__() == 1:
            """Se c'e' un solo elemento aggiungi un nodo alla testa della lista e crea un nuovo nodo con element header e collega"""
            node = self._Node(self._header._element,self._header,self._header) # update header element in a new position of list
            self._header._prev = node
        else:
            """se c'è più di un elemento aggiungi un nodo alla testa della lista e crea un nuovo nodo con element hedear e collegalo
            sia alla nuova testa che al nodo successivo a cui era collegatata il vecchio nodo di testa"""
            node = self._Node(self._header._element, self._header, self._header._next)
            position = self._make_position(self._header._next)  # position of node next header
            position._node._prev = node  # update node after header
        self._header._element = e
        self._header._next = node
        self._size += 1
        return self._make_position(self._header)


    def add_last(self, e):
        """Inserisce l'elemento e in coda alla lista e restituisce la Position del nuovo elemento"""
        if self.is_empty():
            self._header = self._Node(e, self._header, self._header)
            self._header._next = self._header
            self._header._prev = self._header
            self._size = 1
            return self._make_position(self._header)
        if self.__len__() == 1:
            """Se c'e' un solo elemento aggiungi un nodo alla coda della lista e collegalo all'header
             e collega"""
            node = self._Node(e, self._header, self._header)  # update header element in a new position of list
            self._header._next = node
        else:
            """se c'è più di un elemento aggiungi un nodo alla coda della lista e crea un nuovo nodo con element la vecchia
            coda della lista e collegalo sia alla nuova coda della lista che al nodo precedente  a cui era collegatato
             il vecchio nodo di coda"""
            node = self._Node(e, self._header._prev, self._header)
            position = self._make_position(self._header._prev)  # position of node next header
            position._node._next = node  # update node after header
        #self._header._element = e
        self._header._prev = node
        self._size += 1
        return self._make_position(self._header)


    def before(self,p):
        """Restituisce l'elemento nella Position precedente a p, None se p non ha un predecessore e
                ValueError se p non è una position della lista"""
        if self.is_empty():
            return None
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self,p):
        """Restituisce l'elemento nella Position psuccessiva a p, None se p non ha un successore e
                ValueError se p non è una position della lista"""
        if self.is_empty():
            return None
        node = self._validate(p)
        return self._make_position(node._next)






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

