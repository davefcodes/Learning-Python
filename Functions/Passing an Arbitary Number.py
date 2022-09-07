# In case you don't know ahead of time how many arguments a function accepts
# Python allows a function to collect an arbi- trary number of arguments from the calling statement.

def make_pizza(*toppings):   # the asterisk tells python to make an empty tuple called toppping
    """Print the list of topppings that have been requested"""
    print(toppings)

make_pizza('peproni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')



def make_pizza(*toppings):
    """Summarize the pizza we are about to make"""
    print("\nMaking a pizza with the follwoing toppings:")

    for topping in toppings:
        print(f"- {topping}")

make_pizza('peproni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')