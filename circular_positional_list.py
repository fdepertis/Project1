from TdP_collections.list.positional_list import PositionalList


class CircularPositionalList(PositionalList):

    def __init__(self):
        """Crea una lista vuota."""
        self._header = None
        self._size = 0

    #-------------------------- Private-methods---------------------------

    def _make_position(self, node):
        """
        :param node: Rappresenta il nodo del quale è richiesta la Position.
        :return: Restituisce la Position del nodo dato.
        """
        return self.Position(self, node)

    def _set_header(self, e):
        """
        :param e: Rappresenta l'elemento da inserire in cima alla lista.
        :return: Ritorna la posizione del primo elemento della lista.
        """
        self._header = self._Node(e, None, None)
        self._header._prev = self._header
        self._header._next = self._header
        self._size = 1
        return self._make_position(self._header)

    def _prev(self, p):
        """
        :param p: Rappresenta la Position di riferimento.
        :return: Restituisce la Position precedente a p, None se p non ha un predecessore e
                 ValueError se p non è una position della lista.
        """
        if self.is_empty():
            return None
        else:
            return super().before(p)

    def _next(self, p):
        """
        :param p: Rappresenta la Position di riferimento.
        :return: Restituisce la Position successiva a p, None se p non ha un successore e
                 ValueError se p non è una position della lista."""
        if self.is_empty():
            return None
        else:
            return super().after(p)

    def _check_sortability(self):
        """
        :return: Restituisce un TypeError nel caso in cui la lista contenga elementi non tutti dello stesso tipo.
        """
        first_type = type(self.first().element())
        cursor = self._next(self.first())
        for i in range(self._size - 1):
            if type(cursor.element()) is not first_type:
                raise TypeError("List cannot be sorted because elements are not all of the same type.")
            else:
                cursor = self._next(cursor)

   #----------------------------Public-Methods----------------------------

    def first(self):
        """
        :return: Restituisce la Position dell’elemento che è identificato come il primo oppure None se la lista è vuota.
        """
        if self.is_empty():
            return None
        else:
            return self._make_position(self._header)

    def last(self):
        """
        :return: Restituisce la Position dell'elemento che è identificato come l'ultimo oppure None se la lista è vuota.
        """
        if self.is_empty():
            return None
        else:
            return self._make_position(self._header._prev)

    def before(self, p):
        """
        :param p: Rappresenta la Position di riferimento.
        :return: Restituisce l'elemento nella Position precedente a p, None se p non ha un predecessore e
                ValueError se p non è una position della lista.
        """
        if self.is_empty() or self._size == 1:
            return None
        node = self._validate(p)
        return node._prev._element

    def after(self, p):
        """
        :param p: Rappresenta la Position di riferimento.
        :return: Restituisce l'elemento nella Position successiva a p, None se p non ha un successore e
                ValueError se p non è una position della lista.
        """
        if self.is_empty() or self._size == 1:
            return None
        node = self._validate(p)
        return node._next._element

    def is_empty(self):
        """
        :return: Restituisce True se la lista è vuota altrimenti False.
        """
        return self._size == 0

    def is_sorted(self):
        """
        :return: Restituisce True se la lista è ordinata e False altrimenti. Si definisce ordinata una lista ordinata
                 i cui elementi sono tutti dello stesso tipo e sono disposti in ordine crescente a partire dall'header.
        """
        cursor = self.first()
        first_type = type(cursor.element())
        for i in range(self._size - 1):
            if type(self._next(cursor).element()) is not first_type or cursor.element() > self._next(cursor).element():
                return False
            else:
                cursor = self._next(cursor)
        return True

    def add_first(self, e):
        """
        :param e: Rappresenta l'elemento da inserire in testa alla lista.
        :return: Inserisce l'elemento e in testa alla lista e restituisce la Position del nuovo elemento.
        """
        if self.is_empty():
            return self._set_header(e)
        else:
            header_position = self.add_before(self.first(), e)
            self._header = self._validate(header_position)
            return header_position

    def add_last(self, e):
        """
        :param e: Rappresenta l'elemento da inserire in coda alla lista.
        :return: Inserisce l'elemento e in coda alla lista e restituisce la Position del nuovo elemento.
        """
        if self.is_empty():
            return self._set_header(e)
        else:
            return self.add_after(self.last(), e)

    def add_before(self, p, e):
        """
        :param p: Rappresenta la position di riferimento.
        :param e: Rappresenta l'elemento da inserire nella Position precedente a p.
        :return: Inserisce un nuovo elemento e prima del nodo nella Position p e restituisce la Position
                 del nuovo elemento.
        """
        new_position = super().add_before(p, e)
        if p == self.first():
            self._header = self._validate(new_position)
        return new_position

    def add_after(self, p, e):
        """
        :param p: Rappresenta la position di riferimento.
        :param e: Rappresenta l'elemento da inserire nella Position successiva a p.
        :return: Inserisce un nuovo elemento e dopo il nodo nella Position p e restituisce la Position
                 del nuovo elemento.
        """
        return super().add_after(p, e)

    def find(self, e):
        """Restituisce una Position contenente la prima occorrenza dell'elemento e nella lista
                o None se non e' presente"""
        cursor = self.first()
        for i in range(self._size):
            if cursor.element() == e:
                return cursor
            else:
                cursor = self._next(cursor)
        return None

    def replace(self, p, e):
        """Sostituisce l'elemento in Position p con l'elemento e e restituisce il vecchio elemento"""
        return super().replace(p ,e)

    def delete(self, p):
        """Rimuove e restituisce l'elemento in Position p dalla lista e invalida p"""
        if p == self.first() and self._size > 1:
            self._header = self._header._next
        del_node = super().delete(p)
        p._node = None
        p._container = None
        return del_node

    def clear(self):
        """Rimuove tutti gli elementi della lista invalidando le corrispondeti position"""
        cursor = self.last()
        for i in range(self._size):
            next_cursor = self._prev(cursor)
            self.delete(cursor)
            cursor = next_cursor

    def count(self, e):
        """Restituisce il numero di occorrenze di e nella lista"""
        counter = 0
        for i in self.__iter__():
            if i == e:
                counter += 1
        return counter

    def reverse(self):
        """Inverte l'ordine degli elementi nella lista"""
        left_cursor = self.first()
        copy = self.copy()
        right_cursor = copy.last()
        for i in range(self._size):
            left_cursor._node._element = right_cursor.element()
            left_cursor = self._next(left_cursor)
            right_cursor = copy._prev(right_cursor)

    def copy(self):
        """Restituisce una nuova CircularPositionalList che contiene gli stessi elementi
            della lista corrente memorizzati nello stesso ordine"""
        new_list = CircularPositionalList()
        for e in self:
            new_list.add_last(e)
        return new_list

    #--------------------------Operators---------------------------------

    def __add__(self, other):
        """Crea una lista con tutti gli elementi di x e tutti gli elementi di y
            inseriti dopo l’ultimo elemento di x"""
        if type(other) is not CircularPositionalList:
            raise TypeError("The second operand is not a cascaded CircularPositionList")
        sum = CircularPositionalList()
        for e in self:
            sum.add_last(e)
        for e in other:
            sum.add_last(e)
        return sum

    def __iadd__(self, other):
        if type(other) is not CircularPositionalList:
            raise TypeError("The second operand is not a cascaded CircularPositionList")
        for e in other:
            self.add_last(e)
        return self

    def __contains__(self, item):
        """Restituisce True se p è presente nella lista e False altrimenti"""
        cursor = self.first()
        for i in range(self._size):
            if cursor == item:
                return True
            cursor = self._next(cursor)
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

    def __delitem__(self, key):
        """Rimuove l’elemento nella position p invalidando la position"""
        self.delete(key)

    def __iter__(self):
        """Generatore che restituisce gli elementi della lista a partire da quello che è
            identificato come primo fino a quello che è identificato come ultimo"""
        cursor = self.first()
        for i in range(self._size):
            yield cursor.element()
            cursor = self._next(cursor)

    def __str__(self):
        """Rappresenta il contenuto della lista come una sequenza di elementi,
            separati da virgole, partendo da quello che è identificato come primo"""
        s = ""
        for e in self:
            s += str(e) + ", "
        #s += "\nSize: " + str(self._size) + "\nFirst: " + str(self.first()) + "\nLast:  " + str(self.last()) + "\n"
        return s[0:-2]

    def __eq__(self, other):
        """
        :param other: Rappresenta un'altra CircularPositionList
        :return: Restituisce True se le liste sono uguali, ovvero se hanno gli stessi valori e False altrimenti
        """
        if type(self) is not type(other):
            return False
        else:
            self_cursor = self.first()
            other_cursor = other.first()
            for i in range(max(self._size, other._size)):
                if not self_cursor.element() == other_cursor.element():
                    return False
                else:
                    self_cursor = self._next(self_cursor)
                    other_cursor = other._next(other_cursor)
            return True

    def bubblesorted(self):
        """Scrivere un generatore bubblesorted che ordina gli elementi della CircularPositionalList e
            li restituisce nell’ordine risultante. Il generatore non deve modificare l’ordine in cui sono
            memorizzati gli elementi nella lista."""
        self._check_sortability()               #O(n)
        array = list(self)                      #O(n)
        for i in range(self._size-1):
            modified = False                    #O(n)
            for j in range(self._size-i-1):
                if array[j] > array[j+1]:
                    temp = array[j]             #O(n^2)
                    array[j] = array[j+1]       #O(n^2)
                    array[j+1] = temp           #O(n^2)
                    modified = True             #O(n^2)
            if not modified:
                break
        for i in range(self._size):
            yield array[i]                      # O(n)
        #bubble sort: best case = O(n), worst case = O(n^2)
        #T(n) per restituire l'iter
        # complessità non accettabile T(n) + (T(n) al più T(n^2)) + T(n) = caso migliore T(n) caso perggiore T(n)+T(n^2)
        # versione rudimentale del bubble sort da migliorare in modo tale da ottenere la stessa complessità del bubble sort nel caso peggiore"""

    def merge(self, list2):
        """Scrivere una funzione merge che prende in input due CircularPositionalList ordinate
            e le fonde in una nuova CircularPositionalList ordinata."""
        if type(self) is not type(list2):
            raise TypeError("Lists to merge are not of the same type.")
        elif not (self.is_sorted() and list2.is_sorted()):
            raise ValueError("Lists to merge are not already sorted.")
        elif self.is_empty():
            return list2
        elif list2.is_empty():
            return self
        else:
            self_cursor = self.first()          #cursore per le position di self
            list2_cursor = list2.first()        #cursore per le position di list2
            self_counter = 0                    #counter per le position di self
            list2_counter = 0                   #counter per le position di list2
            new_list = CircularPositionalList()
            for i in range(self._size + list2._size):
                if self_cursor.element() < list2_cursor.element() and self_counter < self._size or list2_counter == list2._size:
                    """Aggiungi un elemento da self se è minore del primo elemento di list2 AND self non è finito
                        OR list2 è finito"""
                    new_list.add_last(self_cursor.element())
                    self_counter += 1
                    self_cursor = self._next(self_cursor)
                else:
                    """Altrimenti aggiungi un elemento da list2"""
                    new_list.add_last(list2_cursor.element())
                    list2_counter += 1
                    list2_cursor = list2._next(list2_cursor)
            return new_list
