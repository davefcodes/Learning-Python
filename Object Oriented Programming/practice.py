# 9-1. Restaurant

class Restaurant:
    """A class representing a restaurant."""
    
    def __init__(self, name, cuisine_type):
        """Initialize restaurant name and cuisine_type"""
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.numbers_served = 0

    def describe_restaurant(self):
        """Description about the Restaurant"""
        description = f"{self.name} serves wonderful {self.cuisine_type} food."
        print(f"\n{description}")

    def open_restaurant(self):
        """Displaying the Restaurant is open"""
        msg = f"{self.name} is open. Come enjoy a great meal!"
        print(f"\n{msg}")

    def set_number_served(self, customer_count):
        self.numbers_served = customer_count
        print(f"The number of customers served are today are: {self.numbers_served}")
        
    def increment_number_served(self, daily_count):
        self.numbers_served += daily_count
        print(f"The amount of customers served in a day are {self.numbers_served}")



# american_food.describe_restaurant()
# american_food.open_restaurant()

mickey = Restaurant('Mickey Burger', 'Burger')
mickey.set_number_served(40)

mickey.increment_number_served(10)







# # 9-2 Creating three different instances from the class and call describe_restaurant for each instance


# murray_bagels = Restaurant('murray', "bagel's")
# murray_bagels.describe_restaurant()