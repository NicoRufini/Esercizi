'''
Blockbuster

### CLASSE: Noleggio
In un file "noleggio.py", creare una classe Noleggio.
Questa classe deve avere come attributi una lista di film contenuti in negozio (film_list), un dizionario (rented_film) che ha come chiave un numero intero rappresentante l'id del cliente che ha affittato il film e per valore una lista contenente i film affittati dal cliente.
 
- Definire i seguenti metodi:

    init(film_list): tale metodo, inoltre,  deve creare un dizionario vuoto chiamato rented_film.
    isAvaible(film): tale metodo deve ritornare True se il film passato come argomento è presente nell'inventario del negozio, false in caso contrario. Se il film è disponibile in negozio stampare: "Il film scelto è disponibile: {titolo_film}!". Se il film non è disponibile in negozio stamapre: "Il film scelto è disponibile: {titolo_film}!".
    rentAMovie(film, clientID): tale metodo deve gestire il noleggio di un film ed ha come argomenti il film da noleggiare ed il codice id del cliente che lo noleggia. Affinché sia possibile noleggiare un film, un film deve essere disponibile in negozio. Pertanto, il metodo deve verificare la disponibilità. Nel caso in cui il film richiesto sia disponibile, rimuoverlo dalla lista dei film disponibili in negozio, poi riempire il dizionario rented_film in questo modo:
        la chiave sarà l'id del cliente che noleggia (id_client)
        il corrispondente valore sarà una lista contenente i film noleggiati da quel cliente.
    Pertanto, il film noleggiato, una volta rimosso dalla lista dei film disponibili in negozio deve essere aggiunto alla lista dei film noleggiati dal cliente dato.  Se il cliente ha potuto noleggiare il film richiesto, stampare: "Il cliente {clientId} ha noleggiato {titolo_film}!". Se, invece, il film richiesto non è disponibile pe il noleggio, stampare: Non è possibile nolegiare il film {titolo_film}!".
    giveBack(film, clientID, days): questo metodo consente di restituire un film noleggiato in negozio, ed ha come argomenti il film da restituire, il codice ID del client che restituisce il film, il numero dei giorni in cui il cliente ha tenuto il film per se.  Il film da restituire deve essere rimosso dalla lista dei film noleggiati dal cliente con id clientID, e tale film, deve essere riaggiunto alla lista dei film disponibili in negozio (film_list). Successivamente, il metodo deve calcolare la penale che il cliente deve pagare utilizzando l'opposito metodo. Stampare la penale che il cliente deve pagare: "Cliente: {clientID}! La penale da pagare per il film {titolo_film} e' di {tot} euro!".
    printMovies(): stampa la lista di tutti i film disponibili in negozio. Ogni film deve essere stampato in questo modo: "{titolo_film} - {genere_film} -"
    printRentMovies(clientID): questo metodo deve stampare la lista dei film noleggiati dal cliente di cui viene specificato l'id.

'''
#||\
from film import Film
from movie_genre import Azione, Commedia, Drama #(?) #|||

class Noleggio:
    def __init__(self, film_list: list[Film|Azione|Commedia|Drama]) -> None:
        self.film_list = film_list
        self.rented_film: dict[str, list[Film|Azione|Commedia|Drama]] = {}

    def isAvaible(self, film: Film|Azione|Commedia|Drama) -> bool:
        if film in self.film_list:
            print(f"Il film scelto è disponibile: {film.getTitle()}!")
            return True
        else:
            print(f"Il film scelto non è disponibile: {film.getTitle()}!")
            return False
        
    def rentAMovie(self, film: Film|Azione|Commedia|Drama, clientID: str) -> None:
        if film in self.film_list:
            if clientID in self.rented_film: #and len(self.rented_film[clientID]) == 0:
                #self.rented_film[clientID] = [film]
                self.rented_film[clientID].append(film)
                self.film_list.remove(film)
                print(f"Il cliente {clientID} ha noleggiato {film.getTitle()}!")
            #elif clientID in self.rented_film and len(self.rented_film[clientID]) > 0:
                #self.rented_film[clientID].append(film)
                #self.film_list.remove(film)
                #print(f"Il cliente {clientID} ha noleggiato {film.getTitle()}!")
            else: #
                self.rented_film[clientID] = [film]
                self.film_list.remove(film)
                print(f"Il cliente {clientID} ha noleggiato {film.getTitle()}!")            
        else:
            print(f"Non è possibile nolegiare il film {film.getTitle()}!")

    def giveBack(self, film: Film|Azione|Commedia|Drama, clientID: str, days: int) -> str:
        #if clientID in self.rented_film and film in self.rented_film: #\(?)
        if clientID in self.rented_film.keys() and film in self.rented_film[clientID]: #|(?) #if clientID in self.rented_film.items() and film in self.rented_film.items():
            self.film_list.append(film) #(parameter) film: Never(?)
            self.rented_film[clientID].remove(film) #(parameter) film: Never(?)
            penale_da_pagare: float = film.calcolaPenaleRitardo(days) #(parameter) film: Never(?)

            print(f"Cliente: {clientID}! La penale da pagare per il film {film.getTitle()} e' di {penale_da_pagare} euro!") #title: Never(?)

    def printMovies(self) -> str:
        #for i in self.film_list: #
            #print(i.getTitle(), "-", i.getGenere()) #
        
        self.film_list_string: str = "" #

        for i in self.film_list: #
            self.film_list_string += f"{i.getTitle()} - {i.getGenere()}\n" #

        print(self.film_list_string) #

    def printRentMovies(self, clientID: str) -> str:
        #if clientID in self.rented_film: #
            #for i in self.rented_film[clientID]: #
                #print(i) #

        self.rented_film_string: str = "" #

        if clientID in self.rented_film: #
            for i in self.rented_film[clientID]: #
                self.rented_film_string += f"{i}\n" #

        print(self.rented_film_string) #