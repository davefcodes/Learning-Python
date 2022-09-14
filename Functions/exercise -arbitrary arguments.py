#8-12. Sandwiches: Write a function that accepts a list of items a person wants on a sandwich. 
# The function should have one parameter that collects as many items as the function call provides, and it should print a summary of the sand- wich that’s being ordered. 
# Call the function three times, using a different num- ber of arguments each time.

def make_sandwich(*toppings):
    """Summary of sandwich that is being ordered"""

    print("\nThese are the toppings you want on your sandwich:")
    
    for topping in toppings:
        print(f"- {topping}")

make_sandwich('chicken')
make_sandwich('tomatoes', 'onions', 'ranch')
make_sandwich('mayo', 'olives', 'green peppers', 'onions')

#8-13. User Profile: Build a profile of yourself by calling build_profile(), using your first and last names and three other key-value pairs that describe you.

def build_profile(first, last, **user_info):
    """Building a profile about myself"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

my_profile = build_profile('david', 'faibil', 
                            location = 'new york', 
                            career = 'software engineer')

print(my_profile) 