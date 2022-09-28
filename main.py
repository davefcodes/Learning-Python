#Excerise Pg20 (name.py)  
# A method is an action Python can perform on  a piece of data 

# .title() method makes the first letter in each word upper case
name = "ada lovelace"
print(name.title())

# .upper() method changes the string to all upper case
name = "ada lovelace"
print(name.upper())

# .lower() method changes the string to all lower case
print(name.lower())


#Excerise Pg21 (full_name.py)  
# using f string to format our strings
first_name = "ada"
last_name = "lovelace"

full_name = f"{first_name} {last_name}"
print(full_name)

#Used f-string to compose a messages using the information a variable
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"

print(f"Hello, {full_name.title()}!")

#Used f-string to compose a message and assigned the entire message to a variable 
first_name ="ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}" 

message = f"Hello, {full_name.title()}!" 
print(message)

# using .format method instead f-string
first_name ="ada"
last_name = "lovelace"
full_name = "{}{}".format(first_name, last_name)


#Avoiding syntax erros with strings
#(apostrophe.py) Page24 
message = "One of Python's strengths is its diverse coummunity"
print(message)
