'''
Gestione sistema ospedaliero

### CLASSE: Paziente
Creare un file chiamato "paziente.py".
In tale file, creare una classe chiamata Paziente. Si derivi Paziente dalla classe Persona.

Un paziente ha un nome, un cognome, un età, definiti dalla classe Persona ed un codice identificativo (si usi il tipo String).
- Definire i seguenti metodi:

    costruttore della classe paziente, il quale richiede in input il codice identificativo, il quale deve essere un attributo privato.
    setIdCode(idCode): consente di impostare il codice identificativo del paziente.
    getidCode(): consente di ritornare il codice identificativo del paziente.
    patientInfo(): stampa in output le informazioni del paziente in questo modo:

        "Paziente: {nome} {cognome}
         ID: {codice identificativo}"
 
'''

from persona import Persona

class Paziente(Persona):
    def __init__(self, first_name: str, last_name: str, id: str) -> None:
        super().__init__(first_name, last_name)
        self.__id = id

    def setIdCode(self, idCode: str) -> None:
        self.__id = idCode

    def getidCode(self) -> str:
        return self.__id
    
    def patientInfo(self) -> str:
        print(f"Paziente: {self.first_name} {self.last_name}\nID: {self.__id}")