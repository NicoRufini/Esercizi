'''
Exercise 1: Creating an Abstract Class with Abstract Methods
Create an abstract class Shape with an abstract method area and another abstract method perimeter. 
Then, create two subclasses Circle and Rectangle that implement the area and perimeter methods.

Exercise 2: Implementing Static Methods
Create a class MathOperations with a static method add that takes two numbers and returns their sum, 
and another static method multiply that takes two numbers and returns their product.

Exercise 3: Library Management System 
Create a Book class containing the following attributes: title, author, isbn
The book class must contains the following methods:

    __str__ method to return a string representation of the book.

    @classmethod from_string(cls, book_str) to create a Book instance from a string in the format "title, author, isbn". 
    It means that you must use the class reference cls to create a new object of the Book class using a string.

Example: 

book = “La Divina Commedia, D. Alighieri, 999000666”
divina_commedia: Book = Book.from_string(book)
Here divina_commedia must contain an instance of the class Book with 

title = La Divina Commedia, author = D. Alighieri, isbn = 999000666

Create a Member class with the following attributes: name, member_id, borrowed_books
The member class must contain the following methods:

    borrow_book(book) to add a book to the borrowed_books list.

    return_book(book) to remove a book from the borrowed_books list.

    __str__ method to return a string representation of the member.

    @classmethod from_string(cls, member_str) to create a Member instance from a string in the format "name, member_id".

Create a Library class with the following attributes: books, members, total_books 
(class attribute to keep track of the total number of books)
The library class must contain the following methods:

    add_book(book) to add a book to the library and increment total_books.

    remove_book(book) to remove a book from the library and decrement total_books.

    register_member(member) to add a member to the library.

    lend_book(book, member) to lend a book to a member. It should check if the book is available and if the member is registered.

    __str__ method to return a string representation of the library with the list of books and members.

    @classmethod library_statistics(cls) to print the total number of books.

Create a script and play a bit with the classes:
Create instances of books and members using class methods. Register members and add books to the library. 
Lend books to members and display the state of the library before and after lending.

Exercise 4: University Management System
Create a system to manage a university with departments, courses, professors, and students. 

Create an abstract class Person:
Attributes:

    name (string)
    age (int)

Methods:

    __init__ method to initialize the attributes.
    Abstract method get_role to be implemented by subclasses.
    __str__ method to return a string representation of the person.

Create subclasses Student and Professor that inherit from Person and implement the abstract methods:

Student:
Additional attributes: student_id (string), courses (list of Course instances)
Method enroll(course) to enroll the student in a course.
Professor:
Additional attributes: professor_id (string), department (string), courses (list of Course instances)
Method assign_to_course(course) to assign the professor to a course.


Create a class Course:
Attributes:

    course_name (string)
    course_code (string)
    students (list of Student instances)
    professor (Professor instance)

Methods:

    __init__ method to initialize the attributes.
    add_student(student) to add a student to the course.
    set_professor(professor) to set the professor for the course.
    __str__ method to return a string representation of the course.

Create a class Department:

Attributes:

    department_name (string)
    courses (list of Course instances)
    professors (list of Professor instances)


Methods:

    __init__ method to initialize the attributes.
    add_course(course) to add a course to the department.
    add_professor(professor) to add a professor to the department.
    __str__ method to return a string representation of the department.

Create a class University:

Attributes:

    name (string)
    departments (list of Department instances)
    students (list of Student instances)


Methods:

    __init__ method to initialize the attributes.
    add_department(department) to add a department to the university.
    add_student(student) to add a student to the university.
    __str__ method to return a string representation of the university.


Create a script:

Create instances of departments, courses, professors, and students.
Add them to the university.
Enroll students in courses and assign professors to courses.
Display the state of the university.
'''
#####
'''
#Exercise 1: Creating an Abstract Class with Abstract Methods
from abc import ABC, abstractmethod
import math

class Figure(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Figure):
    def area(self, radius: float):
        self.radius = radius
        circle_area: float = math.pi*self.radius**2

        print(circle_area)
        return super().area()
    
    def perimeter(self, radius: float):
        self.radius = radius
        perimeter_area: float = 2*math.pi*self.radius

        print(perimeter_area)
        return super().perimeter()

class Rectangle(Figure):
    def area(self, base: float, height: float):
        self.base = base
        self.height = height
        rectangle_area: float = self.base*self.height

        print(rectangle_area)
        return super().area()
    
    def perimeter(self, base: float, height: float):
        self.base = base
        self.height = height
        rectangle_perimeter: float = 2*(self.base + self.height)

        print(rectangle_perimeter)
        return super().perimeter()
    
cirle0: Circle = Circle()
rectangle0: Rectangle = Rectangle()

cirle0.area(5)
cirle0.perimeter(5)
rectangle0.area(7, 15)
rectangle0.perimeter(7, 15)
'''
#Exercise 2: Implementing Static Methods
class MathOperations:

    @staticmethod
    def add(number_1: float, number_2: float):
        return number_1 + number_2
    
    @staticmethod
    def multiply(number_1: float, number_2: float):
        return number_1*number_2

math: MathOperations = MathOperations

print(math.add(5, 2))
print(math.multiply(5, 2))
#Exercise 3: Library Management System
#Create a Book class
class Book:
    def __init__(self, title: str, author: str, isbn: str) -> None:
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self) -> str:
        return f"book(title = {self.title}, author = {self.author}, isbn = {self.isbn})"
    
    @classmethod
    def from_string(cls, book_str: str) -> str:
        book_str: list = book_str.split(", ")

        if len(book_str) == 3:
            return f"book(title : {book_str[0]}, author : {book_str[1]}, isbn : {book_str[2]})"
        
book_0: Book = Book("La Divina Commedia", "D. Alighieri", "999000666")
book: str = "La Divina Commedia, D. Alighieri, 999000666"
book_1: Book = Book.from_string(book)

print("Without from_string:", book_0)
print("With from_string:", book_1)

#Create a Member class
class Member:
    def __init__(self, name: str, member_id: int) -> None:
        self.name = name
        self.member_id = member_id
        self.borrowed_books: list[Book] = []

    def borrow_book(self, book: Book):
        self.borrowed_books.append(book)
    
    def return_book(self, book: Book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
    
    def __str__(self) -> str:
        return f"member(name = {self.name}, member id = {self.member_id}, borrowed_books = {self.borrowed_books})"
    
    @classmethod
    def from_string(cls, member_str: str) -> str:
        member_str: list = member_str.split(", ")

        if len(member_str) == 2:
            return f"member(name = {member_str[0]}, member id = {member_str[1]})"

#Create a Library class
class Library:
    def __init__(self, books: list[Book], members: list[Member]) -> None:
        self.books = books
        self.members = members
        self.total_books: int = len(self.books)

    def add_book(self, book: Book):
        self.books.append(book)
        self.total_books += 1

    def remove_book(self, book: Book):
        if book in self.books:
            self.books.remove(book)
            self.total_books -= 1

    def register_member(self, member: Member):
        self.members.append(member)

    def lend_book(self, book: Book, member: Member):
        if member in self.members and book in self.books:
            member.borrowed_books.append(book)
            self.books.remove(book)
            self.total_books -= 1

    def __str__(self) -> str:
        return f"library(books = {self.books}, members = {self.members})"
    
    @classmethod
    def library_statistics(cls) -> str:
        return f"There are {cls().total_books} books in this library"

#Exercise 4: University Management System
from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name: str, age: int) -> None:
        super().__init__()
        self.name = name
        self.age = age

    @abstractmethod
    def get_role(self):
        pass

    def __str__(self) -> str:
        return f"person(name = {self.name}, age = {self.age})"
        #return super().__str__()

class Student(Person):
    def __init__(self, name: str, age: int, student_id: str) -> None:
        super().__init__(name, age)
        self.student_id = student_id
        self.courses: list = []

    def get_role(self, course):
        self.courses.append(course)
        return super().get_role()

class Professor(Person):
    def __init__(self, name: str, age: int, professor_id: str, department: str) -> None:
        super().__init__(name, age)
        self.professor_id = professor_id
        self.department = department
        self.courses: list = []

    def get_role(self, course):
        self.courses.append(course)
        return super().get_role()
    
class Course:
    def __init__(self, course_name: str, course_code: str) -> None:
        self.course_name = course_name
        self.course_code = course_code
        self.students: list[Student] = []
        self.professor: Professor = None

    def add_student(self, student: Student):
        self.students.append(student)

    def set_professor(self, professor):
        self.professor = professor

    def __str__(self) -> str:
        return f"course(name = {self.course_name}, code = {self.course_code}"\
             + f", students = {self.students}, professor = {self.professor})"
    
class Department:
    def __init__(self, department_name: str) -> None:
        self.department_name = department_name
        self.courses: list[Course] =[]
        self.professors: list[Professor] =[]

    def add_course(self, course: Course):
        self.courses.append(course)

    def add_professor(self, professor: Professor):
        self.professors.append(professor)

class University:
    def __init__(self, name: str) -> None:
        self.name = name
        self.departments: list[Department] = []
        self.students: list[Student] = []

    def add_department(self, department: Department):
        self.departments.append(department)

    def add_student(self, student: Student):
        self.students.append(student)

    def __str__(self) -> str:
        return f"university(name = {self.name}, departments = {self.departments}, students = {self.students})"