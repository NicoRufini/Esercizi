'''
Sistema di Prenotazione Cinema

Sviluppa un sistema in Python che gestisca le prenotazioni per un cinema. 
Il cinema ha diverse sale, ognuna con un diverso film in programmazione. 
Gli utenti possono vedere quali film sono disponibili e prenotare posti per un determinato spettacolo.
 
Classi:
- Film: Rappresenta un film con titolo e durata.
 
- Sala: Rappresenta una sala con numero identificativo, 
        film attualmente in programmazione, posti totali, posti prenotati.

Metodi:
    - prenota_posti(num_posti): Prenota un certo numero di posti nella sala, se disponibili. 
      Restituisce un messaggio di conferma o di errore.
    - posti_disponibili(): Restituisce il numero di posti ancora disponibili nella sala.
 
- Cinema: Gestisce le operazioni legate alla gestione delle sale.

Metodi:
    - aggiungi_sala(sala): Aggiunge una nuova sala al cinema.
    - prenota_film(titolo_film, num_posti): Trova il film desiderato e tenta di prenotare posti. 
      Restituisce un messaggio di stato.

Test case:

    Un gestore del cinema configura le sale aggiungendo i film e i dettagli dei posti.
    Un cliente sceglie un film e prenota un certo numero di posti.
    Il sistema verifica la disponibilità e conferma o rifiuta la prenotazione.

 
 
Gestione di un magazzino
Scrivi un programma in Python che gestisca un magazzino. Il programma deve permettere 
di aggiungere prodotti al magazzino, cercare prodotti per nome e verificare la disponibilità di un prodotto.

Definisci una classe Prodotto con i seguenti attributi:
- nome (stringa)
- quantità (intero)
 
Definisci una classe Magazzino con i seguenti metodi:
- aggiungi_prodotto(prodotto: Prodotto): aggiunge un prodotto al magazzino.
- cerca_prodotto(nome: str) -> Prodotto: cerca un prodotto per nome e lo ritorna se esiste.
- verifica_disponibilità(nome: str) -> str: verifica se un prodotto è disponibile in magazzino.
 
Test case:

    Un gestore del magazzino crea un magazzino e diversi prodotti in diverse quantità. 
    Successivamente, aggiunge i prodotti al magazzino.
    Il sistema cerca un prodotto per verificare se esiste nell'inventario.
    Il sistema verifica la disponibilità dei prodotti in inventario.

'''
#Per una sala ci sta solo un film

class Film:
    def __init__(self, titolo: str, durata: int) -> None:
        self.titolo = titolo
        self.durata = durata

    def __str__(self) -> str:
        pass

class Sala:
    def __init__(self, id: int, film_in_programmazione: Film, posti_totali: int) -> None:
        self.id = id
        self.film_in_programmazione = film_in_programmazione
        self.posti_totali = posti_totali
        self.num_posti_disponibili: int = self.posti_totali #
        #self.posti_prenotati: int = 0 #

    def prenota_posti(self, num_posti: int) -> str:
        self.num_posti = num_posti #5 4 3 7 con il 2 deve dare errore
        
        if self.num_posti <= self.num_posti_disponibili:
            self.num_posti_disponibili -= self.num_posti #
            print("u can", self.num_posti)
        else:
            print("error u can't")

    def posti_disponibili(self) -> int:
        print(self.num_posti_disponibili)

    def __str__(self) -> str:
        pass

class Cinema:
    def __init__(self) -> None:
        self.num_sale: list[Sala] = []

    def aggiungi_sala(self, sala: Sala) -> Sala: #-> Sala? per tutti e due controlla i metodi dell'esercizio
        self.sala = sala

        self.num_sale.append(self.sala)

    def prenota_film(self, titolo_film: str, num_posti: int) -> str:
        self.titolo_film = titolo_film
        self.num_posti = num_posti

        for i in self.num_sale:
            if i.film_in_programmazione.titolo == self.titolo_film:
                print("ci sta il film", self.titolo_film)
                i.prenota_posti(self.num_posti)
                break
        print("non ci sta il film, quindi non lo puoi prenotare")

    def __str__(self) -> str:
        pass

#####
class Prodotto:
    def __init__(self, nome: str, quantità: int) -> None:
        self.nome = nome
        self.quantità = quantità

    def __str__(self) -> str:
        pass

class Magazzino:
    def __init__(self) -> None:
        self.num_prodotti: list[Prodotto] = []

    def aggiungi_prodotto(self, prodotto: Prodotto) -> Prodotto: #-> Prodotto? per tutti e due controlla i metodi dell'esercizio
        self.prodotto = prodotto

        self.num_prodotti.append(self.prodotto)

    def cerca_prodotto(self, nome: str) -> Prodotto:
        self.nome = nome

        for i in self.num_prodotti:
            if i.nome == self.nome:
                print(self.nome, "ci sta il prodotto")
                break
        print("non ci sta il prodotto")

    def verifica_disponibilità(self, nome: str) -> str:
        self.nome = nome

        for i in self.num_prodotti:
            if i.nome == self.nome:
                print(self.nome, "è disponibile")
                break
        print("no non è disponibile")

    def __str__(self) -> str:
        pass
