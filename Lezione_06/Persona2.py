class Persona:
    def __init__(self):
        self.name = ""
        self.lastname = ""
        self.age = 0
    
    def displayData(self) -> None:
        print(f"Nome: {self.name}\nCognome: {self.lastname}\nEtà: {self.age}")
    
# mi consente di impostare un valore per self.name
    def setName(self, name:str) -> None:
        self.name = name
    
# mi consente di impostare un valore per self.lastname
    def setLastname(self, lastname:str) -> None:
        self.lastname = lastname

# mi consente di impostare un valore per self.age
    def setAge(self, age:int) -> None:
        if age < 0 or age > 130:
            self.age = 0
        else:
            self.age = age

# ritorna il valore di self.name
    def getName(self) -> str:
        return self.name
    
# ritorna il valore di self.lastname
    def getLastname(self) -> str:
        return self.lastname
    
# ritorna il valore di self.age
    def getAge(self) -> int:
        return self.age

fm:Persona = Persona()
fm.displayData()
fm.setName("Alessandro")
fm.setLastname("Ricci")
fm.setAge(35)
fm.displayData()

print(fm.getName(), fm.getLastname(), fm.getAge())