#   Creating A Class Dog

class Dog():
    """A simple attempt to model a dog"""

    def __init__(self, name, age):
        """Initialize name and age attributes"""
        self.name = name
        self.age = age
    
    def sit(self):
        """Simulate a dog sitting """
        print(self.name.title() + " is now sitting.")
    
    def roll_over(self):
        """Simulate Rolling over"""
        print(self.name.title() + " rolled Over!")

my_dog = Dog("James",14)
print("My dog name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

my_dog.sit()
my_dog.roll_over()

#   car class
class Car():
    """Modelling A Car"""

    def __init__(self, make, model, year):
        """Initializing Attributes Of The Car"""
        self.make = make
        self.model = model
        self.year = year

    def descriptive_name(self):
        """Returns A newly Formattd Car."""
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

new_car = Car('audi',"a4", 2016)
print(new_car.descriptive_name())

#   Creating A Restaurant Class
class Restaurant():
    """Modelling A Restaurant"""

    def __init__(self,restaurant_name,cuisine_type):
        """Initializing Attributes Of Restaurant"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 37

    def describe_restaurant(self):
        """Describes Your Restaurant"""
        print(self.restaurant_name.title() + " Restaurant Serves High Quality " + self.cuisine_type.title() + " .")
    
    def open_restaurant(self):
        """Show That The Restaurant Is Open"""
        print(self.restaurant_name.title() + " Is Now Open For Business.")
    
    def set_number_served(self,numb):
        """Set Numb Of Customers Served"""
        self.number_served = numb
        print(self.restaurant_name.title() + " Has Served "+ str(numb) + " Customers.")

    def increment_number_served(self,increment_value):
        """Increments The Number Of Customers Served"""
        if self.number_served >= 0:
            increased_val = self.number_served + increment_value
            print("The Number Of Customers Has Been Increased To" , increased_val)


la_grande = Restaurant("la_grande","grande fishe")
print("\n" + la_grande.restaurant_name)
print(la_grande.cuisine_type)
la_grande.describe_restaurant()
la_grande.open_restaurant()

Scoop_Haven = Restaurant("Scoop Haven", "Ice cream")
Scoop_Haven.describe_restaurant()

Chick_Repub = Restaurant("Chicken Republic", "Chickens")
Chick_Repub.describe_restaurant()

Genesis = Restaurant("Genesis", "fast Food")
Genesis.describe_restaurant()

restaurant1 = Restaurant("jevenic", "Chinese Food")
restaurant1.set_number_served(5)
restaurant1.increment_number_served(23)