'''
1. GESTIONALE PAGAMENTO
Si definisca una nuova classe Pagamento che contiene un attributo privato e di tipo float che memorizza 
l'importo del pagamento e si definiscano appropriati metodi get() e set(). 
L'importo non è un parametro da passare in input alla classe Pagamento ma deve essere inizializzato 
utilizzando il metodo set() dove opportuno. Si crei inoltre un metodo dettagliPagamento() 
che visualizza una frase che descrive l'importo del pagamento, ad esempio: "Importo del pagamento: €20.00". 
Quando viene stampato, l'importo è sempre con 2 cifre decimali.

Successivamente, si definisca una classe PagamentoContanti che sia derivata da Pagamento e definisca l'importo. 
Questa classe dovrebbe ridefinire il metodo dettagliPagamento() per indicare che il pagamento è in contanti. 
Si definisca inoltre il metodo inPezziDa() che stampa a schermo quante banconote da 
500 euro, 200 euro, 100 euro, 50 euro, 20 euro, 10 euro, 5 euro e/o in quante monete da 2 euro, 1 euro, 
0,50 euro, 0,20 euro, 0,10 euro, 0,05 euro, 0,01 euro sono necessarie per pagare l'importo in contanti.

Si definisca una classe PagamentoCartaDiCredito derivata anch'essa da Pagamento e che definisce l'importo. 
Questa classe deve contenere gli attributi per il nome del titolare della carta, la data di scadenza, 
e il numero della carta di credito. Infine, si ridefinisca il metodo dettagliPagamento() per includere tutte 
le informazioni della carta di credito oltre all'importo del pagamento.

Per il test, si creino almeno due oggetti di tipo PagamentoContanti e due di tipo PagamentoCartaDiCredito con valori differenti 
e si invochi dettagliPagamento() per ognuno di essi.

Esempio di output:
Pagamento in contanti di: €150.00
150.00 euro da pagare in contanti con:
1 banconota da 100 euro
1 banconota da 50 euro

Pagamento in contanti di: €95.25
95.25 euro da pagare in contanti con:
1 banconota da 50 euro
2 banconote da 20 euro
1 banconota da 5 euro
1 moneta da 0.2 euro
1 moneta da 0.05 euro

Pagamento di: €200.00 effettuato con la carta di credito
Nome sulla carta: Mario Rossi
Data di scadenza: 12/24
Numero della carta: 1234567890123456

Pagamento di: €500.00 effettuato con la carta di credito
Nome sulla carta: Luigi Bianchi
Data di scadenza: 01/25
Numero della carta: 6543210987654321
'''
from abc import ABC, abstractmethod

#Pagamento:
class Pagamento(ABC):
    def __init__(self) -> None:
        self.__importo: float = None

    #@abstractmethod
    def setImporto(self, importo: float) -> None:
        self.__importo = importo
    
    #@abstractmethod
    def getImporto(self) -> float:
        return self.__importo
    
    @abstractmethod
    def dettagliPagamento(self) -> None: #-> str(?):
        print(f"Importo del pagamento: €{self.__importo():.2f}") #{'{0:.2f}'.format(self.__importo)}
        #pass

#PagamentoContanti:
class PagamentoContanti(Pagamento):
    def __init__(self) -> None:
        super().__init__()

    def dettagliPagamento(self) -> None:
        print(f"Pagamento in contanti di: €{self.getImporto():.2f}")

    def inPezziDa(self) -> None:
        banconote: list[int] = [500, 200, 100, 50, 20, 10, 5]
        monete: list[float] = [2, 1, 0.50, 0.20, 0.10, 0.05, 0.01]
        banconote_risultato: list[int] = []
        monete_risultato: list[float] = []
        importo: float = self.getImporto()

        ##########

        importo_monete: float = 0

        #prove per l'importo: 1517.62 #|(?); 1500 #|(?); 500; 700; 2483; 389.00; 176.0
        #prove per l'importo EXTRA: 0.00

        if importo_monete % 1 != 0:
            importo_monete +=  round(importo % 1, 2)
            importo -= importo_monete

        while importo % 5 != 0:
            importo -= 1
            importo_monete += 1

        #è per le banconote:
        if importo % 5 == 0:
            for i in banconote:
                while importo > 0 and importo % 5 == 0: #--- #and importo > 0 forse non è necessario
                    if i == importo:
                        importo -= i
                        banconote_risultato.append(i)
                    elif importo % i == 0:
                        while importo % i == 0 and importo > 0: #and importo > 0:
                            importo -= i
                            banconote_risultato.append(i)
                    elif importo - i  >= 0:
                        while importo - i  >= 0: #  
                            importo -= i
                            banconote_risultato.append(i)

        #è per le monete:
        if importo_monete % 5 != 0: #nel dubbio, da rivedere
            for i in monete:
                while importo_monete > 0 and importo_monete % 5 != 0:
                    if i == importo:
                        importo_monete -= i
                        monete_risultato.append(i)
                    elif importo_monete % i == 0:
                        while importo_monete % i == 0 and importo > 0: #and importo > 0: ---
                            importo_monete -= i
                            monete_risultato.append(i)
                    elif importo_monete - i  >= 0:
                        while importo - i  >= 0: #  
                            importo_monete -= i
                            monete_risultato.append(i)

        ###idea per il risultato:
        risultato_string: str = f"{self.getImporto()} euro da pagare in contanti con:"

        banconote_risultato_string: str = "" #non è "" ###forse le posso lasciare a ""
        monete_risultato_string: str = "" #non è "" ###forse le posso lasciare a ""


        #Per aggiornare le stringhe:
        for i in range(len(banconote_risultato)): #---Da rivedere #"banconote" se il count è maggiore di 1
            if i != (len(banconote_risultato) -1) and banconote_risultato[i] != banconote_risultato[-len(banconote_risultato) + i + 1]: #ci potrei mettere un and e verificare che l'item subito accanto è diverso, non rispetterà l'if se è uguale, ritrova la formula per calcolare l'indice dell'item accanto senza andare 'out of bound', ho fatto qualche prova e sembra andare bene
                banconote_risultato_string += f"{banconote_risultato.count(banconote_risultato[i])} banconota da {banconote_risultato[i]} euro\n" #cambia 1 con il count e 50 con banco_risultato[i]

        if len(banconote_risultato) != 0: #nel caso in cui la lista rimanga vuota
            banconote_risultato_string += f"{banconote_risultato.count(banconote_risultato[-1])} banconota da {banconote_risultato[-1]} euro"        

        #Continua dopo con monete_risultato_string

        for i in range(len(monete_risultato)):
            if i != (len(monete_risultato) -1) and monete_risultato[i] != monete_risultato[-len(monete_risultato) + i + 1]:
                monete_risultato_string += f"{monete_risultato.count(monete_risultato[i])} moneta da {monete_risultato[i]} euro\n"

        if len(monete_risultato) != 0: #nel caso in cui la lista rimanga vuota
            monete_risultato_string += f"{monete_risultato.count(monete_risultato[-1])} banconota da {monete_risultato[-1]} euro"

        if banconote_risultato_string != "": ###
            risultato_string += f"\n{banconote_risultato_string}" ###

        if monete_risultato_string != "": ###
            risultato_string += f"\n{monete_risultato_string}" ###

        print(risultato_string)

        ##########

        '''
        importo_monete: float = 0

        spezzetare importo per dare una parte le banconote e una parte le monete:
        ------------------------
        #per i centesimi e anche le monete:
        
        a = 269.99
        b = 0
        if a % 1 != 0:
        b += round(a % 1, 2) 
        a -= b

        while a % 5 != 0:
        a -= 1 #0.01
        b += 1 #0.01
    
        print("a:", a, "b:", b)
        ------------------------

        #prove per l'importo: 1517.62 #|(?); 1500 #|(?); 500; 700; 2483; 389.00; 176.0
        #prove per l'importo EXTRA: 0.00

        if importo_monete % 1 != 0:
        importo_monete +=  round(importo % 1, 2)
        importo -= importo_monete

        while importo % 5 != 0:
        importo -= 1
        importo_monete += 1
        
        #è per le banconote:
        if importo % 5 == 0:
        for i in banconote:
        while importo > 0 and importo % 5 == 0: #--- #and importo > 0 forse non è necessario
        if i == importo:
        importo -= i
        banconote_risultato.append(i)
        elif importo % i == 0:
        while importo % i == 0 and importo > 0: #and importo > 0:
        importo -= i
        banconote_risultato.append(i)
        elif importo - i  >= 0:
        while importo - i  >= 0: #  
        importo -= i
        banconote_risultato.append(i)

        #è per le monete:
        if importo_monete % 5 != 0: #nel dubbio, da rivedere
        for i in monete:
        while importo_monete > 0 and importo_monete % 5 != 0:
        if i == importo:
        importo_monete -= i
        monete_risultato.append(i)
        elif importo_monete % i == 0:
        while importo_monete % i == 0 and importo > 0: #and importo > 0: ---
        importo_monete -= i
        monete_risultato.append(i)
        elif importo_monete - i  >= 0:
        while importo - i  >= 0: #  
        importo_monete -= i
        monete_risultato.append(i)

        ###idea per il risultato:
        risultato_string: str = f"{self.getImporto()} euro da pagare in contanti con:"

        banconote_risultato_string: str = "" #non è "" ###forse le posso lasciare a ""
        monete_risultato_string: str = "" #non è "" ###forse le posso lasciare a ""

        #Per aggiornare le stringhe:
        for i in range(len(banconote_risultato)): #---Da rivedere #"banconote" se il count è maggiore di 1
        if i != (len(banconote_risultato) -1) and banconote_risultato[i] != banconote_risultato[-len(banconote_risultato) + i + 1]: #ci potrei mettere un and e verificare che l'item subito accanto è diverso, non rispetterà l'if se è uguale, ritrova la formula per calcolare l'indice dell'item accanto senza andare 'out of bound', ho fatto qualche prova e sembra andare bene
        banconote_risultato_string += f"{banconote_risultato.count(banconote_risultato[i])} banconota da {banconote_risultato[i]} euro\n" #cambia 1 con il count e 50 con banco_risultato[i]

        if len(banconote_risultato) != 0: #nel caso in cui la lista rimanga vuota
        banconote_risultato_string += f"{banconote_risultato.count(banconote_risultato[-1])} banconota da {banconote_risultato[-1]} euro"        

        #Continua dopo con monete_risultato_string

        for i in range(len(monete_risultato)):
        if i != (len(monete_risultato) -1) and monete_risultato[i] != monete_risultato[-len(monete_risultato) + i + 1]:
        monete_risultato_string += f"{monete_risultato.count(monete_risultato[i]} moneta da {monete_risultato[i]} euro\n"

        if len(monete_risultato) != 0: #nel caso in cui la lista rimanga vuota
        monete_risultato_string += f"{monete_risultato.count(monete_risultato[-1])} banconota da {monete_risultato[-1]} euro"

        if banconote_risultato_string != "": ###
        risultato_string += f"\n{banconote_risultato_string}" ###

        if monete_risultato_string != "": ###
        risultato_string += f"\n{monete_risultato_string}" ###

        print(risultato_string)
        '''

#PagamentoCartaDiCredito:
class PagamentoCartaDiCredito(Pagamento):
    def __init__(self, nome_titolare: str, data_scadenza: str, numero_carta: int) -> None: #numero_carta: str
        super().__init__()
        self.nome_titolare = nome_titolare
        self.data_scadenza = data_scadenza
        self.numero_carta = numero_carta

    def dettagliPagamento(self) -> None:
        print(f"Pagamento di: €{self.__importo:.2f} effettuato con la carta di credito")
        print(f"Nome sulla carta: {self.nome_titolare}")
        print(f"Data di scadenza: {self.data_scadenza}")
        print(f"Numero della carta: {self.numero_carta}")

#pagamentoContanti: PagamentoContanti = PagamentoContanti()

#pagamentoContanti.setImporto(25.2)
#pagamentoContanti.dettagliPagamento()