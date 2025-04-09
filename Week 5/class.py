from turtle import right


class Car:
    color = "red"  # class variable
    model = "BMW"  # class variable

    # Method to display car details
    def drive (self):
        print("The car is driving.")
    def stop (self):
        print("The car has stopped.")

my_car = Car()  # creating an instance of the Car class
my_car.drive()  # calling the instance method
my_car.stop()  # calling the instance method
print(my_car.color) # accessing the class variable using the instance

# self is just like a pointer which refers to the instance of the class the method is in
#refer to the instance of the class  and is used to access methods and variables within the class.

class Person:
    # Constructor method to initialize the object
    def __init__(self, name, age):  # constructor method
        self.name = name  # instance variable
        self.age = age    # instance variable
        self.height = height  # type: ignore # instance variable

personalDetails = Person("John", 30)  # creating an instance of the Person class
print(personalDetails.age)  # accessing the instance variable using the instance
#    def personDetails(self):
#        print(f"Name: {self.name}, Age: {self.age}")    

#def myPerson(name, age):
#    personName = name
 #   personAge = age
    # Method to display person details
   # def display(self):
    #    print(f"Name: {self.name}, Age: {self.age}")
#myPerson(print("Evans", 20))