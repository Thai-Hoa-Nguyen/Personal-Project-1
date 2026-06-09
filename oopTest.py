#Create a class, create objects in OOP
print("======EXERCISE 1======")
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = int(pages)

    def display(self):
        return f"Title: {self.title} by {self.author}, Page: {self.pages}"
    
book1 = Book("Harry Portter","J. K. Rowling",67)
book2 = Book("Shoe Dog: A Memoir by the Creator of Nike","Phil Knight", 40 )

print(book1.display())
print(book2.display())
print("======EXERCISE 1 END======")
print("======EXERCISE 2======")
class Vehicle:
    def __init__(self, carType):
        self.carType = carType
    
    def fuel_type(self):
        return f"{self.carType}"

class ElectricCar(Vehicle):
        def fuel_type(self):
            return f"Battery {self.carType}"
        
class GasCar(Vehicle):
        def fuel_type(self):
            return f"Gas {self.carType}"

car1 = ElectricCar("Tesla")
car2 = GasCar("RAM")

print(car1.fuel_type())
print(car2.fuel_type())
print("======EXERCISE 2 END======")
print("======EXERCISE 3======")

