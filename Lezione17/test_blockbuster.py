'''
Blockbuster

### Creazione di Test Case con UnitTest

Creare una suite di test utilizzando il modulo unittest di Python per verificare il corretto funzionamento delle classi Film, Azione, Commedia, Dramma, e Noleggio. 
Istruzioni
Creare un nuovo file Python denominato "test_blockbuster.py".
Importare il modulo unittest e tutte le classi definite.
Creare una sola classe di test chiamata TestFilm che eredita da unittest.TestCase.
 
Configurazione Iniziale:
- Utilizzare il metodo setUp per creare l'ambiente di test:
   - In setUp, istanziare 10 film (5 di azione, 4 commedie e 1 drammatico) e aggiungerli a una lista di film.
   - Creare un oggetto Noleggio utilizzando la lista di film creata.

Testare la Disponibilità di un Film (isAvaible):
- Scrivere un test per verificare che un film disponibile ritorni True.
- Scrivere un test per verificare che un film non disponibile ritorni False.

Testare il Noleggio di un Film (rentAMovie):
- Scrivere un test per verificare che un film disponibile possa essere noleggiato correttamente.
- Dopo il noleggio, verificare che il film non sia più disponibile.
- Verificare che il film noleggiato appaia nella lista dei film noleggiati dal cliente.

Testare il Noleggio di un Film Non Disponibile:
- Noleggiare un film con un cliente.
- Provare a noleggiare lo stesso film con un altro cliente e verificare che non sia possibile.

Testare la Restituzione di un Film (giveBack):
- Noleggiare un film e poi restituirlo.
- Verificare che il film restituito sia nuovamente disponibile.
- Verificare che il film restituito non sia più nella lista dei film noleggiati dal cliente.

Testare il Calcolo della Penale di Ritardo (calcolaPenaleRitardo):
- Scrivere test per verificare il calcolo della penale di ritardo per film di diversi generi (azione, commedia, dramma).

Testare la Stampa dei Film Disponibili (printMovies):
- Verificare che la lista dei film disponibili contenga i titoli corretti.

Testare la Stampa dei Film Noleggiati da un Cliente (printRentMovies):
- Noleggiare uno o più film per un cliente.
- Verificare che la stampa dei film noleggiati contenga i titoli corretti.

'''

import unittest
from film import Film
from movie_genre import Azione, Commedia, Drama
from noleggio import Noleggio

class testFilm(unittest.TestCase):
   def setUp(self) -> None:
      self.film_test: Film = Film("F01OT01", "The Spiderwick Chronicles")

class testAzione(unittest.TestCase):
   def setUp(self) -> None:
      self.azione_test1: Azione = Azione("AF01OT02", "The Rhythm Section")
      self.azione_test2: Azione = Azione("AF02OT02", "Raiders of the Lost Ark")
      self.azione_test3: Azione = Azione("AF03OT02", "Kill Bill")
      self.azione_test4: Azione = Azione("AF04OT02", "The Terminator")
      self.azione_test5: Azione = Azione("AF05OT02", "Predator")

class testCommedia(unittest.TestCase):
   def setUp(self) -> None:
      self.commedia_test1: Commedia = Commedia("CF01OT03", "21 Jump Street")
      self.commedia_test2: Commedia = Commedia("CF02OT03", "Ace Ventura: Pet Detective")
      self.commedia_test3: Commedia = Commedia("CF03OT03", "Beetlejuice")
      self.commedia_test4: Commedia = Commedia("CF04OT03", "Jojo Rabbit")

class testDrama(unittest.TestCase):
   def setUp(self) -> None:
      self.drama_test: Drama = Drama("DF01OT04", "Minari")

class testNoleggio(unittest.TestCase):
   def setUp(self) -> None:
      #Azione:
      self.azione_test1: Azione = Azione("AF01OT02", "The Rhythm Section")
      self.azione_test2: Azione = Azione("AF02OT02", "Raiders of the Lost Ark")
      self.azione_test3: Azione = Azione("AF03OT02", "Kill Bill")
      self.azione_test4: Azione = Azione("AF04OT02", "The Terminator")
      self.azione_test5: Azione = Azione("AF05OT02", "Predator")

      #Commedia:
      self.commedia_test1: Commedia = Commedia("CF01OT03", "21 Jump Street")
      self.commedia_test2: Commedia = Commedia("CF02OT03", "Ace Ventura: Pet Detective")
      self.commedia_test3: Commedia = Commedia("CF03OT03", "Beetlejuice")
      self.commedia_test4: Commedia = Commedia("CF04OT03", "Jojo Rabbit")

      #Drama:
      self.drama_test: Drama = Drama("DF010T04", "Minari")

      #List of movies:
      list_movies: list[Azione, Commedia, Drama] = [self.azione_test1, self.azione_test2, self.azione_test3,
                                                     self.azione_test4, self.azione_test5, self.commedia_test1, 
                                                     self.commedia_test2, self.commedia_test3, self.commedia_test4, self.drama_test]

      self.noleggio_test: Noleggio = Noleggio(list_movies)