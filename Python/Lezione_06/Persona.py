class Persona:

    '''
    Di una persona dobbiamo sapere delle informazioni.
    Queste informazioni vengono chiamate attributi (della classe Persona)
    Le informazoni saranno
    - nome
    - cognome
    - età

    Come li rappresento in python?

    self.name: str (attributo di tipo stringa)
    self.lastname (attributo di tipo stringa)
    self.age (attributo di tipo int)
    '''

# costruttore della classe persona
    def __init__(self, name, lastname, age):
        self.name = name
        self.lastname = lastname
        self.age = age

# funzione che mostri in output tutti i dati di una persona
    def displayData(self) -> None:
        print(f"Nome: {self.name}\nCognome: {self.lastname}\nEtà: {self.age}")

fm = Persona("Alessandro", "Ricci", 35)
print(fm)

# mostra i dati di una persona
fm.displayData()