'''
Gestione sistema ospedaliero

### CLASSE: Fattura
Creare un file chiamato "fatture.py".
In tale file, creare una classe chiamata Fattura.

- Definire i seguenti metodi:

    init(patient,doctor): deve avere come input una lista di pazienti ed un dottore. Tale metodo deve verificare se il dottore può esercitare la professione, richiamando la funzione isAValidDoctor(). In caso affermativo assegnare all'attributo fatture (di tipo intero) il numero di pazienti che ha il dottore, mentre assegnare 0 all'attributo salary (di tipo int).  In caso contrario, assegnare il valore None a tutti i 4 gli attributi della classe e stampare un messaggio di errore, come, ad esempio: "Non è possibile creare la classe fattura poichè il dottore non è valido!".
    getSalary(): deve ritornare il salario guadagnato dal dottore. Il salario gudaganto viene calcolato moltiplicando la parcella del dottore per il numero di pazienti.
    getFatture(): deve assegnare all'attributo fatture il numero di pazienti (in modo che sia sempre aggiornato) che ha il dottore e ritornare il suo valore.
    addPatient(newPatient): consente di aggiungere un paziente alla lista di pazienti di un dottore, aggiornando poi il numero di fatture ed il salario, richiamando il metodo getFatture() e getSalary().  Stampare "Alla lista del Dottor cognome è stato aggiunto il paziente {codice_identificativo}"
    removePatient(idCode): consente di rimuovere un paziente alla lista di pazienti di un dottore ricevendo in input il codice identificativo del paziente da rimuovere, aggiornando poi il numero di fatture e il salario, richiamando il metodo get Fatture() e getSalary(). Stampare "Alla lista del Dottor cognome è stato rimosso il paziente {codice_identificativo}".

'''
#||\
#from persona import Persona #(?)
from dottore import Dottore
from paziente import Paziente

class Fattura:
    def __init__(self, patient: list[Paziente], doctor: Dottore) -> None: #patient: list[Paziente], doctor: Doctor
        self.patient = patient
        self.doctor = doctor
        self.fatture: int = 0
        self.salary: int = 0

        if self.doctor.isAValidDoctor() == True: #(?) #== True
            self.fatture = len(self.patient)
        else:
            self.patient = None
            self.doctor = None
            self.fatture = None
            self.salary = None
            print("Non è possibile creare la classe fattura poichè il dottore non è valido!")

    def getSalary(self) -> int:
        self.salary = self.doctor.getParcel()*self.fatture #self.doctor.__parcel*self.fatture
        return self.salary
    
    def getFatture(self) -> int:
        self.fatture = len(self.patient)
        return self.fatture
    
    def addPatient(self, newPatient: Paziente) -> str: #newPatient: Paziente
        #if type(self.patient) != None: ###
        self.patient.append(newPatient)
        self.getFatture()
        self.getSalary()
        print(f"Alla lista del Dottor {self.doctor.getLastname()} è stato rimosso il paziente {newPatient.getidCode()}") #self.doctor.__last_name #self.newPatient.__id: Any(?)
    
    def removePatient(self, idCode: str) -> str:
        for i in self.patient:
            if i.getidCode() == idCode: #if i.__id == idCode:
                self.patient.remove(i)
        
        self.getFatture()
        self.getSalary()
        print(f"Alla lista del Dottor {self.doctor.getLastname()} è stato rimosso il paziente {idCode}") #self.doctor.__last_name