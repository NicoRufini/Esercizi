#9-11. Imported Admin: Start with your work from Exercise 9-8. Store the classes User, Privileges, and Admin in one module. 
#Create a separate file, make an Admin instance, and call show_privileges() to show that everything is working correctly.

#From 9-5
class User:
    def __init__(self, first_name: str, last_name: str, email: str, phone_number: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.login_attempts: int = 0

    def describe_user(self) -> str:
        print(f"name = {self.first_name}, surname = {self.last_name}, email = {self.email}, phone number = {self.phone_number}")
    
    def greet_user(self) -> str:
        print(f"Hi {self.first_name} {self.last_name}!")

    def increment_login_attempts(self) -> int:
        self.login_attempts += 1

    def reset_login_attempts(self) -> int:
        self.login_attempts = 0

#From 9-8
class Privileges:
    def __init__(self, privileges: list[str]) -> None:
        self.privileges = privileges
        #self.privileges: list[str] = ["can add post", "can delete post", "can ban user"]
    
    def show_privileges(self)  -> str:
        string_privileges: str = "Your privileges: "
        for i in range(len(self.privileges)):
            if self.privileges[i] != self.privileges[-1]:
                string_privileges += f"{self.privileges[i].__str__()}, "

        string_privileges += f"{self.privileges[-1].__str__()}"
        
        print(string_privileges)

class Admin(User):
    def __init__(self, first_name: str, last_name: str, email: str, phone_number: str, privileges: Privileges) -> None:
        super().__init__(first_name, last_name, email, phone_number)
        self.privileges = privileges

privileges_py: Privileges = Privileges(["can add post", "can ban users", "can delete post"])
admin_py: Admin = Admin("Marisol", "Normann", "fakeemailnumber3@gmail.com", "555-738 264 261", privileges_py)