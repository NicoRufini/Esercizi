class Persona:
    def __init__(self, name: str, surname: str, data_di_nascita: str, gender: str, codice_fiscale: str) -> None:
        #Il "_" a "self._name = name" è una convenzione per indicare che la varibile deve rimanere privata
        self.name = name
        self.surname = surname
        self.data_di_nascita = data_di_nascita
        self.gender = gender
        self.codice_fiscale = codice_fiscale

    def calcola_eta(self) -> int:
        return 10

    def __eq__(self, value: object) -> bool:
        return value.codice_fiscale == self.codice_fiscale

class Dipendent(Persona):
    def __init__(self, name: str, surname: str, data_di_nascita: str, gender: str, ore_lavorate: int) -> None:
        super().__init__(name, surname, data_di_nascita, gender)
        self.ore_lavorate = ore_lavorate

    def calcola_stipendio(self) -> float:
        return 500.0
    

class Professor(Dipendent):
    def __init__(self, name: str, surname: str, data_di_nascita: str, gender: str, ore_lavorate: int, materia_insegnata: str, ore_di_lezione: int) -> None:
        super().__init__(name, surname, data_di_nascita, gender, ore_lavorate)
        self.materia_insegnata = materia_insegnata
        self.ore_di_lezione = ore_di_lezione

    def __str__(self) -> str:
        return f"My name is {self.name}"

professore_1 = Professor("Nicolò", "Rufini", "7/5/2003", "Maschio", 500, "Python", 1000)
print(professore_1.ore_di_lezione)
print(professore_1)

dipendente_1 = Dipendent("Nicolò", "Rufini", "7/5/2003", "Maschio", 500)
print(dipendente_1.name)
print(dipendente_1.ore_lavorate)

persona_1 = Persona("Nicolò", "Rufini", "7/5/2003", "Maschio")
print(persona_1.calcola_eta())