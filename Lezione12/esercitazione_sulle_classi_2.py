'''

Sistema di Gestione Biblioteca
Si desidera sviluppare un sistema per la gestione di una biblioteca in Python. 
Il sistema deve permettere di gestire un inventario di libri e le operazioni di prestito e restituzione degli stessi. 
Gli utenti del sistema devono essere in grado di aggiungere libri al catalogo, prestarli, restituirli e visualizzare 
quali libri sono disponibili in un dato momento.
 
Classi:
- Libro: Rappresenta un libro con titolo, autore, stato del prestito. 
  Il libro deve essere inizialmente disponibile (non prestato).

- Biblioteca: Gestice tutte le operazioni legate alla gestione di una biblioteca.

    Metodi:
    - aggiungi_libro(libro): Aggiunge un nuovo libro al catalogo della biblioteca. 
      Restituisce un messaggio di conferma.

    - presta_libro(titolo): Cerca un libro per titolo e, se disponibile e non già prestato, 
      lo segna come disponibile. Restituisce un messaggio di stato.

    - restituisci_libro(titolo): Cerca un libro per titolo e, se trovato e prestato, 
      lo segna come disponibile. Restituisce un messaggio di stato.

    - mostra_libri_disponibili(): Restituisce una lista dei titoli dei libri attualmente disponibili. 
      Se non ci sono libri disponibili, restituisce un messaggio di errore.

Test Cases:
- Un amministratore della biblioteca aggiunge alcuni libri all'inventario.
- Un utente prende in prestito un libro, che viene quindi marcato come non disponibile.
- L'utente restituisce il libro, che viene marcato di nuovo come disponibile.
- In qualsiasi momento, un utente può visualizzare quali libri sono disponibili per il prestito.
 
 
Catalogo Film 
Sviluppa un sistema in Python per la gestione di un catalogo film che permetta di aggiungere, 
rimuovere e cercare film di un particolare regista. Il sistema dovrebbe consentire anche 
di visualizzare tutti i registi e i loro film.

Classe:
- MovieCatalog(): Gestisce tutte le operazioni legate al catalogo dei film.

    Metodi:
    - add_movie(director_name, movies): Aggiunge uno o più film a un regista specifico nel catalogo. 
      Se il regista non esiste, viene creato un nuovo record. Se il regista esiste, la sua lista di film viene aggiornata.

    - remove_movie(director_name, movie_name): Rimuove un film specifico dall'elenco dei film di un regista. 
      Se tutti i film sono rimossi, il regista può essere opzionalmente rimosso dal catalogo.

    - list_directors(): Elenca tutti i registi presenti nel catalogo.

    - get_movies_by_director(director_name): Restituisce tutti i film di un regista specifico.

    - search_movies_by_title(title): Trova tutti i film che contengono una certa parola nel titolo. 
      Restituisce un elenco dei registi e dei rispettivi film che contengono la parola cercata o un 
      messaggio di errore se nessun film contiene la parola cercata nel titolo.

'''

class Libro:
    def __init__(self, titolo: str, autore: str) -> None:
        self.titolo = titolo
        self.autore = autore
        self.stato_prestito: bool = False
    
    def __str__(self) -> str:
        pass
    
class Biblioteca:
    def __init__(self) -> None:
        self.catalogo: list[Libro] = []

    def aggiungi_libro(self, libro):
        self.libro = libro

        self.catalogo.append(self.libro)

    def presta_libro(self, titolo: str): #-> str:
        self.titolo = titolo
        
        for i in self.catalogo:
            if i.titolo == self.titolo and i.stato_prestito == False:
                i.stato_prestito = True
                print(i.titolo, "è disponibilie")
                break
        print("non è disponibile")
    
    def restituisci_libro(self, titolo: str): #-> str:
        self.titolo = titolo
        
        for i in self.catalogo:
            if i.titolo == self.titolo and i.stato_prestito == True:
                i.stato_prestito = False
                print(i.titolo, "non è disponibilie")
                break
        print("è disponibile")

    def mostra_libri_disponibili(self): #-> str:
        libri_disponibili_string: staticmethod = "Libri disponibili:\n"

        for i in self.catalogo:
            if i.stato_prestito == False:
                libri_disponibili_string += f"{i.__str__()}\n"

        if libri_disponibili_string != "Libri disponibili:\n":
            print(libri_disponibili_string)
        else:
            print("errore, non ci stanno libri disponibili")

#####

class Film:
    def __init__(self, title:str, director: str) -> None:
        self.title = title
        self.director = director
    
    def __str__(self) -> str:
        pass

class MovieCatalog:
    def __init__(self) -> None:
        self.catalogo: dict[str:list[str]] = {}

    def add_movie(self, director_name: str, movies: list[str]):
        self.director_name = director_name
        self.movies = movies

        if self.director_name in self.catalogo:
            self.catalogo[self.director_name].extend(self.movies)
        else:
            self.catalogo[self.director_name] = self.movies
    
    def remove_movie(self, director_name: str, movies: list[str]):
        self.director_name = director_name
        self.movies = movies

        self.catalogo[self.director_name].remove(self.movies)
        
        if self.catalogo[self.director_name] == []:
            self.catalogo.pop(self.director_name)

    def list_directors(self):
        for i in self.catalogo.keys():
            print(i)

    def get_movies_by_director(self, director_name: str):
        self.director_name = director_name

        for i in self.catalogo[self.director_name]:
            print(i)

    def search_movies_by_title(self, title: str):
        self.title = title

        if self.title in self.catalogo:
            pass
        else:
            print("error nessun film contiene questa parola")