#9-12. Multiple Modules: Store the User class in one module, and store the Privileges and Admin classes in a separate module. 
#In a separate file, create an Admin instance and call show_privileges() to show that everything is still working correctly.

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