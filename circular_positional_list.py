from TdP_collections.list.positional_list import PositionalList
import time

class CircularPositionalList(PositionalList):

    def __init__(self):
        """Create an empty list."""
        self._header = self._Node(None, None, None)
        self._size = 0

    #-------------------------- Private-methods---------------------------

    def _make_position(self, node):
        """Ritorna la Position del nodo dato"""
        return self.Position(self, node)

    def _set_header(self, e):
        """Metodo privato utilizzato da add_first e add_last per settare il primo elemento della lista"""
        self._header = self._Node(e, self._header, self._header)
        self._header._next = self._header
        self._header._prev = self._header
        self._size = 1
        return self._make_position(self._header)

   #----------------------------Public-Methods----------------------------

    def first(self):
        """Restituisce la Position dell’elemento che è identificato
            come il primo oppure None se la lista è vuota"""
        if self.is_empty():
            return None
        return self._make_position(self._header)

    def last(self):
        """Restituisce la Position dell'elemento che è identificato
            come l'ultimo oppure None se la lista è vuota"""
        if self.is_empty():
            return None
        return self._make_position(self._header._prev)

    def before(self,p):
        """Restituisce l'elemento nella Position precedente a p, None se p non ha un predecessore e
            ValueError se p non è una position della lista"""
        if self.is_empty():
            return None
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self,p):
        """Restituisce l'elemento nella Position p successiva a p, None se p non ha un successore e
            ValueError se p non è una position della lista"""
        if self.is_empty():
            return None
        node = self._validate(p)
        return self._make_position(node._next)

    def is_empty(self):
        """Restituisce True se la lista è vuota altrimenti False"""
        return self._size == 0

    def is_sorted(self):
        """Restituisce True se la lista è ordinata e False altrimenti.
            Si definisce ordinata una lista ordinata i cui elementi sono tutti dello stesso tipo
            e sono disposti in ordine crescente a partire dall'header"""
        cursor = self.first()
        for i in range(self._size - 1):
            if type(cursor.element()) is not type(self.after(cursor).element()) or cursor.element() > self.after(cursor).element():
                return False
            else:
                cursor = self.after(cursor)
        return True

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
        for i in range(self._size):
            if cursor.element() == e:
                return cursor
            else:
                cursor = self.after(cursor)
        return None

    def replace(self, p, e):
        """Sostituisce l'elemento in Position p con l'elemento e e restituisce il vecchio elemento"""
        return super().replace(p ,e)

    def delete(self, p):
        """Rimuove e restituisce l'elemento in Position p dalla lista e invalida p"""
        if p == self.first() and self._size > 1:
            self._header = self._header._next
        return super().delete(p)

    def clear(self):
        """Rimuove tutti gli elementi della lista invalidando le corrispondeti position"""
        cursor = self.last()
        for i in range(self._size):
            next_cursor = self.before(cursor)
            self.delete(cursor)
            cursor = next_cursor

    def count(self, e):
        """Restituisce il numero di occorrenze di e nella lista"""
        counter=0
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
            left_cursor._node._element=right_cursor.element()
            left_cursor=self.after(left_cursor)
            right_cursor= copy.before(right_cursor)

    def copy(self):
        """Restituisce una nuova CircularPositionalList che contiene gli stessi elementi
            della lista corrente memorizzati nello stesso ordine"""
        new_list = CircularPositionalList()
        for e in self.__iter__():
            new_list.add_last(e)
        return new_list

    #--------------------------Operators---------------------------------

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

    def __iadd__(self, other):
        if type(other) is not CircularPositionalList:
            raise TypeError("The second operand is not a cascaded CircularPositionList")
        for e in other.__iter__():
            self.add_last(e)
        return self

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

    def __delitem__(self, key):
        """Rimuove l’elemento nella position p invalidando la position"""
        self.delete(key)

    def __delitem__(self, key):
        """Rimuove l’elemento nella position p invalidando la position"""
        self.delete(key)
        key._node = None
        key._container = None

    def __iter__(self):
        """Generatore che restituisce gli elementi della lista a partire da quello che è
            identificato come primo fino a quello che è identificato come ultimo"""
        cursor = self.first()
        for i in range(self._size):
            yield cursor.element()
            cursor = self.after(cursor)

    def __str__(self):
        """Rappresenta il contenuto della lista come una sequenza di elementi,
            separati da virgole, partendo da quello che è identificato come primo
        :return:
        """
        s = ""
        for e in self.__iter__():
            s += str(e) + ", "
        #s += "\nSize: " + str(self._size) + "\nFirst: " + str(self.first()) + "\nLast:  " + str(self.last()) + "\n"
        return s

    def greater(self, i, j):
        if i._element > j._element:
            return True
        else:
            return False

    def swap(self, i, j):
        """

        :param i:
        :param j:
        :return:
        """
        tmp=i.element()
        self.replace(i,j.element())
        self.replace(j,tmp)

    def bubble_sorted(self):
        """Scrivere un generatore bubblesorted che ordina gli elementi della CircularPositionalList e
            li restituisce nell’ordine risultante. Il generatore non deve modificare l’ordine in cui sono
            memorizzati gli elementi nella lista.
        :return: sorted copy of list
        """
        self_copy=self.copy() #T(n)
        tmp = self_copy.first()
        cursor_k = self_copy.first()
        cursor_i = self_copy.first()
        print("---------------")
        for k in range(self_copy._size-1):
            modified=False
            for i in range(self_copy._size-k-1):
                if self.greater(cursor_i._node,cursor_i._node._next):
                    self_copy.swap(self_copy._make_position(cursor_i._node),self_copy._make_position(cursor_i._node._next))
                    modified=True
                cursor_i = self_copy.after(cursor_i)
            cursor_i = tmp
            cursor_k = self_copy.after(cursor_k)
            if modified == False:
                break
        #bubble sort best_case = T(n) worst_case=T(n^2)
        return self_copy

    def generator_bubble_sort(self):
        """

        :return:
        """
        cursor = self.first()
        for j in range(self._size):
            yield cursor
            cursor = self.after(cursor)
        #T(n) per restituire l'iter
        # complessità non accettabile T(n) + (T(n) al più T(n^2)) + T(n) = caso migliore T(n) caso perggiore T(n)+T(n^2)
        #versione rudimentale del bubble sort da migliorare in modo tale da ottenere la stessa complessità del bubble sort nel caso peggiore

    def merge(self,list):
        """Scrivere una funzione merge che prende in input due CircularPositionalList ordinate e le
            fonde in una nuova CircularPositionalList ordinata.
        :param list:
        :return:
        """
        if self.is_empty() and list.is_empty:
            return CircularPositionalList()
        elif self.is_empty():
            return list
        elif list.is_empty():
            return self
        elif self.last().element() < list.first().element():
            return self+list
        elif list.last().element() < self.first().element():
            return  list+self
        else:
            self_cursor = self.first()
            list_cursor = list.first()
            return_list = CircularPositionalList()
            while True:
                if self_cursor == self.last() and list_cursor == list.last():
                    if self_cursor.element() <= list_cursor.element():
                        return_list.add_last(self_cursor.element())
                        return_list.add_last(list_cursor.element())
                    elif self_cursor.element() < list_cursor.element():
                        return_list.add_last(list_cursor.element())
                        return_list.add_last(self_cursor.element())
                    break

                if self_cursor.element() < list_cursor.element() and self_cursor != self.last():
                    return_list.add_last(self_cursor.element())
                    self_cursor = self.after(self_cursor)
                elif self_cursor.element() > list_cursor.element() and list_cursor != list.last():
                    return_list.add_last(list_cursor.element())
                    list_cursor = list.after(list_cursor)
                else:
                    if self_cursor != self.last():
                        return_list.add_last(self_cursor.element())
                        self_cursor = self.after(self_cursor)
                    if list_cursor != list.last():
                        return_list.add_last(list_cursor.element())
                        list_cursor = list.after(list_cursor)
                time.sleep(1)
        return return_list











