
#Program that checks if user can VOTE or NOT

def checkID():
  name = (input("What is your name? "))
  user_age = int(input("What is your age? "))
  
  
  
  if user_age >= 18:
    print(f"You can vote {name} ")
  elif user_age < 21:
    print(f"You can't vote {name} ")
  else:
    print("Sorry ")

checkID()




