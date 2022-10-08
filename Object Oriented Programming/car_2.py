# Modifying an Attribute's Value Through a Method
class Car:
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 20

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def update_odometer(self,mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back. 
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it.")

# my_new_car = Car('audi', 's8', '2022')
# print(my_new_car.get_descriptive_name())

# my_new_car.update_odometer(25) # modified an attribute value through a method
# my_new_car.read_odometer()

# Incrementing an Attribute's Value Through a Method
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
        

    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it.")

# my_used_car = Car('subaru', 'outback', 2015)
# print(my_used_car.get_descriptive_name())

# my_used_car.update_odometer(23_500)
# my_used_car.read_odometer()

# my_used_car.increment_odometer(100)
# my_used_car.read_odometer()

# Incrementing an Attribute's Value Through a Method and Reject negative increments on an odometer
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
        if miles < 0:    # rejects negative increments 
            print("Odometer can't be rolled back")
        else:
            self.odometer_reading += miles
        

    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it.")

my_used_car = Car('subaru', 'outback', 2015)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(200)
my_used_car.read_odometer()


