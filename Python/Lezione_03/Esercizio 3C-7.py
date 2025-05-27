''' Esercizio 3C-7. Si scriva un programma in python che computi la statistica di otto lanci di una moneta.
Per ciascuno dei lanci effettuati, l'utente inserisce "t" o "T" se è uscito "testa", mentre inserisce "c" o "C" se è uscito "croce".
Il programma deve mostrare in output il numero totale e la percentuale dei risultati "testa" e "croce".
NOTA.
Le percentuali devono essere mostrate in output obbligatoriamente con 2 cifre decimali.
Usare il match statement.
Expected Output:
Per ciascun lancio della moneta inserisci "t" o "T" se e' uscito "testa" mentre inserisci "c" o "C" se e' uscito "croce".
Lancio 1: t
Lancio 2: c
Lancio 3: t
Lancio 4: t
Lancio 5: c
Lancio 6: c
Lancio 7: t
Lancio 8: t
Totale "testa": 5
Percentaule "testa": 62.50%
Totale "croce": 3
Percentuale "croce": 37.50% '''

cont_testa = 0
cont_croce = 0

print("Inserire t oppure c")
    
for i in range(1, 9):
    risultato = input(f"Lancio {i}: ")
    match risultato:
        case "t"|"T":
            cont_testa += 1
        case "c"|"C":
            cont_croce += 1
        case _:
            print("Inserire t oppure c")

testa_percent = cont_testa / 8 * 100
croce_percent = cont_croce / 8 * 100

print(f"Totale 'testa': {cont_testa}")
print(f"Percentuale 'testa': {testa_percent:.2f}%")
print(f"Totale 'croce': {cont_croce}")
print(f"Percentuale 'croce': {croce_percent:.2f}%")