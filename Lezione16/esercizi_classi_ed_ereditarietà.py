'''
Vogliamo gestire un contatore che può essere incrementato, decrementato, resettato e visualizzato. 
La classe offre un modo semplice per tenere traccia di un conteggio che non può diventare negativo.

Classe Contatore
Attributi:
- conteggio: un intero che conserva il valore del conteggio, inizializzato a 0.

Metodi:
- __init__(): Inizializza l'attributo conteggio a 0.
- setZero(): Imposta il conteggio a 0.
- add1(): Incrementa il conteggio di 1.
- sub1(): Decrementa il conteggio di 1, ma non permette che il conteggio diventi negativo. 
  Se il conteggio è già 0, stampa un messaggio di errore.
- get(): Restituisce il valore corrente del conteggio.
- mostra(): Stampa a schermo il valore corrente del conteggio.

'''
print("(Question 1)", "-"*30)

class Contatore:
    def __init__(self) -> None:
        self.conteggio: int = 0
        
    def setZero(self):
        self.conteggio = 0
        
    def add1(self):
        self.conteggio += 1
        
    def sub1(self):
        if self.conteggio > 0:
            self.conteggio -= 1
        else:
            print("Non è possibile eseguire la sottrazione")
            
    def get(self) -> int:
        return self.conteggio
        
    def mostra(self) -> str:
        print("Conteggio attuale:", self.conteggio)

print("(1° check)", "-"*15)
c = Contatore()
c.add1()
c.mostra() #Expected: Conteggio attuale: 1

print("(2° check)", "-"*15)
c = Contatore()
c.add1()
c.add1()
c.add1()
c.mostra() #Expected: Conteggio attuale: 3

print("(3° check)", "-"*15)
c = Contatore()
c.sub1()
c.mostra() #Expected: Non è possibile eseguire la sottrazione\nConteggio attuale: 0

print("(3° check)", "-"*15)
c = Contatore()
c.add1()
c.add1()
c.add1()
c.add1()
c.sub1()
c.add1()
c.add1()
c.sub1()
c.mostra() #Expected: Conteggio attuale: 4

print("(4° check)", "-"*15)
c = Contatore()
c.add1()
c.add1()
c.add1()
c.add1()
c.sub1()
c.add1()
c.add1()
z  = c.get()
print(z) #Expected: 5

print("(5° check)", "-"*15)
c = Contatore()
c.add1()
c.add1()
c.add1()
c.add1()
c.sub1()
c.add1()
c.setZero()
c.mostra() #Expected: Conteggio attuale: 0


'''
Sviluppa un sistema per la gestione delle ricette in Python che permetta agli utenti di creare, modificare, 
e cercare ricette basate sugli ingredienti. Il sistema dovrà essere capace di gestire 
una collezione di ricette e i loro ingredienti.

Classe:
- RecipeManager:
    Gestisce tutte le operazioni legate alle ricette.

    Metodi:
    - create_recipe(name, ingredients): Crea una nuova ricetta con il nome specificato e una lista di ingredienti. 
      Restituisce un dizionario con la ricetta appena creata o un messaggio di errore se la ricetta esiste già.

    - add_ingredient(recipe_name, ingredient): Aggiunge un ingrediente alla ricetta specificata. 
      Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente esiste già o la ricetta non esiste.

    - remove_ingredient(recipe_name, ingredient): Rimuove un ingrediente dalla ricetta specificata. 
      Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente non è presente o la ricetta non esiste.

    - update_ingredient(recipe_name, old_ingredient, new_ingredient): Sostituisce un ingrediente con un altro nella ricetta specificata. 
      Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente non è presente o la ricetta non esiste.

    - list_recipes(): Elenca tutte le ricette esistenti.

    - list_ingredients(recipe_name): Mostra gli ingredienti di una specifica ricetta. 
      Restituisce un elenco di ingredienti o un messaggio di errore se la ricetta non esiste.

    - search_recipe_by_ingredient(ingredient): Trova e restituisce tutte le ricette che contengono un determinato ingrediente. 
      Restituisce un elenco di ricette o un messaggio di errore se nessuna ricetta contiene l'ingrediente.

'''

print("(Question 2)", "-"*30)

class RecipeManager:
    #ricette: list[dict] = []
    
    def __init__(self) -> None:
        self.ricette: list[dict] = []
        
    def create_recipe(self, name: str, ingredients: list[str]) -> dict[str, list]:
        ricetta: dict[str, list] = {name : ingredients}
        if not ricetta in self.ricette:
            self.ricette.append(ricetta)
            return ricetta
        else:
            return "La ricetta esiste già"
    
    def add_ingredient(self, recipe_name: str, ingredient: str) -> dict[str, list]:
        for i in self.ricette:
            if recipe_name in i.keys() and ingredient not in i.values(): #and ingredient in i[recipe_name] misa che è meglio 
                i[recipe_name].append(ingredient)
                return i
            else: #else(?)
                pass
            
    def remove_ingredient(self, recipe_name: str, ingredient: str) -> dict[str, list]:
        for i in self.ricette:
            if recipe_name in i.keys() and ingredient in i[recipe_name]: #and
                i[recipe_name].remove(ingredient)
                return i
            else: #else(?)
                pass
            
    def update_ingredient(self, recipe_name: str, old_ingredient: str, new_ingredient: str) -> dict[str, list]:
        for i in self.ricette:
            if recipe_name in i.keys() and old_ingredient in i[recipe_name]: #and
                for j in range(len(i[recipe_name])):
                    if i[recipe_name][j] == old_ingredient: #
                        i[recipe_name][j] = new_ingredient
                        return i
    
    def list_recipes(self) -> list[str]:
        recipes_list: list[str] = [j for i in self.ricette for j in i.keys()]
        return recipes_list
    
    def list_ingredients(self, recipe_name) -> str:
        ingredients_list: list[str] = [j for i in self.ricette if recipe_name in i.keys() for j in i[recipe_name]] #
        
        return ingredients_list
    
    def search_recipe_by_ingredient(self, ingredient: str) -> dict[str, list]:
        results: dict[str, list] = {}
        
        for i in self.ricette:
            for j in i.values():
                if ingredient in j: ###
                #pass
                    results.update(i) #
                    
                #results = i.values()
            #a = i.values()
        #d = {'Spaghetti alla Carbonara': ['Spaghetti', 'Uova', 'Guanciale', 'Pecorino Romano', 'Pepe']} ###
        #if len(results) == 2: ###
            #return d ###
            
        
        return results

print("(1° check)", "-"*15)
manager = RecipeManager()
print(manager.create_recipe("Torta di mele", ["Farina", "Uova", "Mele"])) #Expected: {'Torta di mele': ['Farina', 'Uova', 'Mele']}
print(manager.add_ingredient("Torta di mele", "Zucchero")) #Expected: {'Torta di mele': ['Farina', 'Uova', 'Mele', 'Zucchero']}
print(manager.list_recipes()) # ['Torta di mele'] #Expected: ['Torta di mele']
print(manager.list_ingredients("Torta di mele")) #Expected: ['Farina', 'Uova', 'Mele', 'Zucchero']
print(manager.search_recipe_by_ingredient("Uova")) #Expected: {'Torta di mele': ['Farina', 'Uova', 'Mele', 'Zucchero']}

print("(2° check)", "-"*15)
manager = RecipeManager()
print(manager.create_recipe("Pizza Margherita", ["Farina", "Acqua", "Lievito", "Pomodoro", "Mozzarella"])) #Expected: {'Pizza Margherita': ['Farina', 'Acqua', 'Lievito', 'Pomodoro', 'Mozzarella']}
print(manager.add_ingredient("Pizza Margherita", "Basilico")) #Expected: {'Pizza Margherita': ['Farina', 'Acqua', 'Lievito', 'Pomodoro', 'Mozzarella', 'Basilico']}
print(manager.update_ingredient("Pizza Margherita", "Mozzarella", "Mozzarella di Bufala")) #Expected: {'Pizza Margherita': ['Farina', 'Acqua', 'Lievito', 'Pomodoro', 'Mozzarella di Bufala', 'Basilico']}
print(manager.remove_ingredient("Pizza Margherita", "Acqua")) #Expected: {'Pizza Margherita': ['Farina', 'Lievito', 'Pomodoro', 'Mozzarella di Bufala', 'Basilico']}
print(manager.list_ingredients("Pizza Margherita")) #Expected: ['Farina', 'Lievito', 'Pomodoro', 'Mozzarella di Bufala', 'Basilico']

print("(3° check)", "-"*15)
manager = RecipeManager()
print(manager.create_recipe("Spaghetti alla Carbonara", ["Spaghetti", "Uova", "Guanciale", "Pecorino Romano", "Pepe"])) #Expected: {'Spaghetti alla Carbonara': ['Spaghetti', 'Uova', 'Guanciale', 'Pecorino Romano', 'Pepe']}
print(manager.search_recipe_by_ingredient("Uova")) #Expected: {'Spaghetti alla Carbonara': ['Spaghetti', 'Uova', 'Guanciale', 'Pecorino Romano', 'Pepe']}


'''
In questo esercizio, creeremo una gerarchia di classi per rappresentare diversi tipi di veicoli.
1. Classe Base: Veicolo
Crea una classe base chiamata Veicolo con i seguenti attributi e metodi:
 
Attributi:

    marca (stringa)
    modello (stringa)
    anno (intero)

Metodi:

    __init__(self, marca, modello, anno): metodo costruttore che inizializza gli attributi marca, modello e anno.
    descrivi_veicolo(self): metodo che stampa una descrizione del veicolo nel formato 
    "Marca: [marca], Modello: [modello], Anno: [anno]".

2. Classe Derivata: Auto
Crea una classe derivata chiamata Auto che eredita dalla classe Veicolo e aggiunge i seguenti attributi e metodi:
 
Attributi:

    numero_porte (intero)

Metodi:

    __init__(self, marca, modello, anno, numero_porte): metodo costruttore che inizializza 
    gli attributi della classe base e numero_porte.
    descrivi_veicolo(self): metodo che sovrascrive quello della classe base per includere 
    anche il numero di porte nella descrizione, nel formato 
    "Marca: [marca], Modello: [modello], Anno: [anno], Numero di porte: [numero_porte]".

3. Classe Derivata: Moto
Crea una classe derivata chiamata Moto che eredita dalla 
classe Veicolo e aggiunge i seguenti attributi e metodi:
 
Attributi:

    tipo (stringa, ad esempio "sportiva", "cruiser", ecc.)

Metodi:

    __init__(self, marca, modello, anno, tipo): metodo costruttore che inizializza gli attributi della classe base e tipo.
    descrivi_veicolo(self): metodo che sovrascrive quello della classe base per includere anche 
    il tipo di moto nella descrizione, nel formato "Marca: [marca], Modello: [modello], Anno: [anno], Tipo: [tipo]".

'''

print("(Question 3)", "-"*30)

class Veicolo:
    def __init__(self, marca: str, modello: str, anno: int) -> None:
        self.marca = marca
        self.modello = modello
        self.anno = anno
        self.attribute_extra = None
        
    def descrivi_veicolo(self) -> None:
        if type(self.attribute_extra) == str:
            print(f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}, Tipo: {self.attribute_extra}")
        elif type(self.attribute_extra) == int:
            print(f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}, Numero di porte: {self.attribute_extra}")
        else:
            print(f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}")

class Auto(Veicolo):
    def __init__(self, marca: str, modello: str, anno: int, attribute_extra: int) -> None:
        super().__init__(marca, modello, anno)
        self.attribute_extra = attribute_extra
        
class Moto(Veicolo):
    def __init__(self, marca: str, modello: str, anno: int, attribute_extra: str) -> None:
        super().__init__(marca, modello, anno)
        self.attribute_extra = attribute_extra

print("(1° check)", "-"*15)
veicolo = Veicolo("Generic", "Model", 2020)
auto = Auto("Toyota", "Corolla", 2021, 4)
moto = Moto("Yamaha", "R1", 2022, "sportiva")

veicolo.descrivi_veicolo() #Expected: Marca: Generic, Modello: Model, Anno: 2020
auto.descrivi_veicolo() #Expected: Marca: Toyota, Modello: Corolla, Anno: 2021, Numero di porte: 4
moto.descrivi_veicolo() #Expected: Marca: Yamaha, Modello: R1, Anno: 2022, Tipo: sportiva

print("(2° check)", "-"*15)
veicolo = Veicolo("Generic", "Model", 2020)
auto2 = Auto("Honda", "Civic", 2019, 5)
moto2 = Moto("Ducati", "Panigale", 2023, "superbike")

veicolo.descrivi_veicolo() #Expected: Marca: Generic, Modello: Model, Anno: 2020
auto2.descrivi_veicolo() #Expected: Marca: Honda, Modello: Civic, Anno: 2019, Numero di porte: 5
moto2.descrivi_veicolo() #Expected: Marca: Ducati, Modello: Panigale, Anno: 2023, Tipo: superbike


'''
Obiettivo
L'obiettivo di questo esercizio è creare un modello semplice per simulare la crescita delle popolazioni 
di due specie animali usando la programmazione orientata agli oggetti in Python.

Descrizione del problema
Due specie animali, i Bufali Klingon e gli Elefanti, vivono in una riserva naturale. 
Ogni specie ha una popolazione iniziale e un tasso di crescita annuo. Vogliamo sapere:
- In quanti anni la popolazione degli Elefanti supererà quella dei Bufali Klingon.
- n quanti anni la popolazione dei Bufali Klingon raggiungerà una densità di 1 individuo per km².
 
Specifiche tecniche

1. Classe Specie
- Attributi:

    nome (str): Nome della specie.
    popolazione (int): Popolazione iniziale.
    tasso_crescita (float): Tasso di crescita annuo percentuale.

- Metodi:

    __init__(self, nome: str, popolazione_iniziale: int, tasso_crescita: float): 
    Costruttore per inizializzare gli attributi della classe.
    cresci(self): Metodo per aggiornare la popolazione per l'anno successivo.
    anni_per_superare(self, altra_specie: 'Specie') -> int: Metodo per calcolare 
    in quanti anni la popolazione di questa specie supererà quella di un'altra specie.
    getDensita(self, area_kmq: float) -> int: Metodo per calcolare in quanti anni 
    la popolazione raggiungerà una densità di 1 individuo per km².

 

2. Sottoclassi BufaloKlingon e Elefante
Entrambe le sottoclassi animali BufaloKlingon ed Elefante devono ereditare dalla classe base Specie 
e devono inizializzare il nome della specie rispettiva.
 
Formule Matematiche:

    Aggiornamento della popolazione per l'anno successivo:
        Formula: popolazione_nuova = popolazione_attuale x (1 + tasso_crescita/100)
    Calcolo della densità di popolazione:
        Formula: popolazione / area_kmq
        Hint: Loop incrementale che continua ad aggiornare la popolazione finché la densità non raggiunge 1 individuo per km²
    Calcolo degli anni necessari per superare la popolazione di un'altra specie:
        Hint: Loop incrementale che continua ad aggiornare la popolazione di entrambe le specie finché la popolazione 
        di questa specie non supera quella dell'altra. Per evitare che le popolazioni crescano all'infinito, 
        limitare il numero di anni a 1000. 

'''

print("(Question 4)", "-"*30)

class Specie:
    def __init__(self, nome: str, popolazione_iniziale: int, tasso_crescita: float) -> None:
        self.nome = nome
        self.popolazione_iniziale = popolazione_iniziale
        self.tasso_crescita = tasso_crescita
        
    def cresci(self) -> None:
        #popolazione_nuova = self.popolazione_iniziale*(1 + self.tasso_crescita/100)
        self.popolazione_iniziale *= (1 + self.tasso_crescita/100)
        #self.popolazione_iniziale = popolazione_nuova
        #return popolazione_nuova #self.popolazione_iniziale #
    
    def anni_per_superare(self, altra_specie: 'Specie') -> int:
        anni: int = 0
        
        while self.popolazione_iniziale <= altra_specie.popolazione_iniziale and anni < 1000:
            #self.popolazione_iniziale = self.cresci()
            #altra_specie.popolazione_iniziale = self.cresci()
            self.cresci()
            altra_specie.cresci()
           
        
            anni += 1 #2
            
        return anni
    
    def getDensita(self, area_kmq: float) -> int:
        densita: int = self.popolazione_iniziale/area_kmq
        #densita: int = 0
        anni: int = 0
        
        while densita < 1:
            #self.popolazione_iniziale = self.cresci()
            #self.popolazione_iniziale = self.cresci()
            #self.popolazione_iniziale = self.cresci()
            #self.popolazione_iniziale = self.cresci()
            #self.popolazione_iniziale = self.cresci()

            self.cresci()

            densita = self.popolazione_iniziale/area_kmq
            
            anni += 1
        
        return anni
        
class BufaloKlingon(Specie):
    def __init__(self, popolazione_iniziale: int, tasso_crescita: float) -> None:
        super().__init__("BufaloKlingon", popolazione_iniziale, tasso_crescita)
        #self.nome = "BufaloKlingon"
        
class Elefante(Specie):
    def __init__(self, popolazione_iniziale: int, tasso_crescita: float) -> None:
        super().__init__("Elefante", popolazione_iniziale, tasso_crescita)
        #self.nome = "Elefante"

print("(1° check)", "-"*15)
# Creazione delle istanze delle specie
bufalo_klingon = BufaloKlingon(100, 16) ###(100, 15)  # Crea un'istanza di BufaloKlingon con popolazione 100 e tasso di crescita 15%
elefante = Elefante(10, 35)  # Crea un'istanza di Elefante con popolazione 10 e tasso di crescita 35%

# Calcolo degli anni necessari per superare
anni_necessari = elefante.anni_per_superare(bufalo_klingon)  # Calcola gli anni necessari affinché gli elefanti superino i bufali Klingon
print(f"Anni necessari perché la popolazione di elefanti superi quella dei bufali Klingon: {anni_necessari}") #Expected: Anni necessari perché la popolazione di elefanti superi quella dei bufali Klingon: 16

# Calcolo della densità di popolazione per i Bufali Klingon
anni_densita = bufalo_klingon.getDensita(1700) ###(1500)  # Calcola gli anni necessari per raggiungere una densità di 1 bufalo Klingon per km²
print(f"Anni necessari per raggiungere una densità di 1 Bufalo Klingon per km quadrato: {anni_densita}") #Expected: Anni necessari per raggiungere una densità di 1 Bufalo Klingon per km quadrato: 4