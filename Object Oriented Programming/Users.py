#9-3 Users 

class Users:
    """A class representing users"""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()

    def describe_user(self):
        """Summary of User information"""
        print('First Name:',self.first_name)
        print('Last Name:',self.last_name)
        print('Username:',self.username)
        print('Email:',self.email)
        print('Location:',self.location)

    def greet_user(self):
        """Personalized greeting to user"""
        msg = f"Hello {self.first_name} {self.last_name}, Welcome!\n"
        print(f"\n{msg}")

user_1 = Users('david', 'faibil', 'davefcodes', 'dave@example.com', 'new york')
user_1.describe_user()
user_1.greet_user()
 
user_2 = Users('kasey','green','kgreen23', 'kg@example.com', 'california')
user_2.describe_user()
user_2.greet_user()