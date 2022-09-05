# In case you don't know ahead of time how many arguments a function accepts
# Python allows a function to collect an arbi- trary number of arguments from the calling statement.

def make_pizza(*toppings):
    """Print the list of topppings that have been requested"""
    print(toppings)

make_pizza('peproni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
