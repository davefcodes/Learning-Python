class Car:
    """A simple attempt to represent a car."""

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


    def update_odometer(self,mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back. 
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")


    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

    def fill_gas_tank(self):
        """Fill up the gas tank"""
        print("The gas tank of this car is full.")
    

# Using Instance as Attributes 

class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
       
        print(f"This car has a {self.battery_size}-kWh battery.")


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """"
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car. 
        """
        super().__init__(make, model, year) # super() function allows you to call a method from the parent class 
        self.battery = Battery() 

    def fill_gas_tank(self):  #overriding methods from the parent class
        """Electric cars don't have gas tank."""
        print("This car doesn't need a gas tank") 

my_tesla = ElectricCar('tesla', 'model S', 2022)
print(my_tesla.get_descriptive_name())

my_tesla.fill_gas_tank()
my_tesla.battery.describe_battery()

