from score_board import ScoreBoard
from circular_positional_list import CircularPositionalList, merge, bubblesorted
from datetime import date

"""Scrivere uno script verifica.py che testi tutte le funzionalità implementate.
In particolare se l_uno è una lista e l_due = l_uno.copy(), allora la stessa operazione
su entrambe le sequenze deve produrre lo stesso risultato."""

def test_default():
    #CircularPositionList Test
    l_uno = CircularPositionalList()
    print("\nLa lista è vuota?\t\t\t\t\t\t\t\t\t", l_uno.is_empty())
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
    for e in bubblesorted(l_uno):
        l_uno_ordinata.add_last(e)
    l_due_ordinata = CircularPositionalList()
    for e in bubblesorted(l_due):
        l_due_ordinata.add_last(e)
    print("Eseguo il bubblesort:\t\t\t\t\t\t\t\t", l_uno_ordinata)
    print("Le liste sono ordinate?\t\t\t\t\t\t\t\t", l_uno_ordinata.is_sorted() and l_due_ordinata.is_sorted())
    print("Allora eseguo il merge:\t\t\t\t\t\t\t\t", merge(l_uno_ordinata, l_due_ordinata))
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
    print("\nTest")
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
    print("------------------Test-Merge-----------------------\n")
    sb1_uno.merge(sb2_uno)
    print(str(sb1_uno))
    print("Si noti che dei 12 score totali ne prende i migliori 10")

def insert_score(sb):
    risp = 1
    while risp == 1:
        score = float(input("Inserisca lo score totalizzato:\n"))
        name = input("Inserisca il nome del player che ha totalizzato lo score:\n")
        print("Inserisca la data in cui è stato totalizzato lo score")
        Y = int(input("Anno:\n"))
        M = int(input("Mese:\n"))
        D = int(input("Giorno:\n"))
        sb.insert(ScoreBoard.Score(name, score, date(Y, M, D)))
        while True:
            risp = int(input("Vuole inserire un altro score?(1-yes or 2-no):\n"))
            if risp == 2 or risp == 1:
                break
            else:
                print("Scelta errata, ripeta")
    return sb

def create_score():
    dim = 0
    sb = ScoreBoard()
    while True:
        risp=int(input("Desidera creare uno Scoreboard di una opportuna dimensione?(1-yes or 2-no):\n"))
        if risp == 1:
            dim = input("Inserisca la dimensione che desidera impostare:\n")
            sb = ScoreBoard(int(dim))
            break
        elif risp == 2:
            print("ScoreBoard creato di dimensione 10")
            break
        else:
            print("Scelta errata, ripeta")
    return sb

print("------------------TEST-INTERATTIVO-------------------")

x = 0
exit = 0
while exit == 0:
    print("-----------------------------------------------------")
    print("\nCosa volete testare?\n")
    print("1-Circular Positional List\n")
    print("2-Score Board\n")
    print("3-Esegui default test\n")
    print("4-Termina test\n")
    print("-----------------------------------------------------")
    x = input("Scelga una delle opzioni:\n")
    print("-----------------------------------------------------")
    if int(x) == 1:
        l_1 = CircularPositionalList()
        while exit == 0:
            print("-----------------------------------------------------")
            print("\nTest Circular Positional List\n")
            print("1-Visualizza gli elementi della lista [print(str(list))]\n")
            print("2-Ottieni il primo elemento della lista [first()]\n")
            print("3-Ottieni l'ultimo elemento della lista [last(p)]\n")
            print("4-Ottieni il predecessore di un elemento[before(p)]\n")
            print("5-Ottieni il successore di un elemento  [after(p)]\n")
            print("6-Verifica se la lista è vuota [is_empty()]\n")
            print("7-Verifica se la lista è ordinata [is_sorted()]\n")
            print("8-Aggiungi in testa [add_first(e)]\n")
            print("9-Aggiungi in coda [add_last(e)]\n")
            print("10-Aggiungi prima di un elemento [add_before(p, e)]\n")
            print("11-Aggiungi dopo un elemento [add_after(p, e)]\n")
            print("12-Cerca un elemento nella lista [find(e)]\n")
            print("13-Sostituisci un elemento presente con uno nuovo [replace(p, e)]\n")
            print("14-Elimina un elemento dalla lista [delete(e)]\n")
            print("15-Elimina tutti gli elementi della lista [clear()]\n")
            print("16-Conta quante volte è presente nella lista un dato elemento [count(e)]\n")
            print("17-Inverti l'ordine degli elementi nella lista [reverse()]\n")
            print("18-Ottieni una copia della lista [copy()]\n")
            print("19-Add di due liste [x + y]\n")
            print("20-Verifica se una position è presente nella lista [ p in x]\n")
            print("21-Restituisce l'elemento contenuto nella position p [ x[p] ]\n")
            print("22-Restituisci il numero di elementi di x  [len(x)]\n")
            print("23-Sostituisci l'elemento di p con e [x[p] = e]\n")
            print("24-Rimuove l'elemento nella position p invalidando la position [del p]\n")
            print("25-Generatore degli elementi [__iter__]\n")
            print("26-Ritorna al passo precedente\n")
            print("27-Termina test\n")
            print("-----------------------------------------------------")
            x = input("Scegli una delle opzioni:\n")
            print("-----------------------------------------------------")
            if int(x) == 1:
                print(str(l_1))
            elif int(x) == 2:
                print("Il primo elemento della lista è: " + str(l_1.first().element()))
            elif int(x) == 3:
                print("L'ultimo elemento della lista è: " + str(l_1.last().element()))
            elif int(x) == 4:
                search = input("Di quale elemento vuole ottenere il predecessore:\n")
                print("Il predecessore di " + search + "è: " + str(l_1.before(l_1.find(int(search)))))
            elif int(x) == 5:
                search = input("Di quale elemento vuole ottenere il successore:\n")
                print("Il successore di " + search + "è: " + str(l_1.after(l_1.find(int(search)))))
            elif int(x) == 6:
                if l_1.is_empty():
                    print("La lista è vuota")
                else:
                    print("La lista non è vuota")
            elif int(x) == 7:
                if l_1.is_sorted():
                    print("La lista è ordinata")
                else:
                    print("La lista non è ordinata")
            elif int(x) == 8:
                risp = 1
                while risp == 1:
                    insert = input("Inserisci il valore da aggiungere in testa:\n")
                    print("Lista prima dell'inserimento: ", str(l_1))
                    l_1.add_first(int(insert))
                    print("Lista dopo l'inserimento: ", str(l_1))
                    while True:
                        risp = int(input("Vuole inserire un altro elemento?(1-yes or 2-no):\n"))
                        if risp == 2 or risp == 1:
                            break
                        else:
                            print("Scelta errata, ripeta")
            elif int(x) == 9:
                risp = 1
                while risp == 1:
                    insert = input("Inserisci il valore da aggiungere in coda:\n")
                    print("Lista prima dell'inserimento: ", str(l_1))
                    l_1.add_last(int(insert))
                    print("Lista dopo l'inserimento: ", str(l_1))
                    while True:
                        risp = int(input("Vuole inserire un altro elemento?(1-yes or 2-no):\n"))
                        if risp == 2 or risp == 1:
                            break
                        else:
                            print("Scelta errata, ripeta")
            elif int(x) == 10:
                risp = 1
                while risp == 1:
                    befor = input("Di chi prima vuole inserire un valore:\n")
                    insert = input("Inserisci il valore da aggiungere prima di " + befor + ":\n")
                    print("Lista prima dell'inserimento: ", str(l_1))
                    l_1.add_before(l_1.find(int(befor)), int(insert))
                    print("Lista dopo l'inserimento: ", str(l_1))
                    while True:
                        risp = int(input("Vuole inserire un altro elemento?(1-yes or 2-no):\n"))
                        if risp == 2 or risp == 1:
                            break
                        else:
                            print("Scelta errata, ripeta")
            elif int(x) == 11:
                risp = 1
                while risp == 1:
                    befor = input("Di chi dopo vuole inserire un valore:\n")
                    insert = input("Inserisci il valore da aggiungere dopo " + befor + ":\n")
                    print("Lista prima dell'inserimento: ", str(l_1))
                    l_1.add_after(l_1.find(int(befor)), int(insert))
                    print("Lista dopo l'inserimento: ", str(l_1))
                    while True:
                        risp = int(input("Vuole inserire un altro elemento?(1-yes or 2-no):\n"))
                        if risp == 2 or risp == 1:
                            break
                        else:
                            print("Scelta errata, ripeta")
            elif int(x) == 12:
                risp = 1
                while risp == 1:
                    search = input("Quale elemento vuole cercare:\n")
                    print("L'elemento " + str(l_1.find(int(search)).element()) + "è presente e la sua position è: " + str(l_1.find(int(search))) + "\n")
                    while True:
                        risp = int(input("Vuole cercare un altro elemento?(1-yes or 2-no):\n"))
                        if risp == 2 or risp == 1:
                            break
                        else:
                            print("Scelta errata, ripeta")
            elif int(x) == 13:
                risp = 1
                while risp == 1:
                    p = input("Quale elemento vuole aggiornare:\n")
                    e = input("Qual'e' l'elemento che vuole inserire:\n")
                    print("Lista prima dell'aggiornamento: ", str(l_1))
                    print("\nL'elemento "+ str(l_1.replace(l_1.find(int(p)), int(e))) + "è stato aggiornato al nuovo valore\n")
                    print("Lista dopo dell'aggiornamento: ", str(l_1))
                    while True:
                        risp = int(input("Vuole aggiornare un altro elemento?(1-yes or 2-no):\n"))
                        if risp == 2 or risp == 1:
                            break
                        else:
                            print("Scelta errata, ripeta")
            elif int(x) == 14:
                risp = 1
                while risp == 1:
                    e = input("Quale elemento vuole eliminare:\n")
                    print("Lista prima dell'eliminazione: ", str(l_1))
                    print("\nL'elemento "+ str(l_1.delete(l_1.find(int(e)))) + "è stato eliminato\n")
                    print("Lista dopo dell'aggiornamento: ", str(l_1))
                    while True:
                        risp = int(input("Vuole eliminare un altro elemento?(1-yes or 2-no):\n"))
                        if risp == 2 or risp == 1:
                            break
                        else:
                            print("Scelta errata, ripeta")

            elif int(x) == 15:
                print("Lista prima della pulizia: ", str(l_1))
                l_1.clear()
                print("Lista dopo la pulizia: ", str(l_1))
            elif int(x) == 16:
                counter = input("Di quale elemento vuole trovare il numero di occorrenze nella lista:\n")
                print("L'elemento è presente " + str(l_1.count(int(counter))) + " volte nella lista")
            elif int(x) == 17:
                print("Lista prima dell'inversione: ", str(l_1))
                l_1.reverse()
                print("Lista dopo l'inversione: ", str(l_1))
            elif int(x) == 18:
                copy = l_1.copy()
                print("Lista: ",str(l_1))
                print("Copia della lista: ",str(copy))
                print("\nMINI TEST sulla correttezza della copia:")
                print("ELiminerò il primo elemento della copia della lista ")
                print("per verificare che una semplice modifica sulla copia ")
                print("della lista non apporta modifiche sulla lista di cui \n"+"si è effettuati la copia ")
                copy.delete(copy.first())
                print("Lista di cui si è effettuata una copia: ", str(l_1))
                print("Copia della lista dopo la modifica: ", str(copy))
            elif int(x) == 19:
                print("Le serve un altra lista per sommarla alla precedente")
                while True:
                    r = int(input("Vuole creare una nuova copia della lista per sommarla o vuole crearne una nuova?(1-copia or 2-nuova):\n"))
                    if r == 2 or r == 1:
                        break
                    else:
                        print("Scelta errata, ripeta")
                if r == 1:
                    copy = l_1.copy()
                    print("Lista iniziale: " + str(l_1))
                    print("Copia della lista: " + str(copy))
                    print(" x + y (Lista iniziale + Copia) = " + str(l_1+copy))
                else:
                    l_2 = CircularPositionalList()
                    while True:
                        risp = int(input("Vuole inserire un elemento in coda , in testa o non vuole inserire nessun altro valore?(1-coda or 2-testa or 3-Non voglio più inserire):\n"))
                        if risp == 1:
                            insert = input("Inserisci il valore da aggiungere in coda:\n")
                            print("Lista prima dell'inserimento: ", str(l_2))
                            l_2.add_last(int(insert))
                            print("Lista dopo l'inserimento: ", str(l_2))
                        elif risp == 2:
                            insert = input("Inserisci il valore da aggiungere in testa:\n")
                            print("Lista prima dell'inserimento: ", str(l_2))
                            l_2.add_first(int(insert))
                            print("Lista dopo l'inserimento: ", str(l_2))
                        elif risp == 3:
                            break
                        else:
                            print("Scelta errata, ripeta")
                    print("Lista iniziale: " + str(l_1))
                    print("Secodan lista: " + str(l_2))
                    print(" x + y (Lista iniziale + Seconda lista) = " + str(l_1+l_2))
            elif int(x) == 20:
                print("Mini Test")
                l_2 = CircularPositionalList()
                l_2.add_first(57)
                l_2.add_first(43)
                l_2.add_first(9)
                l_2.add_first(11)
                l_2.add_first(2)
                print("Ho questa lista: " + str(l_2))
                print("Verifico se p di 57 è presente nella lista")
                if l_2.find(57) in l_2:
                    print("p di 57 è presente in lista")
                print("Verifico se p di 100 è presente nella lista")
                if not ((l_2.find(100) != None) in l_2):
                    print("p di 100 non è presente in lista")
            elif int(x) == 21:
                print("Mini Test")
                l_2 = CircularPositionalList()
                l_2.add_first(57)
                l_2.add_first(43)
                l_2.add_first(9)
                l_2.add_first(11)
                l_2.add_first(2)
                print("Ho questa lista: " + str(l_2))
                print("L'elemento associato alla position dell'ultimo elemento della lista è: ", str(l_2[l_2.last()]))
            elif int(x) == 22:
                print("Mini Test")
                l_2 = CircularPositionalList()
                l_2.add_first(57)
                l_2.add_first(43)
                l_2.add_first(9)
                l_2.add_first(11)
                l_2.add_first(2)
                print("Ho questa lista: " + str(l_2))
                print("Il numero di elementi della lista è: ", str(len(l_2)))
            elif int(x) == 23:
                print("Mini Test")
                l_2 = CircularPositionalList()
                l_2.add_first(57)
                l_2.add_first(43)
                l_2.add_first(9)
                l_2.add_first(11)
                l_2.add_first(2)
                print("Ho questa lista: " + str(l_2))
                print("Sostituisco nella position di 57 il proprio elemento con 100 ")
                l_2[l_2.find(57)] = 100
                print("Lista dopo la sostituzione è: ", str(l_2))
            elif int(x) == 24:
                print("Mini Test")
                l_2 = CircularPositionalList()
                l_2.add_first(57)
                l_2.add_first(43)
                l_2.add_first(9)
                l_2.add_first(11)
                l_2.add_first(2)
                print("Ho questa lista: " + str(l_2))
                print("Elimino il primo elemento della lista")
                del l_2[l_2.first()]
                print("Lista dopo l'eliminazione è: ", str(l_2))
            elif int(x) == 25:
                print("Mini Test")
                l_2 = CircularPositionalList()
                l_2.add_first(57)
                l_2.add_first(43)
                l_2.add_first(9)
                l_2.add_first(11)
                l_2.add_first(2)
                print("Ho questa lista: " + str(l_2))
                print("Scorro la lista attraverso l'iteratore")
                k = 1
                for i in l_2:
                    print(str(k) +  "°: " +str(i))
                    k +=1
            elif int(x) == 26:
                break
            elif int(x) == 27:
                exit = 1
            else:
                print("Scelta errata, ripeta")
    elif int(x) == 2:
        while exit == 0:
            print("\nTest ScoreBoard\n")
            print("1-Crea uno ScoreBorad \n")
            print("2-Ritorna al passo precedente\n")
            print("3-Termina test\n")
            print("-----------------------------------------------------")
            x = input("Scelga una delle opzioni:\n")
            print("-----------------------------------------------------")
            if int(x) == 1:
                dim = 0
                sc_1 = create_score()
                while exit == 0:
                    print("\nTest ScoreBoard(Dimensione ScoreBoard " + str(len(sc_1)) +")\n")
                    print("1-Ottieni la dimensione dello score\n")
                    print("2-Ottieni il numero di elementi presenti\n")
                    print("3-Verifica se la lista è vuota\n")
                    print("4-Inserisci uno score nello ScoreBoard\n")
                    print("5-Restituisci gli x migliori Score dello ScoreBoard\n")
                    print("6-Restituisci gli x peggiori Score dello ScoreBoard\n")
                    print("7-Testa la funzione merge di questo Scoreboard\n")
                    print("8-Visualizza elementi memorizzati nello ScoreBoard\n")
                    print("9-Ritorna al passo precedente\n")
                    print("10-Termina test\n")
                    print("-----------------------------------------------------")
                    x = input("Scelga una delle opzioni:\n")
                    print("-----------------------------------------------------")
                    if int(x) == 1:
                        print("La dimensione dello ScoreBoard è: ",len(sc_1))
                    elif int(x) == 2:
                        print("Il numero di Score presenti nello ScoreBoard è: ",sc_1.size())
                    elif int(x) == 3:
                        if sc_1.is_empty():
                            print("Lo ScoreBoard è vuoto")
                        else:
                            print("Lo ScoreBoard non è vuoto")
                    elif int(x) == 4:
                        sc_1 = insert_score(sc_1)
                    elif int(x) == 5:
                        i = int(input("Mi dica quanti x migliori risultati vuole visualizzare:\n"))
                        k = 1
                        for i in sc_1.top(i):
                            print(str(k) + "°  \t" + str(i))
                            k += 1
                    elif int(x) == 6:
                        i = int(input("Mi dica quanti x peggiori risultati vuole visualizzare:\n"))
                        k = 1
                        for i in sc_1.last(i):
                            print(str(k) + "°  \t" + str(i))
                            k += 1
                    elif int(x) == 7:
                        print("Le serve un altro ScoreBoard da fondere al precedente Scoreboard\n")
                        sc_2 = create_score()
                        sc_2 = insert_score(sc_2)
                        print(sc_1)
                        print(sc_2)
                        print("------------------Test-Merge-----------------------\n")
                        sc_1.merge(sc_2)
                        print(str(sc_1))
                    elif int(x) == 8:
                        print(sc_1)
                    elif int(x) == 9:
                        break
                    elif int(x) == 10:
                        exit = 1
                    else:
                        print("Scelta errata, ripeta")
            elif int(x) == 2:
                break
            elif int(x) == 3:
                exit = 1
            else:
                print("Scelta errata, ripeta")
    elif int(x) == 3:
        test_default()
    elif int(x) == 4:
        exit = 1
    else:
        print("Scelta errata, ripeta")