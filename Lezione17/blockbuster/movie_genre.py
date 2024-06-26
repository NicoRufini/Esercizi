'''
Blockbuster

### CLASSI GENERE
Si creino tre classi chiamate Azione, Commedia e Drama, tutte derivanti dalla classe Film. Ognuna di queste classi ha un attributo privato di tipo string chiamato genere, che equivale al genere di film (genere="Azione", nella classe Azione) ed un attributo privato di tipo float chiamato penale. I film di azione hanno una penalità di 3 euro al giorno, le commedie hanno una penale di 2.50 euro al giorno, i film drammatici hanno una penale di 2 euro al giorno.

- Per ognuna di queste classi si implementi un metodo chiamato:

    getGenere(), che ritorna il genere di film
    getPenale(), che ritorna il valore della penale
    calcolaPenaleRitardo(), che prende in ingresso il numero dei giorni di ritardo per un film e restituisce la penale da pagare per quel film.

Le tre classi Azione, Commedia e Drama devono essere contenute nel file "movie_genre.py".

'''
#|||
from film import Film

#class Azione
class Azione(Film):
    def __init__(self, id: str, title: str) -> None:
        super().__init__(id, title)
        self.__genere: str = "Azione"
        self.__penale: float = 3

    def getGenere(self) -> str:
        return self.__genere
    
    def getPenale(self) -> float:
        return self.__penale
    
    def calcolaPenaleRitardo(self, giorni: int) -> float:
        return self.__penale*giorni 
    
#class Commedia
class Commedia(Film):
    def __init__(self, id: str, title: str) -> None:
        super().__init__(id, title)
        self.__genere: str = "Commedia"
        self.__penale: float = 2.5

    def getGenere(self) -> str:
        return self.__genere
    
    def getPenale(self) -> float:
        return self.__penale
    
    def calcolaPenaleRitardo(self, giorni: int) -> float:
        return self.__penale*giorni 
    
#class Drama
class Drama(Film):
    def __init__(self, id: str, title: str) -> None:
        super().__init__(id, title)
        self.__genere: str = "Drama"
        self.__penale: float = 2

    def getGenere(self) -> str:
        return self.__genere
    
    def getPenale(self) -> float:
        return self.__penale
    
    def calcolaPenaleRitardo(self, giorni: int) -> float:
        return self.__penale*giorni 
    