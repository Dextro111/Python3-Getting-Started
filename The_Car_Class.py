class Car():
    """A simple attempt to rep a car."""

    def __init__(self, make, model, year):
        """Initialize attributes of the car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 1000
    
    def get_descriptive_name(self):
        """Returns A Formatted Descriptive name."""
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()
    
    def read_odometer(self):
        """Print Statement showing the cars Mileage."""
        print("This car Has " + str(self.odometer_reading) + " Miles On It")

    def update_odometer(self, mileage):
        """Set the odometer reading to a given value. Reject change if value decreases"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("Odometer Reading doesnt decrease")
    
    def increment_odometer(self, miles):
        """Add the given amount to odometer reading"""
        self.odometer_reading += miles

class ElectricCar(Car):
    """Reps Apects of A Car, For Electric vehicles."""

    def __init__(self, make, model, year):
        """
        Init Attrib of Parent Class.
        Then For only Electric CAR
        """
        super().__init__(make, model, year)
        self.battery = Battery()
    
    ##    """Prints A Battery descr statement"""
     #   print("This car has A " + str(self.battery) + "-Kwh battery.") 

class Battery():
    """A Model for a battery of an electric car"""

    def __init__(self, battery_size=70):
        """Initialize battery attributes"""
        self.battery_size = battery_size
        
    def describe_battery(self):
        """Print A Statement Describ battery size"""
        print("This Car has a " + str(self.battery_size) + "-Kwh battery")

tesla = ElectricCar("Tesla", "AUX", 2043)
print(tesla.get_descriptive_name())
tesla.battery.describe_battery()

used_car = Car("lexus", "360", 2037)
print(used_car.get_descriptive_name())
used_car.update_odometer(39000)
used_car.read_odometer()
used_car.increment_odometer(300)
used_car.read_odometer()

new_car = Car("Mercedes", "DX", 2027)
print(new_car.get_descriptive_name())
new_car.update_odometer(360)
new_car.read_odometer()