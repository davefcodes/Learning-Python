class Restaurant:
    """A class representing a restaurant."""
    
    def __init__(self, name, cuisine_type):
        """Initialize restaurant name and cuisine_type"""
        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Description about the Restaurant"""
        description = f"{self.name} serves wonderful {self.cuisine_type}"
        print(f"\n{description}")

    def open_restaurant(self):
        """Displaying the Restaurant is open"""
        msg = f"{self.name} is open. Come enjoy a great meal!"
        print(f"\n{msg}")


restaurant = Restaurant('The Grand', 'american')

print(restaurant.name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()

# 9-2 Creating three different instances from the class and call describe_restaurant for each instance


murray_bagels = Restaurant('murray', "bagel's")
murray_bagels.describe_restaurant()

pinch_chinese = Restaurant('pinch', 'chinese')
pinch_chinese.describe_restaurant()

oxomoco = Restaurant('oxomoco', 'mexican')
oxomoco.describe_restaurant()
