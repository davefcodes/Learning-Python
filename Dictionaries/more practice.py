# 6-1. Person: Use a dictionary to store information about a person you know. Store their first name, last name, age, and the city in which they live. You should have keys such as first_name, last_name, age, and city. Print each piece of information stored in your dictionary.


person = {
  'first_name': 'brenda', 
  'last_name': 'matias',
  'age': '21',
  'city': 'new york'
}

print(person['first_name'].title())
print(person['last_name'].title())
print(person['age'])
print(person['city'].title())


# 6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers. Think of five names, and use them as keys in your dictionary. Think of a favorite number for each person, and store each as a value in your dictionary. Print each person’s name and their favorite number. For even more fun, poll a few friends and get some actual data for your program.


fav_numbers = {
  'jimmy': 68,
  'david': 22, 
  'samuel': 19,
  'ali': 10,
  'sarah': 27
}

print(f"Jimmy's favorite number is {fav_numbers['jimmy']}")
print(f"David's favorite number is {fav_numbers['david']}")
print(f"Samuel's favorite number is {fav_numbers['samuel']}")
print(f"Ali's favorite number is {fav_numbers['ali']}")
print(f"Sarah's favorite number is {fav_numbers['sarah']}")

# 6-3. Glossary: A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.
# • Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store their meanings as values.
# • Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.


glossary = {
  'string': 'A series of characters ',
  'dictionary': 'A collection of key-value pairs',
  'len': 'Returns the number of items in an object',
  'list': 'a collection of items in a particular order',
  'variable': 'used to store information'
}


word = 'string'

print(f"\n{word.title()}: {glossary['string']}")

word = 'dictionary'
print(f"\n{word.title()}: {glossary['dictionary']}")

word = 'len'
print(f"\n{word.title()}: {glossary['len']}")

word = 'list'
print(f"\n{word.title()}: {glossary['list'].capitalize()}")

word = 'variable'
print(f"\n{word.title()}: {glossary['variable'].capitalize()}")

