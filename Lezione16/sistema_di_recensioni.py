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
        self.get_title()#
        self.reviews: list[int] = []

    def set_title(self, title: str):
        self.title = title

    def get_title(self) -> str:
        return self.title
    
    def aggiungiValutazione(self, voto: int):
        if 1 <= voto <= 5:
            self.reviews.append(voto)

    def getMedia(self) -> float:
        self.media = sum(self.reviews) / len(self.reviews)
        #return sum(self.reviews) / len(self.reviews)
        return f"Voto Medio: {self.media}"
    
    def getRate(self) -> str:
        '''
        <=1=Terribile, <=2=Brutto, <=3=Normale, <=4=Bello, <=5=Grandioso.
        '''
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

    def ratePercentage(self, voto: float) -> float:
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
        pass

    def recensione(self):
        pass

#class Film: class Media è la sua superclasse e basta; rappresenta specificamente un film