# Simple function named greet_user() that displays a message.

def greet_user():
    """Display a simple message"""
    print("Hello Friend!")

greet_user()


#Passing Information to a Function

def greet_user(username):
    """Display a simple greeting"""
    print(f"Hi {username.title()}, Welcome!")

greet_user("dave")