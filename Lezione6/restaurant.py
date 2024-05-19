#9-10. Imported Restaurant: Using your latest Restaurant class, store it in a module. 
#Make a separate file that imports Restaurant. Make a Restaurant instance, 
#and call one of Restaurant's methods to show that the import statement is working properly.

#From 9-4

class Restaurant:
    def __init__(self, restaurant_name: str, cuisine_type: str) -> None:
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served: int = 0

    def describe_restaurant(self)  -> str:
        print(f"Restaurant = {self.restaurant_name}, Cuisine = {self.cuisine_type}")
    
    def open_restaurant(self) -> str:
        print("The restaurant is open")
    
    def set_number_served(self, number_served: int) -> int:
        self.number_served = number_served

    def increment_number_served(self, add_number_served: int) -> int:
        self.add_number_served = add_number_served
        self.number_served += self.add_number_served


restaurant_py: Restaurant = Restaurant("Thai Square", "Thai")