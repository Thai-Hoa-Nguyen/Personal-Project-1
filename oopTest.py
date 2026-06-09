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
    def __init__(self, carType, carName):
        self.carType = carType
        self.carName = carName

    def fuelTypeDetection(self):
        #if ElectricCar => print Battery
        #if NormalCar => print Gas
        if self.carType == "1": #1 is for battery
            return f"Car: {self.carName}, Car Type: {self.carType == "Battery"}"
        
car1 = input(Vehicle)
