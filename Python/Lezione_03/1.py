""" 1. Sistema di gestione per un parcheggio
Progetta un algoritmo per la gestione dell'ingresso e dell'uscita di veicoli da un parcheggio con un numero massimo di posti dato in input. L'utente può inserire una delle seguenti opzioni "ingresso", "uscita", "stato", "esci". Per ogni opzione:
    se l'utente inserisce "ingresso", verifica se ci sono posti disponibili, quindi incrementa il numero di posti occupati;
    se l'utente inserisce "uscita", verifica che ci siano veicoli nel parcheggio, quindi decrementa il numero di posti occupati;
    se l'utente inserisce "stato", mostra il numero dei posti liberi e il numero dei posti occupati;
    se l'utente inserisce "esci", termina l'algoritmo.
Torna all'inserimento di una opzione finché l'utente non seleziona "esci". """

posti_max = int(input("Inserire il numero massimo di posti: "))
posti_disp = 0

opzione = input(f"Selezionare un'opzione:\n'ingresso', 'uscita', 'stato', 'esci'\n")

if opzione == "ingresso":
    if posti_disp > 0:
        posti_disp -= 1
elif opzione == "uscita":
    if posti_disp < posti_max:
        posti_disp += 1
elif opzione == "stato":
    print(f"Posti liberi: {posti_disp}, Posti occupati: {posti_max - posti_disp}")
elif opzione == "esci":
    print("Grazie e arrivederci")
else:
    print("Opzione non valida")