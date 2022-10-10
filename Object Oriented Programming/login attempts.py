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
        self.login_attempts = 0

    def describe_user(self):
        """Summary of User information"""
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")
        print(f"Location: {self.location}")

    def greet_user(self):
        """Personalized greeting to user"""
        msg = f"Hello {self.first_name} {self.last_name}, Welcome!\n"
        print(f"\n{msg}")

    def increment_login_attempts(self):
        """Increment value of login_attempts."""
        self.login_attempts += 1
        

    def reset_login_attempts(self):
        """Reset login_attempts to 0"""
        self.login_attempts = 0
       


user_1 = Users('david', 'faibil', 'davefcodes', 'dave@example.com', 'new york')
user_1.describe_user()
user_1.greet_user()
 
print("\nMaking 3 login attempts...")
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
print(f"    Login Attempts: {user_1.login_attempts}")

print("Resetting login attempts...")
user_1.reset_login_attempts()
print(f"    Login attempts: {user_1.login_attempts}")

# user_2 = Users('kasey','green','kgreen23', 'kg@example.com', 'california')
# user_2.describe_user()
# user_2.greet_user()