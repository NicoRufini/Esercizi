"""
Sistema di gestione dello zoo virtuale
Classi:
1. Zoo: questa classe rappresenta uno zoo. Lo zoo ha dei recinti fences e dei guardiani dello zoo, zoo_keepers.
2. Animal: questa classe rappresenta un animale nello zoo. Ogni animale ha questi attributi: name, species, age, 
   height, width, preferred_habitat, health che è uguale a round(100 * (1 / age), 3).
3. Fence: questa classe rappresenta un recinto dello zoo in cui sono tenuti gli animali. I recinti possono contenere uno o più animali. 
   I recinti possono hanno gli attributi area, temperature e habitat.
4. ZooKeeper: questa classe rappresenta un guardiano dello zoo responsabile della gestione dello zoo. I guardiani dello zoo hanno un name, 
   un surname, e un id. Essi possono nutrire gli animali, pulire i recinti e svolgere altri compiti nel nostro zoo virtuale.

Funzionalità:
1. add_animal(animal: Animal, fence: Fence) (Aggiungi nuovo animale): consente al guardiano dello zoo di aggiungere un nuovo animale allo 
   zoo. L'animale deve essere collocato in un recinto adeguato in base alle esigenze del suo habitat e se c'è ancora spazio nel recinto, 
   ovvero se l'area del recinto è ancora sufficiente per ospitare questo animale.
2. remove_animal(animal: Animal, fence: Fence) (Rimuovi animale): consente al guardiano dello zoo di rimuovere un animale dallo zoo. 
   L'animale deve essere allontanato dal suo recinto. Nota bene: L'area del recinto deve essere ripristinata dello spazio 
   che l'animale rimosso occupava.
3. feed(animal: Animal) (Dai da mangiare agli animali): implementa un metodo che consenta al guardiano dello zoo di nutrire 
   tutti gli animali dello zoo. Ogni volta che un animale viene nutrito, la sua salute incrementa di 1% rispetto alla sua salute corrente, 
   ma le dimensioni dell'animale (height e width) vengono incrementate del 2%. Perciò, l'animale si può nutrire soltanto se il recinto ha 
   ancora spazio a sufficienza per ospitare l'animale ingrandito dal cibo.
4. clean(fence: Fence) (Pulizia dei recinti): implementare un metodo che consenta al guardiano dello zoo 
   di pulire tutti i recinti dello zoo. 
   Questo metodo restituisce un valore di tipo float che indica il tempo che il guardiano impiega per pulire il recinto. 
   Il tempo di pulizia è il rapporto dell'area occupata dagli animali diviso l'area residua del recinto. Se l'area residua è pari a 0, 
   restituire l'area occupata.
5. describe_zoo() (Visualizza informazioni sullo zoo): visualizza informazioni su tutti i guardani dello zoo, sui recinti dello zoo che 
   contengono animali. 
E.s.: Se abbiamo un guardiano chiamato Lorenzo Maggi con matricola 1234, e un recinto Fence(area=100, temperature=25, habitat=Continentale) 
      con due animali Animal(name=Scoiattolo, species=Blabla, age=25, ...), Animal(name=Lupo, species=Lupus, age=14,...) 
      ci si aspetta di avere una rappresentazione testuale dello zoo come segue:

Guardians:

ZooKeeper(name=Lorenzo, surname=Maggi, id=1234)

Fences:

Fence(area=100, temperature=25, habitat=Continent)

with animals:

Animal(name=Scoiattolo, species=Blabla, age=25)

Animal(name=Lupo, species=Lupus, age=14)
#########################

Fra un recinto e l'altro mettete 30 volte il carattere #."""
################
'''
animals:
name = "Wolf", species = "Lupus", age = 14,height = 85, width = 160, preferred_habitat = "mountains"

Fences:
area = -100, temperature = 25, habitat = "Continent"

Zookeepers are not important
'''
#####
###
'''
class Zoo: 
    def __init__(self, fences: int, zoo_keepers: int) -> None: #fences: ?
        self.fences = fences
        self.zoo_keepers = zoo_keepers

    def __str__(self) -> str:
        return f"Zoo(fences = {self.fences}, zoo_keepers = {self.zoo_keepers})" '''###
'''
class Animal:
    def __init__(self, name: str, species: str, age: int, height: int, width: float, preferred_habitat: str) -> None: #, health) #width: ?
        self.name = name
        self.species = species
        self.age = age
        self.height = height
        self.width = width
        self.preferred_habitat = preferred_habitat 
        #self.health = health # round(100 * (1 / age), 3)
        #self.set_health()

    def set_health(self):
        self.health: float = round(100 * (1 / self.age), 3)
        return self.health

    def __str__(self) -> str:
        return f"Animal(name = {self.name}, species = {self.species}, age = {self.age}, height = {self.height}cm, "\
               f"width = {self.width}cm, preferred_habitat = {self.preferred_habitat}, health = {self.set_health()})" 

class Fence:
    def __init__(self, area: float, temperature: float, habitat: str) -> None:
        self.area = area #The area cannot have a negative value abs(area)
        self.temperature = temperature
        self.habitat = habitat
    
    def __str__(self) -> str:
        if self.area < 0:
            return "The area can't have a negative value."
        else:
            return f"Fence(area = {self.area}, temperature = {self.temperature}°C, habitat = {self.habitat})"

class ZooKeeper:
    def __init__(self, name: str, surname: str, id: str) -> None:
        self.name = name
        self.surname = surname
        self.id = id

    def __str__(self) -> str:
        return f"ZooKeeper(name = {self.name}, surname = {self.surname}, id = {self.id})" 

class Zoo:
    def __init__(self) -> None:
        self.fences = Fence(area = -100, temperature = 25, habitat = "Continent")
        self.zoo_keeper = ZooKeeper(name = "Lorenzo", surname = "Maggi", id = 1234)

    def __str__(self) -> str:
        return f"Guardians:\n\n{self.zoo_keeper}\n\nFences:\n\n{self.fences}\n\nwith animals:\n\n" '''

#Zoo keeper
'''print("-" * 100)
zoo_keeper_0 = ZooKeeper(name = "Lorenzo", surname = "Maggi", id = 1234)
print(zoo_keeper_0)
print("-" * 100)'''

#Fence
'''fence_0 = Fence(area = -100, temperature = 25, habitat = "Continent")
print(fence_0)
print("-" * 100)'''

#Animal
'''animal_0 = Animal(name = "Wolf", species = "Lupus", age = 14,height = 85, width = 160, preferred_habitat = "mountains")
print(animal_0)
print("-" * 100)
#print("#" * 30)'''

'''print(Zoo())'''

#####
"""
class Animal:
    def __init__(self, name: str, species: str, age: int, height: int, 
                 width: float, preferred_habitat: str) -> None: #, health) #width: ?
        self.name = name
        self.species = species
        self.age = age
        self.height = height
        self.width = width
        self.preferred_habitat = preferred_habitat 
        #self.health = health # round(100 * (1 / age), 3)
        #self.set_health()

    def set_health(self):
        self.health: float = round(100 * (1 / self.age), 3)
        return self.health

    def __str__(self) -> str:
        return f"Animal(name = {self.name}, species = {self.species}, age = {self.age}, height = {self.height}cm, "\
               f"width = {self.width}cm, preferred_habitat = {self.preferred_habitat}, health = {self.set_health()})" 
'''
class Fence:
    def __init__(self, area: float, temperature: float, habitat: str) -> None: #list_animal: list[Animal])
        self.area = area #The area cannot have a negative value abs(area)
        self.temperature = temperature
        self.habitat = habitat
        #self.list_animal = list_animal

    def set_list_animal(self):
        self.list_animal: list[Animal] = []
        
        if Animal(self, name: str != None, species: str != None, age: int != None, height: int != None, width: float != None, preferred_habitat: str != None):
            self.list_animal.append(Animal)
        
        return self.list_animal
    
    def __str__(self) -> str:
        if self.area < 0:
            return f"Fences:\n\nThe area can't have a negative value.\n\nwith animals:\n\n{self.set_list_animal()}"
        else:
            return f"Fences:\n\nFence(area = {self.area}, temperature = {self.temperature}°C, habitat = {self.habitat})" \
                   f"\n\nwith animals:\n\n{self.set_list_animal()}" '''

#Fence deve essere figlia di animal
#Riprova la prima Fence (quella non figlia)
class Fence(Animal):
    def __init__(self,  name: str, species: str, age: int, height: int, width: float, preferred_habitat: str,
                 area: float, temperature: float, habitat: str) -> None:
        super().__init__(name, species, age, height, width, preferred_habitat)
        self.area = area #The area cannot have a negative value abs(area)
        self.temperature = temperature
        self.habitat = habitat

    def set_list_animal(self):
        self.list_animal: list[Animal] = []
        if self.name != None and self.species != None and self.age != None and self.height != None \
            and self.width != None and self.preferred_habitat != None:
            self.list_animal.append(Animal)
        
        return self.list_animal
    
    def __str__(self) -> str:
        if self.area < 0:
            return f"Fences:\n\nThe area can't have a negative value.\n\nwith animals:\n\n{self.set_list_animal()}"
        else:
            return f"Fences:\n\nFence(area = {self.area}, temperature = {self.temperature}°C, habitat = {self.habitat})" \
                   f"\n\nwith animals:\n\n{self.set_list_animal()}"
        
animal_0 = Animal(name = "Wolf", species = "Lupus", age = 14,height = 85, width = 160, preferred_habitat = "mountains")
print(animal_0)
print("-" * 100)

fence_0 = Fence(area = -100, temperature = 25, habitat = "Continent")
print(fence_0)"""

#####
###
'''
class Zoo: 
    def __init__(self, fences: int, zoo_keepers: int) -> None: #fences: ?
        self.fences = fences
        self.zoo_keepers = zoo_keepers

    def __str__(self) -> str:
        return f"Zoo(fences = {self.fences}, zoo_keepers = {self.zoo_keepers})" '''###

class Animal: #class Animal(object) maybe (in some way) class Animal can return a list instead of class Fences
    def __init__(self, name: str, species: str, age: int, height: int, width: float, preferred_habitat: str) -> None: #, health) #width: ?
        self.name = name
        self.species = species
        self.age = age
        self.height = height
        self.width = width
        self.preferred_habitat = preferred_habitat 
        #self.health = health # round(100 * (1 / age), 3)
        self.set_health()

    def set_health(self):
        self.health: float = round(100 * (1 / self.age), 3)
        #return self.health

    def __str__(self) -> str:
        return f"Animal(name = {self.name}, species = {self.species}, age = {self.age}, height = {self.height}cm, "\
               f"width = {self.width}cm, preferred_habitat = {self.preferred_habitat}, health = {self.health})" 

class Fence: #class Fence(object) **fences(?)
    def __init__(self, area: float, temperature: float, habitat: str) -> None: #, class_animal: Animal set_list_animal
        self.area = area #The area cannot have a negative value abs(area)
        self.temperature = temperature
        self.habitat = habitat
        self.animal: list[Animal] = []

    #def set_list_animal(self): #@classmethod of set_list_animal and call it in Fence add_animal(?)
        #self.list_animal: list[Animal] = [self.animal] #[self.animal]
        #self.other_list_animal: list = [] #self.list_animal.append(self.animal)(?)
        #for i in self.list_animal:
            #self.other_list_animal.append(i)
            #return i #return? try print()
        

###@@ ###@@ ###@@ ###@@ ###@@ ###@@ ###@@@


    
    def __str__(self) -> str:
        fence_string: str = ""
        if self.area >= 0:
            fence_string = f"Fence(area = {self.area}m², temperature = {self.temperature}°C, habitat = {self.habitat})\n\n"\
                           f"with animals:\n\n"
            for i in self.animal:
                fence_string +=  f"{i.__str__()}\n"    
            return f"{fence_string}" + "#" * 30
            

class ZooKeeper: #class ZooKeeper(object) **zookeepers(?)
    def __init__(self, name: str, surname: str, id: str) -> None:
        self.name = name
        self.surname = surname
        self.id = id

    def add_animal(self, animal: Animal, fence: Fence) -> Animal: #, fence: Fence)
        self.animal = animal
        self.fence = fence
        #self.fence = fence
        if animal.preferred_habitat == fence.habitat:
            self.fence.animal.append(self.animal)

    def remove_animal(self, animal: Animal, fence: Fence) -> Animal: #, fence: Fence
        self.animal = animal
        self.fence = fence
        if animal.preferred_habitat == fence.habitat:
            self.fence.animal.remove(self.animal)

    def feed(self, animal: Animal) -> Animal:
        self.animal = animal
        animal.health += 0.01 * animal.health
        animal.height += 0.02 * animal.height
        animal.width += 0.02 * animal.width
        animal.health = round(animal.health, 3)
        animal.height = round(animal.height, 3)
        animal.width = round(animal.width, 3)

    def clean(self, fence: Fence) -> Fence: #class_fence(?) #calculate animal area = width * height, maybe on class Fence calculate it
        self.fence = fence
        self.clean_time = None #Il tempo di pulizia è il rapporto dell'area occupata dagli animali diviso l'area residua del recinto.  
        #Se l'area residua è pari a 0, restituire l'area occupata.


    def __str__(self) -> str:
        return f"ZooKeeper(name = {self.name}, surname = {self.surname}, id = {self.id})" 

class Zoo: #**fences **zookeepers
    def __init__(self, fences: list[Fence], zoo_keepers: list[ZooKeeper]) -> None: #zoo_keepers e fences sono delle liste
        self.fences = fences
        self.zoo_keepers = zoo_keepers
    
    def describe_zoo(self) -> str:
        #return f"Guardians:\n\n{self.zoo_keepers}\n\nFences:\n\n{self.fences}"
        zoo_zoo_keepers_string: str = "Guardians:\n\n"
        zoo_fences_string: str = "Fences:\n\n"

        for i in self.zoo_keepers:
            zoo_zoo_keepers_string += f"{i.__str__()}\n"

        for i in self.fences:
            zoo_fences_string += f"{i.__str__()}\n\n"

        return f"{zoo_zoo_keepers_string}\n{zoo_fences_string}"
    
        '''
        zoo_zoo_keepers_string: str = "Guardians:\n\n"
        zoo_fences_string: str = "Fences:\n\n"

        for i in self.zoo_keepers:
            zoo_zoo_keepers_string += f"{i.__str__()}\n"
        
        for i in self.fences:
            zoo_fences_string += f"{i.__str__()}\n"

        return f"{zoo_zoo_keepers_string}\n\n{zoo_fences_string}"
        ''' 

#Animal
animal_forest_1 = Animal(name = "Wolf", species = "Lupus", age = 14, height = 85, width = 160, preferred_habitat = "Forest")
#animal_forest_2 = Animal(name = "Squirrel", species = "Chipmunk", age = 6, height = 18, width = 15, preferred_habitat = "Forest")
#animal_forest_3 = Animal(name = "Tiger", species = "Bnegal tiger", age = 12, height = 110, width = 190, preferred_habitat = "Forest")
#animal_acquatic_1 = Animal(name = "Sea turtle", species = "Hawksbill", age = 75, height = 44, width = 86, preferred_habitat = "Acquatic")
#animal_polar_1 = Animal(name = "Penguin", species = "Pygoscelis adeliae", age = 17, height = 65, width = 14, preferred_habitat = "Polar")
#animal_polar_2 = Animal(name = "Sea lion", species = "Eumetopias jubatus", age = 21, height = 89, width = 37, preferred_habitat = "Polar")
#print(animal_0)
#print("-" * 100)
#print("#" * 30)

#Fence
fence_forest = Fence(area = 100, temperature = 25, habitat = "Forest") #, class_animal = animal_0
#fence_acquatic = Fence(area = 25, temperature = 20, habitat = "Acquatic")
#fence_polar = Fence(area = 75, temperature = 0, habitat = "Polar")
#print(fence_0)
#print("-" * 100)

#Zoo keeper
#print("-" * 100)
zoo_keeper_0 = ZooKeeper(name = "Lorenzo", surname = "Maggi", id = 1234)
#print(zoo_keeper_0)
#print("-" * 100)

#add_animal
#zoo_keeper_0.add_animal(animal = animal_forest_1, fence = fence_forest) #fence = fence_0, animal = animal_0
#zoo_keeper_0.add_animal(animal = animal_forest_2, fence = fence_forest)
#zoo_keeper_0.add_animal(animal = animal_forest_3, fence = fence_forest)
#zoo_keeper_0.add_animal(fence = fence_acquatic, animal = animal_acquatic_1)
#print(zoo_keeper_0.add_animal(fence = fence_0, animal = animal_0))
#print(zoo_keeper_0.add_animal(fence = fence_0, animal = animal_0))

#remove_animal
#zoo_keeper_0.remove_animal(animal = animal_forest_1, fence = fence_forest)
#zoo_keeper_0.remove_animal(animal = animal_forest_2, fence = fence_forest)
#zoo_keeper_0.remove_animal(animal = animal_forest_3, fence = fence_forest)
#zoo_keeper_0.remove_animal(fence = fence_acquatic, animal = animal_acquatic_1)

#feed
#zoo_keeper_0.feed(animal = animal_forest_1)
#zoo_keeper_0.feed(animal = animal_forest_1)
#zoo_keeper_0.feed(animal = animal_forest_2)
#zoo_keeper_0.feed(animal = animal_forest_2)
#zoo_keeper_0.feed(animal = animal_forest_3)
#zoo_keeper_0.feed(animal = animal_forest_3)
#zoo_keeper_0.feed(animal = animal_acquatic_1)
#zoo_keeper_0.feed(animal = animal_acquatic_1)

#clean

#Zoo
zoo_park= Zoo(fences = [fence_forest], zoo_keepers = [zoo_keeper_0])
print(zoo_park.describe_zoo())

#Do the functions first, then **fences and **zookeepers
################
'''
animals:
name = "Wolf", species = "Lupus", age = 14, height = 85, width = 160, preferred_habitat = "mountains", "forests"
name = "Squirrel", species = "Chipmunk", age = 6, height = 18, width = 15, preferred_habitat = "forests"
name = "Tiger", species = "Bnegal tiger", age = 12, height = 110, width = 190, preferred_habitat = "forests", "savannah", "swamps"
name = "Penguin", species = "Pygoscelis adeliae", age = 17, height = 65, width = 14, preferred_habitat = "ocean", "coasts", "Polar"
name = "Sea lion", species = "Eumetopias jubatus", age = 21, height = 89, width = 37, preferred_habitat = "ocean", "coasts", "Polar"
name = "Sea turtle", species = "Hawksbill", age = 75, height = 44, width = 86, preferred_habitat = "ocean", "coasts", "Tropical"


Fences:
area = 100, temperature = 25, habitat = "Continent"
area = 100, temperature = 25, habitat = "Forest" #Wolf, Squirrel, Tiger
area = 25, temperature = 20, habitat = "Acquatic" #Sea turtle
area = 100, temperature = 25, habitat = "Dessert"
area = 100, temperature = 25, habitat = "Mountainous"
area = 75, temperature = 0, habitat = "Polar" #Penguin, Sea lion
area = 100, temperature = 25, habitat = "Tropical"

Zookeepers are not important
'''