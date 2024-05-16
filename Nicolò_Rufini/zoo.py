#Nicolò Rufini

class Animal:
    def __init__(self, name: str, species: str, age: int, height: float, width: float, preferred_habitat: str) -> None:
        self.name = name
        self.species = species
        self.age = age
        self.height = height
        self.width = width
        self.preferred_habitat = preferred_habitat 
        self.set_health()

    def set_health(self):
        self.health: float = round(100 * (1 / self.age), 3)

    def __str__(self) -> str:
        return f"Animal(name = {self.name}, species = {self.species}, age = {self.age}, height = {self.height}cm, "\
               f"width = {self.width}cm, preferred_habitat = {self.preferred_habitat}, health = {self.health})" 


class Fence:
    def __init__(self, area: float, temperature: float, habitat: str) -> None:
        self.area = area
        self.temperature = temperature
        self.habitat = habitat
        self.animal: list[Animal] = []
        self.occupied_area: float = 0
    
    def __str__(self) -> str:
        fence_string: str = ""
        if self.area >= 0:
            fence_string = f"Fence(area = {self.area}m², temperature = {self.temperature}°C, habitat = {self.habitat})\n\n"\
                           f"with animals:\n\n"
            for i in self.animal:
                fence_string +=  f"{i.__str__()}\n"    
            return f"{fence_string}" + "#" * 30


class ZooKeeper:
    def __init__(self, name: str, surname: str, id: str) -> None:
        self.name = name
        self.surname = surname
        self.id = id

    def add_animal(self, animal: Animal, fence: Fence) -> Animal:
        self.animal = animal
        self.fence = fence
        fence.occupied_area += animal.width * animal.height
        self.residual_area: float = fence.area - fence.occupied_area
        if animal.preferred_habitat == fence.habitat and fence.occupied_area <= fence.area:
            self.fence.animal.append(self.animal)
        else:
            fence.occupied_area -= animal.width * animal.height

    def remove_animal(self, animal: Animal, fence: Fence) -> Animal:
        self.animal = animal
        self.fence = fence
        if animal.preferred_habitat == fence.habitat:
            self.fence.animal.remove(self.animal)
            fence.occupied_area -= animal.width * animal.height
            self.residual_area += animal.width * animal.height 

    def feed(self, animal: Animal) -> Animal: 
        self.animal = animal                  
        if self.residual_area > 0:
            animal.health += 0.01 * animal.health
            animal.height += 0.02 * animal.height
            animal.width += 0.02 * animal.width
            animal.health = round(animal.health, 3)
            animal.height = round(animal.height, 3)
            animal.width = round(animal.width, 3)
            self.residual_area -= (animal.height * animal.width)

    def clean(self, fence: Fence) -> Fence:
        self.fence = fence                  
        self.residual_area: float = fence.area - fence.occupied_area 
        if self.residual_area != 0:
            self.clean_time: float = fence.occupied_area / self.residual_area
            return f"Time: {round(self.clean_time, 3)}"
        else:
            return f"Time: {fence.occupied_area}"

    def __str__(self) -> str:
        return f"ZooKeeper(name = {self.name}, surname = {self.surname}, id = {self.id})" 


class Zoo:
    def __init__(self, fences: list[Fence], zoo_keepers: list[ZooKeeper]) -> None:
        self.fences = fences
        self.zoo_keepers = zoo_keepers
    
    def describe_zoo(self) -> str:
        zoo_zoo_keepers_string: str = "Guardians:\n\n"
        zoo_fences_string: str = "Fences:\n\n"
        for i in self.zoo_keepers:
            zoo_zoo_keepers_string += f"{i.__str__()}\n"

        for i in self.fences:
            zoo_fences_string += f"{i.__str__()}\n\n"

        return f"{zoo_zoo_keepers_string}\n{zoo_fences_string}"
    
