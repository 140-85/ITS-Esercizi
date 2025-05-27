""" 2. Automazione di un semaforo intelligente
Progettare un algoritmo che simuli il comportamento di un semaforo intelligente. Questo sistema deve adattare i tempi di durata (espressi in percentuale) del verde in base al numero di veicoli presenti sulle principali direzioni di traffico: Nord-Sud ed Est-Ovest. Ogni direzione può ricevere una priorità se il numero di veicoli supera una soglia predefinita.
Requisiti:
    Se il numero di veicoli in una sola direzione supera la soglia (es. 70 veicoli), quella direzione riceve un tempo minimo garantito per il verde (es. 60%) e il restante tempo è assegnato all'altra direzione.
    Se entrambe le direzioni superano la soglia, il tempo è equamente suddiviso (50% per ciascuna direzione).
    Se nessuna direzione supera la soglia, il tempo è calcolato proporzionalmente al numero totale di veicoli nelle due direzioni.
Stampare la percentuale del tempo assegnato al verde per ciascuna direzione. """

soglia = int(input("Inserire un valore soglia: "))
ns = int(input("Inserire il numero di veicoli presenti in direzione Nord-Sud: "))
eo = int(input("Inserire il numero di veicoli presenti in direzione Est-Ovest: "))
verde = int(input("Inserire un valore priorità: "))

if ns > soglia and eo < soglia:
    t_ns = verde
    t_eo = 100 - verde
elif ns < soglia and eo > soglia:
    t_eo = verde
    t_ns = 100 - verde
elif ns and eo > soglia:
        t_ns, t_eo = 50
elif ns and eo <= soglia:
        t_ns = ns / (ns + eo) * 100
        t_eo = 100 - t_ns

print(t_ns, t_eo)