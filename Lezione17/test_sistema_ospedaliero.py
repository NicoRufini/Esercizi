'''
Gestione sistema ospedaliero

### Creazione di Test Case con UnitTest

Creare una suite di test utilizzando il modulo unittest di Python per verificare il corretto funzionamento delle classi Persona, 
Dottore, Paziente e Fattura fornite nel codice. I test devono coprire l'inizializzazione degli oggetti, 
i metodi di accesso e modifica degli attributi, e i comportamenti specifici delle classi.
Istruzioni
Creare un nuovo file Python denominato "test_persona.py".
Importare il modulo unittest e tutte le classi definite.

Test della Classe Persona
- Creare una classe di test chiamata TestPersona che eredita da unittest.TestCase.
- Implementare il metodo setUp per inizializzare un oggetto Persona con nome e cognome.
- Scrivere test per verificare:
  - L'inizializzazione corretta degli attributi first_name, last_name e age.
  - Il funzionamento dei metodi setName, setLastName e setAge.

Test della Classe Dottore
- Creare una classe di test chiamata TestDottore che eredita da unittest.TestCase.
- Implementare il metodo setUp per inizializzare un oggetto Dottore con nome, cognome, specializzazione e parcella.
- Scrivere test per verificare:
  - L'inizializzazione corretta degli attributi specifici di Dottore.
  - Il funzionamento del metodo isValidDoctor con diverse età.

Test della Classe Paziente
- Creare una classe di test chiamata TestPaziente che eredita da unittest.TestCase.
- Implementare il metodo setUp per inizializzare un oggetto Paziente con nome, cognome e ID.
- Scrivere test per verificare:
  - L'inizializzazione corretta degli attributi specifici di Paziente.

Test della Classe Fattura
- Creare una classe di test chiamata TestFattura che eredita da unittest.TestCase.
- Implementare il metodo setUp per inizializzare un oggetto Fattura con una lista di pazienti e un dottore valido.
- Scrivere test per verificare:
  - L'inizializzazione corretta della classe Fattura.
  - Il calcolo corretto del salario e del numero di fatture.
  - L'aggiunta e la rimozione di pazienti dalla lista.

'''
#\\\
import unittest
from persona import Persona
from dottore import Dottore
from paziente import Paziente
from fatture import Fattura

class TestPersona(unittest.TestCase):
    def setUp(self) -> None:
      self.persona_test: Persona = Persona("Giampiero", "Bolagnoni")
      #self.persona_test2: first_name and\or last_name != str (?)
        #return super().setUp()

    def test_init(self):
        self.assertEqual(self.persona_test.getName(), "Giampiero", "Error: __init__(), first_name")
        self.assertEqual(self.persona_test.getLastname(), "Bolagnoni", "Error: __init__(), last_name")
        self.assertEqual(self.persona_test.getAge(), 0, "Error: __init__(), age")

    def test_setName(self):
        self.persona_test.setName("Giovanni")
        self.assertEqual(self.persona_test.getName(), "Giovanni", "Error: setName()")

    def test_setLastName(self):
      self.persona_test.setLastName("Posgantino")
      self.assertEqual(self.persona_test.getLastname(), "Posgantino", "Error: setLastName()")

    def test_setAge(self):
      self.persona_test.setAge(15)
      self.assertEqual(self.persona_test.getAge(), 15, "Error: setAge")
    

class TestDottore(unittest.TestCase):
    def setUp(self) -> None:
      self.dottore_test: Dottore = Dottore("Giampiero", "Bolagnoni", "Chirurgo", 77.5)
      #self.dottore_test2: \\ (?)

    def test_init(self):
      self.assertEqual(self.dottore_test.getName(), "Giampiero", "Error: __init__(), first_name")
      self.assertEqual(self.dottore_test.getLastname(), "Bolagnoni", "Error: __init__(), last_name")
      self.assertEqual(self.dottore_test.getAge(), 0, "Error: __init__(), age")
      self.assertEqual(self.dottore_test.getSpecialization(), "Chirurgo", "Error: __init__(), specialization")
      self.assertEqual(self.dottore_test.getParcel(), 77.5, "Error: __init__(), parcel")

    def test_isAValidDoctor(self):
      self.dottore_test.setAge(22)
      self.assertFalse(self.dottore_test.isAValidDoctor(), "Errore: test_isValidDoctor with age 22 is not False")

      self.dottore_test.setAge(31)
      self.assertTrue(self.dottore_test.isAValidDoctor(), "Errore: test_isValidDoctor with age 31 is not True")
      
      self.dottore_test.setAge(30)
      self.assertFalse(self.dottore_test.isAValidDoctor(), "Errore: test_isValidDoctor with age 30 is not False")

class TestPaziente(unittest.TestCase):
  def setUp(self) -> None:
    self.paziente_test: Paziente = Paziente("Giampiero", "Bolagnoni", "A01B02C03")
    #self.paziente_test2 \\

  def test_init(self):
    self.assertEqual(self.paziente_test.getName(), "Giampiero", "Error: __init__(), first_name")
    self.assertEqual(self.paziente_test.getLastname(), "Bolagnoni", "Error: __init__(), last_name")
    self.assertEqual(self.paziente_test.getAge(), 0, "Error: __init__(), age")
    self.assertEqual(self.paziente_test.getidCode(), "A01B02C03", "Error: __init__(), id")

class TestFattura(unittest.TestCase):
  def setUp(self) -> None:
    self.paziente1: Paziente = Paziente("Monica", "Rossi", "M06R05")
    self.paziente2: Paziente = Paziente("Alessandro", "Vernuzzo", "A10V08")
    self.dottore0: Dottore = Dottore("Giampiero", "Bolagnoni", "Chirurgo", 77.5)
    self.dottore0.setAge(61)
    self.fattura_test: Fattura = Fattura([self.paziente1, self.paziente2], self.dottore0)

  def test_init(self):
    self.assertEqual(self.fattura_test.getFatture(), 2, "Error: __init__(), fatture")

  def test_getSalary(self):
    self.assertEqual(self.fattura_test.getSalary(), 77.5*2, "Error: getSalary()")

  def test_addPatient(self):
    new_patient: Paziente = Paziente("Daniele", "Soccarddino", "D07S11")
    self.fattura_test.addPatient(new_patient)
    self.assertEqual(self.fattura_test.getFatture(), 3, "Error: addPatient()")

  def test_removePatient(self):
    self.fattura_test.removePatient("A10V08")
    self.assertEqual(self.fattura_test.getFatture(), 1, "Error: removePatient()")

unittest.main()