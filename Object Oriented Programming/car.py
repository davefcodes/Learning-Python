#Working with classes and Instances 
class Car:
    "A simple attempt to represent a car."

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """"Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

my_new_car = Car('audi', 's7', '2023') # we make an instance from the Car class and assigned it to the variable
print(my_new_car.get_descriptive_name())


#Setting a Default Value for an Attribute
class Car:
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it.")

my_new_car = Car('audi', 's8', '2022')
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

#Modifying an Attribute's value directly 
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# Modifying an Attribute's Value Through a Method
class Car:
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def update_odometer(self,mileage):
        """Set the odometer reading to the given value."""
        self.odometer_reading = mileage

    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it.")

my_new_car = Car('audi', 's8', '2022')
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(25)
my_new_car.read_odometer()