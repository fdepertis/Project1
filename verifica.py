from circular_positional_list import CircularPositionalList
from score_board import ScoreBoard

"""Scrivere uno script verifica.py che testi tutte le funzionalità implementate.
In particolare se l_uno è una lista e l_due = l_uno.copy(), allora la stessa operazione
su entrambe le sequenze deve produrre lo stesso risultato."""

#CircularPositionList Test
l_uno = CircularPositionalList()
print("La lista è vuota?\t\t\t\t\t\t\t\t\t", l_uno.is_empty())
l_uno.add_first(11)
print("Aggiungo il primo elemento 11:\t\t\t\t\t\t", l_uno)
print("La lista è vuota ora?\t\t\t\t\t\t\t\t", l_uno.is_empty())
l_uno.add_last(13)
print("Aggiungo un secondo elemento 13 in coda:\t\t\t", l_uno)
l_uno.add_after(l_uno.first(), 17)
print("Aggiungo un terzo elemento 17 dopo il primo:\t\t", l_uno)
l_uno.add_before(l_uno.last(), 19)
print("Aggiungo un quarto elemento 19 prima dell'ultimo:\t", l_uno)
l_uno.add_after(l_uno.last(), 23)
print("Aggiungo un quinto elemento 23 dopo l'ultimo:\t\t", l_uno)
print("Qual è la dimensione della lista?\t\t\t\t\t", len(l_uno))
print("La lista è circolare?\t\t\t\t\t\t\t\t", l_uno.first().element() == l_uno.after(l_uno.last()) and l_uno.last().element() == l_uno.before(l_uno.first()))
l_uno.delete(l_uno.find(13))
print("Elimino 13 dalla lista:\t\t\t\t\t\t\t\t", l_uno)
l_uno.replace(l_uno.find(17), 29)
print("Sostituisco 17 con 29:\t\t\t\t\t\t\t\t", l_uno)
l_uno.add_last(11)
print("Aggiungo un altro 11 in coda:\t\t\t\t\t\t", l_uno)
print("Quanti 11 ci sono nella lista?\t\t\t\t\t\t", l_uno.count(11))
print("Quanti 12 ci sono nella lista?\t\t\t\t\t\t", l_uno.count(12))
l_uno.add_first(31)
print("Aggiungo un altro elemento 31 in testa:\t\t\t\t", l_uno)
print("Chi è l'header ora?\t\t\t\t\t\t\t\t\t", l_uno[l_uno.first()])
l_uno.reverse()
print("Inverto la lista:\t\t\t\t\t\t\t\t\t", l_uno)
l_uno[l_uno.last()] = 37
print("Sostituisco l'ultimo elemento 31 con 37:\t\t\t", l_uno)
l_due = l_uno.copy()
print("Copio la lista l_uno in l_due:\t\t\t\t\t\t", l_due)
print("Sono uguali?\t\t\t\t\t\t\t\t\t\t", l_uno == l_due)
del l_uno[l_uno.first()]
del l_due[l_due.first()]
print("Elimino il primo elemento da entrambe le liste:\t\t", l_uno)
print("Sono ancora uguali?\t\t\t\t\t\t\t\t\t", l_uno == l_due)
print("Concateno le liste:\t\t\t\t\t\t\t\t\t", l_uno + l_due)
l_uno.add_before(l_uno.first(), 41)
l_due.add_before(l_due.first(), 41)
l_uno.add_after(l_uno.last(), 43)
l_due.add_after(l_due.last(), 43)
print("Aggiungo 41 e 43 in entrambe:\t\t\t\t\t\t", l_uno)
print("Sono ancora uguali?\t\t\t\t\t\t\t\t\t", l_uno == l_due)

print("Le liste sono ordinate?\t\t\t\t\t\t\t\t", l_uno.is_sorted() and l_due.is_sorted())
l_uno_ordinata = CircularPositionalList()
for e in l_uno.bubblesorted():
    l_uno_ordinata.add_last(e)
l_due_ordinata = CircularPositionalList()
for e in l_due.bubblesorted():
    l_due_ordinata.add_last(e)
print("Eseguo il bubblesort:\t\t\t\t\t\t\t\t", l_uno_ordinata)
print("Le liste sono ordinate?\t\t\t\t\t\t\t\t", l_uno_ordinata.is_sorted() and l_due_ordinata.is_sorted())
print("Allora eseguo il merge:\t\t\t\t\t\t\t\t", l_uno_ordinata.merge(l_due_ordinata))
l_uno.clear()
l_due.clear()
l_uno_ordinata.clear()
l_due_ordinata.clear()
print("Svuoto le liste:", l_uno + l_due + l_uno_ordinata + l_due_ordinata)