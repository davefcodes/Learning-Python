# Passing a List 

def greet_users(names):
    """Print a simple message to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}"
        print(msg)

user_names = ['Kim', 'Dave', 'Sam', 'Chantel']
greet_users(user_names)


