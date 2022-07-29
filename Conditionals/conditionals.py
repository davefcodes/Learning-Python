# 5-1. Conditional Tests: Write a series of conditional tests. Print a statement describing each test and your prediction for the results of each test. Your code should look something like this:
#             car = 'subaru'
#             print("Is car == 'subaru'? I predict True.")
#             print(car == 'subaru')
#             print("\nIs car == 'audi'? I predict False.")
#             print(car == 'audi')

# • Look closely at your results, and make sure you understand why each line evaluates to True or False.

# • Create at least ten tests. Have at least five tests evaluate to True and another five tests evaluate to False.


age = 19

print("Is age == 19? I predict True")
print(age == 19)

print("Is age == 20? I predict False ")
print(age == 20)

userName = "Dave"
print("\nIs the userName == Dave? I predict True")
print("Dave" in userName) 

print("Is userName == 'Ema'? I predict False")
print(userName == 'Ema')


car = 'audi'
print("\nIs car == 'audi'? I predit True")
print(car == 'audi')

print("Is car == 'bmw'? I predict False")
print(car == 'bmw')


birthday_month = 'February'

print("\nIs birthday_month == 'February'? I predict True")
print(birthday_month == 'february'.title()) #string will evaluate to false without the title() function 

print("Is birthday_month == 'March'? I predict False")
print(birthday_month == 'March')


breakfast = ['milk', 'bread', 'eggs', 'bacon']
print("\nIs steak in breakfast? I predict False ")
print("steak" in breakfast)
print("Is eggs in breakfast? I predict True")
print("eggs" in breakfast)


# 5-2. More Conditional Tests: You don’t have to limit the number of tests you create to ten. If you want to try more comparisons, write more tests and add them to conditional_tests.py. Have at least one True and one False result for each of the following:
# • Tests for equality and inequality with strings
# • Tests using the lower() method
# • Numerical tests involving equality and inequality, greater than and less than, greater than or equal to, and less than or equal to
# • Tests using the and keyword and the or keyword
# • Test whether an item is in a list
# • Test whether an item is not in a list

user_name = "marie"

print("\nIs user_name == marie? I predict True")
print(user_name == "marie")

if user_name != "david":
  print("Add david to the usernames")

pizza_topping = 'chicken'
print("\nIs pizza_topping == Chicken? I predict Fasle " )
print(pizza_topping == "Chicken")

friends = "Brenda"
print(friends.lower() == "brenda")

age_0 = 22 
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)
print (age_0 >= 22) and (age_1 >= 18)





names = ["samuel","james", "david"]
print("wonder" in names)
print("james" in names)


age = int(input("Type your age: "))



if age < 4:
  price = 0
elif age < 18:
  price = 25
elif age < 65:
  price = 40
elif age >= 65:
  price = 20

print(f"Your ticket cost is ${price}")


  

