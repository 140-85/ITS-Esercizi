''' Esercizio 3C-5. Scrivere un programma in Python che memorizzi il nome, il ruolo e l'età di un utente in un dizionario. Il nome, il ruolo e l'età devono essere inseriti in input dall'utente stesso. Il programma deve determinare il livello di accesso ai servizi in base al ruolo e all'età dell'utente secondo questo schema:
- Admin → "Accesso completo a tutte le funzionalità."
- Moderatore → "Può gestire i contenuti ma non modificare le impostazioni."
- Utente adulto (età ≥ 18) → "Accesso standard a tutti i servizi."
- Utente minorenne (età < 18) → "Accesso limitato! Alcune funzionalità sono bloccate."
- Ospite → "Accesso ristretto! Solo visualizzazione dei contenuti."
- Ruolo non riconosciuto → "Attenzione! Ruolo non riconsciuto! Accesso Negato!" '''

def main():

    nome = input("Digitare nome dell'utente: ")
    ruolo = input("Digitare ruolo dell'utente: ")
    eta = int(input("Digitare l'età dell'utente: "))

    utente = {"nome": nome, "ruolo": ruolo, "eta": eta}

    match ruolo:
        case "admin":
            print("Accesso completo a tutte le funzionalità.")
        case "moderatore":
            print("Può gestire i contenuti ma non modificare le impostazioni.")
        case _ if eta >= 18:
            print("Accesso standard a tutti i servizi.")
        case _ if eta < 18:
            print("Accesso limitato! Alcune funzionalità sono bloccate.")
        case "ospite":
            print("Accesso ristretto! Solo visualizzazione dei contenuti.")
        case _:
            print("Attenzione! Ruolo non riconosciuto! Accesso Negato!")

if __name__ == "__main__":
    main()