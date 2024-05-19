#9-12. Multiple Modules: Store the User class in one module, and store the Privileges and Admin classes in a separate module. 
#In a separate file, create an Admin instance and call show_privileges() to show that everything is still working correctly.

from user import User

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

privileges_2_py: Privileges = Privileges(["can ban users"])
admin_2_py: Admin = Admin("Nora", "James", "fakeemailnumber4@gmail.com", "555-0731 82 82 41", privileges_2_py)