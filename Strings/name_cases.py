# Try It Yourself Page25
#2-3. Personal Message: Use a variable to represent a person’s name, and print a message to that person. Your message should be simple, such as, “Hello Eric, would you like to learn some Python today?”

name = "Eric"
message = f"Hello {name}, would you like to learn some Python Today"

print(message)

# 2-4. Name Cases: Use a variable to represent a person’s name, and then print that person’s name in lowercase, uppercase, and title case.

name = "David"

print(name.lower())
print(name.upper())
print(name.title())

#2-5. Famous Quote: Find a quote from a famous person you admire. Print the quote and the name of its author. Your output should look something like the following, including the quotation marks:

famous_quote = "“Tim Gover once said,there’s no off-season when you’re serious about being a winner.“"
print(famous_quote)

#2-6. Famous Quote 2: Repeat Exercise 2-5, but this time, represent the famous person’s name using a variable called famous_person. Then compose your message and represent it with a new variable called message. Print your message.
famous_person = "Joe Rogan -"
message = " “The universe rewards hustle.”"
print(famous_person + message)

#2-7. Stripping Names: Use a variable to represent a person’s name, and include some whitespace characters at the beginning and end of the name. Make sure you use each character combination, "\t" and "\n", at least once.Print the name once, so the whitespace around the name is displayed. Then print the name using each of the three stripping functions, lstrip(), rstrip(), and stri

person_name = " \n\tDavid "
print(person_name)

print(person_name.lstrip())
print(person_name.rstrip())
print(person_name.strip())