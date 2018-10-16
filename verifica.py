from score_board import ScoreBoard
from circular_positional_list import CircularPositionalList

from datetime import date

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

print("\nIL TEST E' STATO EFFETTUATO SUL GIOCO DEI 100m QUINDI PER MIGLIORI RISULTATI DEL GIOCO INTENDIAMO IL MIGLIOR TEMPO TOTALIZZATO")
sb_uno = ScoreBoard()
if sb_uno.is_empty():
    print("La classifica è vuota")
print("Dimensione dello ScoreBoard",len(sb_uno))
print("Inserisco score di Usain Bolt")
sb_uno.insert(ScoreBoard.Score("Usain Bolt  ", 9.58, date(2009, 8, 16)))
print("Numero di score presenti",sb_uno.size())
if not sb_uno.is_empty():
    print("La classifica non è vuota")
print("Inserisco score di Yohan blake")
sb_uno.insert(ScoreBoard.Score("Yohan Blake ", 9.69, date(2012, 8, 23)))
print("Numero di score presenti",sb_uno.size())
sb_uno.insert(ScoreBoard.Score("Tyson Gay   ", 9.71, date(2009, 8, 16)))
sb_uno.insert(ScoreBoard.Score("Usain Bolt  ", 9.72, date(2008, 5, 31)))
sb_uno.insert(ScoreBoard.Score("Usain Bolt  ", 9.63, date(2012, 8, 5)))
sb_uno.insert(ScoreBoard.Score("Asafa Powell", 9.74, date(2007, 9, 9)))
sb_uno.insert(ScoreBoard.Score("Usain Bolt  ", 9.69, date(2008, 8, 16)))
sb_uno.insert(ScoreBoard.Score("Tyson Gay   ", 9.69, date(2009, 9, 20)))
sb_uno.insert(ScoreBoard.Score("Asafa Powell", 9.72, date(2008, 9, 2)))
print("Inserisco score di Yohan blake dopo aver inserito 8 score precedenti")
sb_uno.insert(ScoreBoard.Score("Yohan Blake ", 9.75, date(2012, 6, 29)))
print("Numero di score presenti",sb_uno.size())
print(str(sb_uno))
print("Aggiorno la classifica")
print("Inserisco nuovo score 9.74 s totalizzato da Justin Gatlin\n")
sb_uno.insert(ScoreBoard.Score("Justin Gatlin", 9.74, date(2015, 5, 15)))
print(str(sb_uno))
print("Si noti che la classifica è stata aggiornata e Justin Gatlin si è piazzato alle spalle di Yohan Blake nella top 10\n")
print("Si noti anche che di default la classifica può contenere solo i migliori 10 score e di conseguenza lo score di 9.75 s totalizzato da Yohan Blake è stato eliminato")
print("Provo a inserire di nuovo il vecchio punteggio di yohan blake\n ")
sb_uno.insert(ScoreBoard.Score("Yohan Blake ", 9.75, date(2012, 6, 29)))
print(str(sb_uno))
print("Si noti che la classifica non è stata aggiornata siccome lo score inserito non è migliore di quelli presenti ")
print("Seleziono solo i primi 3 della top 10\n")
print("TOP 3")
print("----\t-----------\t\t\t-----\t\t-----------\n||||\tPlayer Name\t\t\tScore\t\tDate\n----\t-----------\t\t\t-----\t\t-----------")
k = 1
for i in sb_uno.top(3):
    print(str(k) + "°  \t" + str(i))
    k += 1
print("\nSeleziono solo i peggiori 3 della top 10\n")
print("WORST 3")
print("----\t-----------\t\t\t-----\t\t-----------\n||||\tPlayer Name\t\t\tScore\t\tDate\n----\t-----------\t\t\t-----\t\t-----------")
k = 1
for n in sb_uno.last(3):
    print(str(k) + "°  \t" + str(n))
    k += 1

print("Test")
sb1_uno = ScoreBoard(4)
sb2_uno = ScoreBoard(9)

sb1_uno.insert(ScoreBoard.Score("Florence D. ", 10.49, date(1988, 7, 16)))
sb1_uno.insert(ScoreBoard.Score("Marion Jones", 10.65, date(1998, 9, 12)))
sb1_uno.insert(ScoreBoard.Score("Carmelita J.", 10.67, date(2009, 9, 13)))
sb1_uno.insert(ScoreBoard.Score("Elaine T.   ", 10.70, date(2016, 7, 1)))

sb2_uno.insert(ScoreBoard.Score("Florence D. ", 10.61, date(1988, 7, 17)))
sb2_uno.insert(ScoreBoard.Score("Florence D. ", 10.62, date(1988, 9, 24)))
sb2_uno.insert(ScoreBoard.Score("Florence D. ", 10.70, date(1988, 7, 17)))
sb2_uno.insert(ScoreBoard.Score("Marion Jones", 10.71, date(1998, 5, 12)))
sb2_uno.insert(ScoreBoard.Score("Shelly-Ann  ", 10.70, date(2012, 6, 29)))
sb2_uno.insert(ScoreBoard.Score("Carmelita J.", 10.64, date(2009, 9, 20)))
sb2_uno.insert(ScoreBoard.Score("Marion Jones", 10.65, date(1998, 9, 12)))
sb2_uno.insert(ScoreBoard.Score("Marion Jones", 10.70, date(1999, 8, 22)))


print(sb1_uno)
print(sb2_uno)
print("--------------Test-Merge------------------\n")
print(str(sb1_uno.merge(sb2_uno)))
print("Si noti che dei 12 score totali ne prende i migliori 10")

