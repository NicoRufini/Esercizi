'''
2. RENDERING GRAFICO
Si vuole sviluppare un sistema in Python per gestire il rendering di diverse forme geometriche. 
Il sistema dovrà supportare almeno tre tipi di forme: quadrati, rettangoli, e triangoli rettangoli.

Definire la classe astratta Forma che sarà utilizzata per definire l'attributo corrispondente al nome della forma 
e le funzionalità base di ogni forma, come i metodi astratti getArea() per calcolare l'area e render() per disegnare su schermo la forma.

Definire la classe Quadrato che estende la classe Forma e aggiunge specifiche circa la lunghezza di un suo lato.
Il costruttore della classe deve ricevere come argomento solo il lato del quadrato, ed impostare il nome della forma su "Quadrato".
Il metodo getArea() deve calcolare l'area del quadrato.
Il metodo render() deve stamapre su schermo un quadrato avente lato pari al valore passato nel costruttore. 
Il quadrato da stampare deve essere un quadrato vuoto (" "), avente degli asterischi ("*") lungo il suo perimetro. (Vedi Esempio di output)

Definire la classe Rettangolo che estende la classe Forma e aggiunge specifiche circa la lunghezza della sua base e della sua altezza.
Il costruttore della classe deve ricevere come argomento solo la base e l'altezza del rettangolo, 
ed impostare il nome della forma su "Rettangolo".
Il metodo getArea() deve calcolare l'area del rettangolo.
Il metodo render() deve stampare su schermo un rettangolo avente base ed altezza pari ai valori passati nel costruttore. 
Il rettangolo da stampare deve essere un rettangolo vuoto (" "), avente degli asterischi ("*") lungo il suo perimetro. 
(Vedi Esempio di output)

Definire la classe Triangolo che estende la classe Forma e aggiunge specifiche circa la dimensione di un lato del triangolo 
(per semplicità, si suppone che il triangolo in questione sia un triangolo rettangolo).
Il costruttore della classe deve ricevere come argomento solo il lato del triangolo, ed impostare il nome della forma su "Triangolo".
Il metodo getArea() deve calcolare l'area del triangolo.
Il metodo render() deve stampare su schermo un triangolo rettangolo 
avente i due cateti di lunghezza pari ai valori passati nel costruttore. Il triangolo da stampare deve essere un triangolo vuoto (" "), 
avente degli asterischi ("*") lungo il suo perimetro. (Vedi Esempio di output)
 
Hint: per il disegno utilizzare print("*", end=" "), dato che l'argomento end = " " 
permette di controllare come termina ogni chiamata a print, e impostandolo a uno spazio si può fare in modo che 
tutte le stampe successive siano sulla stessa riga, separate da uno spazio.

Esempi di output:
Ecco un Quadrato di lato 4!

* * * *
*       *
*       *
* * * *
L'area di questo quadrato vale: 16

Ecco un Rettangolo avente base 8 ed altezza 4!
* * * * * * * *
*             *
*             *
* * * * * * * *
L'area di questo rettangolo vale: 32

Ecco un Triangolo avente base 4 ed altezza 4!
*      
* *    
*   *  
* * * *
L'area di questo triangolo vale: 8.0
'''
from abc import ABC, abstractmethod

#Forma:
class Forma(ABC):
    @abstractmethod
    def getArea(self):
        pass

    @abstractmethod
    def render(self):
        pass #continua, potrei usare vari print()

#Quadrato:
class Quadrato(Forma):
    def __init__(self, lato: int) -> None:
        self.lato = lato

    def getArea(self):
        return self.lato**2 
    
    def render(self):
        contatore: int = 0

        if self.lato >= 0: #|??????????????????
            print(f"Ecco un Quadrato di lato {self.lato}!")
        else: #
            print("I lati del quadrato non possono avere dei valori negativi") #

        if self.lato > 0:
            print("* "*self.lato)
        else:
            print("")

        while contatore < self.lato - 2:
            print("*"+" "*(self.lato*2 - 3)+"*")
            contatore += 1

        if self.lato >= 2:
            print("* "*self.lato)

        if self.lato >= 0: #|??????????????????
            print("L'area di questo quadrato vale:", self.getArea(), "\n")

#Rettangolo:
class Rettangolo(Forma):
    def __init__(self, base: int, altezza: int) -> None:
        self.base = base
        self.altezza = altezza

    def getArea(self):
        return self.base*self.altezza 
    
    def render(self):
        contatore: int = 0

        if self.base != self.altezza:
            '''if self.base < 0 or self.altezza < 0: #if self.base >= 0 or self.altezza >= 0:
                print(f"Ecco un Rettangolo avente base {self.base} ed altezza {self.altezza}!")'''
            if self.base >= 0 and self.altezza >= 0: #|??????????????????
                print(f"Ecco un Rettangolo avente base {self.base} ed altezza {self.altezza}!")
            else: #
                print("La base e/o l'altezza del rettangolo non possono avere dei valori negativi") #

            if self.base > 0 and self.altezza > 0:
                print("* "*self.base)
            else:
                print("")

        
            while contatore < self.altezza - 2 and self.base > 0: #and self.base > 0:
                print("*"+" "*(self.base*2 - 3)+"*") #print("*"+" "*(self.altezza*2 + (self.base - 3))+"*")
                contatore += 1
            '''elif self.altezza > self.base:
                while contatore < self.altezza - 2:
                    print("*"+" "*(self.base*2 - 3)+"*") #print("*"+" "*(self.altezza*2 + 13)+"*")
                    contatore += 1'''

            if self.altezza >= 2:
                print("* "*self.base)
            
            if self.base >= 0 and self.altezza >= 0: #|??????????????????
                print("L'area di questo rettangolo vale:", self.getArea(), "\n")
        
        else:
            print("Un rettangolo non può avere base ed altezza uguali\n")

#Triangolo:
class Triangolo(Forma):
    def __init__(self, lato: int) -> None:
        self.lato = lato

    def getArea(self):
        return (self.lato*self.lato)/2

    def render(self):
        contatore: int = 0
        spazio: int = 0

        if self.lato >= 0: #|??????????????????
            print(f"Ecco un Triangolo avente base {self.lato} ed altezza {self.lato}!")
        else: #
            print("I lati del triangolo non possono avere dei valori negativi") #

        while contatore < self.lato - 1:
            print("*"+" "*spazio+"*")
            contatore += 1
            spazio += 2

        if self.lato > 0:
            print("* "*self.lato)
        else:
            print("")

        if self.lato >= 0: #|??????????????????
            print("L'area di questo triangolo vale:", self.getArea(), "\n")

print("(Quadrato)", "-"*30)
#Quadrato:
#Lato 8:
quadrato0: Quadrato = Quadrato(8)
quadrato0.render()

#Lato 15:
quadrato0: Quadrato = Quadrato(15)
quadrato0.render()

#Lato 4:
quadrato0: Quadrato = Quadrato(4)
quadrato0.render()

#Lato 5:
quadrato0: Quadrato = Quadrato(5)
quadrato0.render()

#Lato 2:
quadrato0: Quadrato = Quadrato(2)
quadrato0.render()

#Lato 1:
quadrato0: Quadrato = Quadrato(1)
quadrato0.render()

#Lato 0:
quadrato0: Quadrato = Quadrato(0)
quadrato0.render()

#Lato -1:
quadrato0: Quadrato = Quadrato(-1)
quadrato0.render()

print("\n(Rettangolo)", "-"*30)
#Rettangolo:
#base 8:
rettangolo0: Rettangolo = Rettangolo(8, 4)
rettangolo0.render()

#base 15:
rettangolo0: Rettangolo = Rettangolo(15, 7)
rettangolo0.render()

#base 4:
rettangolo0: Rettangolo = Rettangolo(4, 2)
rettangolo0.render()

#base 5:
rettangolo0: Rettangolo = Rettangolo(5, 3)
rettangolo0.render()

#base 2:
rettangolo0: Rettangolo = Rettangolo(2, 1)
rettangolo0.render()

#base 1:
rettangolo0: Rettangolo = Rettangolo(1, 0)
rettangolo0.render()

#base 0:
rettangolo0: Rettangolo = Rettangolo(0, 0)
rettangolo0.render()

#altezza -1:
rettangolo0: Rettangolo = Rettangolo(7, -1)
rettangolo0.render()

#altezza 8:
rettangolo0: Rettangolo = Rettangolo(4, 8)
rettangolo0.render()

#altezza 15:
rettangolo0: Rettangolo = Rettangolo(7, 15)
rettangolo0.render()

#altezza 4:
rettangolo0: Rettangolo = Rettangolo(2, 4)
rettangolo0.render()

#altezza 5:
rettangolo0: Rettangolo = Rettangolo(3, 4)
rettangolo0.render()

#altezza 2:
rettangolo0: Rettangolo = Rettangolo(1, 2)
rettangolo0.render()

#altezza 1:
rettangolo0: Rettangolo = Rettangolo(0, 1)
rettangolo0.render()

#altezza -1:
rettangolo0: Rettangolo = Rettangolo(7, -1)
rettangolo0.render()

print("\n(Triangolo)", "-"*30)
#Triangolo:
#Lato 8:
triangolo0: Triangolo = Triangolo(8)
triangolo0.render()

#Lato 15:
triangolo0: Triangolo = Triangolo(15)
triangolo0.render()

#Lato 4:
triangolo0: Triangolo = Triangolo(4)
triangolo0.render()

#Lato 5:
triangolo0: Triangolo = Triangolo(5)
triangolo0.render()

#Lato 2:
triangolo0: Triangolo = Triangolo(2)
triangolo0.render()

#Lato 1:
triangolo0: Triangolo = Triangolo(1)
triangolo0.render()

#Lato 0:
triangolo0: Triangolo = Triangolo(0)
triangolo0.render()

#Lato -1:
triangolo0: Triangolo = Triangolo(-1)
triangolo0.render()