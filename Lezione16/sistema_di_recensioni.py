'''
Obiettivo:
Implementare una classe Media che rappresenti un media generico (ad esempio, un film o un libro) 
e una classe derivata Film che rappresenti specificamente un film. Gli studenti dovranno anche 
creare oggetti di queste classi, aggiungere valutazioni e visualizzare le recensioni.

Specifiche della Classe Media:
 
Attributi:
- title (stringa): Il titolo del media.
- reviews (lista di interi): Una lista di valutazioni del media, con voti compresi tra 1 e 5.

Metodi:
- set_title(self, title): Imposta il titolo del media.
- get_title(self): Restituisce il titolo del media.
- aggiungiValutazione(self, voto): Aggiunge una valutazione alla lista delle recensioni se è valida (tra 1 e 5).
- getMedia(self): Calcola e restituisce la media delle valutazioni.
- getRate(self): Restituisce una stringa che descrive il giudizio medio del media basato sulla media delle valutazioni.
- ratePercentage(self, voto): Calcola e restituisce la percentuale di un voto specifico nelle recensioni.
- recensione(self): Mostra un riassunto delle recensioni e delle valutazioni del media, 
  stampando il titolo, il voto medio, il giudizio e le percentuali di ciascun voto. Esempio di riassunto:
 
Titolo del Film: The Shawshank Redemption
Voto Medio: 3.80
Giudizio: Bello
Terribile: 10.00%
Brutto: 10.00%
Normale: 10.00%
Bello: 30.00%
Grandioso: 40.00%

Si verifichi il funzionamento scrivendo un codice che crei almeno due oggetti di tipo Film, 
aggiunga a ognuno dei due almeno dieci valutazioni e richiami il metodo recensione().
'''

class Media:
    def __init__(self) -> None:
        #self.get_title() #
        self.title: str = None
        self.reviews: list[int] = []
        #self.media = sum(self.reviews) / len(self.reviews) #
        #self.media: float = 0 #

    def set_title(self, title: str):
        self.title = title

    def get_title(self) -> str:
        return f"Titolo del Film: {self.title}"
    
    def aggiungiValutazione(self, voto: int):
        if 1 <= voto <= 5:
            self.reviews.append(voto)

    def getMedia(self) -> str:
        self.media = sum(self.reviews) / len(self.reviews) #
        #return sum(self.reviews) / len(self.reviews)
        return f"Voto Medio: {self.media}"
    
    def getRate(self) -> str:
        '''
        <=1=Terribile, <=2=Brutto, <=3=Normale, <=4=Bello, <=5=Grandioso.
        '''
        self.media = sum(self.reviews) / len(self.reviews) #

        if self.media <= 1:
            return "Giudizio: Terribile"
        elif self.media <= 2:
            return "Giudizio: Brutto"
        elif self.media <= 3:
            return "Giudizio: Normale"
        elif self.media <= 4:
            return "Giudizio: Bello"
        elif self.media <= 5:
            return "Giudizio: Grandioso"

    def ratePercentage(self, voto: float) -> float: #La traccia in realtà NON chiede una stringa con il float "voto" come ho al return
        ''' ###Non lo devi mettere qui, lo devi spostare da un altra parte, forse è meglio se lo metti in recensione(self)
        self.Terribile = 0
        self.Brutto = 0 ...
        for i in self.reviews:
        if i <=1=Terribile:
        self.Terribilie += i ...

        rates_list = [self.Terrible, self.Brutto, ...]
        rates_dict = {Terribile : 0, Brutto : 0 , ...}
        rate: int = 0

        for i in rates_list and for j in rates_dict.keys(): #non si può fare #ho trovato il modo di farlo, continuo dopo
        rate = (len(self.Terrible, brutto, ...) / len(self.reviews))*100
        rates_dict[j] = rate
        '''

        '''
        #Questo invece lo devi lasciare qui
        voto_quantity: int = 0
        for i in self.reviews:
        if i == voto:
        voto_quantity += i

        voto_rate: float = (len(voto_quantity)/len(self.reviews))*100
        '''
        voto_quantity: int = 0

        for i in self.reviews:
            if i == voto:
                voto_quantity += 1
            #else: #
                #return "Nessuna delle recensioni ha questo voto" #

        voto_rate: float = ((voto_quantity)/len(self.reviews))*100

        return f"Il {voto_rate}% delle recensioni ha il voto {voto}."

    def recensione(self) -> str:
        terribile: int = 0
        brutto: int = 0
        normale: int = 0
        bello: int = 0
        grandioso: int = 0
        #self.media = sum(self.reviews) / len(self.reviews) #

        for i in self.reviews:
            if i <= 1:
                terribile += 1
            elif i <= 2:
                brutto += 1
            elif i <= 3:
                normale += 1
            elif i <= 4:
                bello += 1
            elif i <= 5:
                grandioso += 1
        
        rates_list: list = [terribile, brutto, normale, bello, grandioso]
        #voto_rate: float = 0
        rates_media_list: list = []

        for i in rates_list:
            #voto_rate = (len(i)/len(self.reviews))*100
            rates_media_list.append((i/len(self.reviews))*100)

        rates_media_dict: dict = {"Terribile" : rates_media_list[0], "Brutto" : rates_media_list[1], \
                                  "Normale" : rates_media_list[2], "Bello" : rates_media_list[3], \
                                    "Grandioso" : rates_media_list[4]}

        rates_media_string: str = ""

        for i, j in rates_media_dict.items():
            if i != "Grandioso":
                rates_media_string += f"{i}: {j}%\n"
        
        rates_media_string += f"Grandioso: {rates_media_list[4]}%" #

        print(f"{self.get_title()}\n{self.getMedia()}\n{self.getRate()}\n{rates_media_string}") #000 è temporaneo

#class Film: class Media è la sua superclasse e basta; rappresenta specificamente un film
class Film(Media):
    pass

film: Film = Film()

print("(Primo film)", "-"*30)
film.set_title("The Shawshank Redemption")
#print(film.get_title()) #
film.aggiungiValutazione(5) #Voti: [5, 4, 3, 5, 4, 5, 2, 4, 1, 5]
film.aggiungiValutazione(4)
film.aggiungiValutazione(3)
film.aggiungiValutazione(5)
film.aggiungiValutazione(4)
film.aggiungiValutazione(5)
film.aggiungiValutazione(2)
film.aggiungiValutazione(4)
film.aggiungiValutazione(1)
film.aggiungiValutazione(5)
#print(film.getRate()) #

#print(film.ratePercentage(1)) #
film.recensione() #

print("(Secondo film)", "-"*30)

film2: Film = Film()

film2.set_title("The Spiderwick Chronicles")
film2.aggiungiValutazione(3) #Voti: [3, 3, 3, 2, 3, 4, 4, 2, 3, 2]
film2.aggiungiValutazione(3)
film2.aggiungiValutazione(3)
film2.aggiungiValutazione(2)
film2.aggiungiValutazione(3)
film2.aggiungiValutazione(4)
film2.aggiungiValutazione(4)
film2.aggiungiValutazione(2)
film2.aggiungiValutazione(3)
film2.aggiungiValutazione(2)

#print(film2.ratePercentage(3)) #
film2.recensione() #

#Si verifichi il funzionamento scrivendo un codice 
#che crei almeno due oggetti di tipo Film, aggiunga a ognuno dei due almeno dieci valutazioni e richiami il metodo recensione().