# 6-3. Glossary: A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.
# • Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store their meanings as values.
# • Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.

glossary = {
    'string': 'A series of characters ',
    'dictionary': 'A collection of key-value pairs',
    'len': 'Returns the number of items in an object',
    'list': 'a collection of items in a particular order',
    'variable': 'used to store information',
    'set': 'a collection in which each item must be unique'
}

# 6-4. Glossary 2: Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) by replacing your series of print() calls with a loop that runs through the dictionary’s keys and values. When you’re sure that your loop works, add five more Python terms to your glossary. When you run your program again, these new words and meanings should automatically be included in the output.

for word, meaning in glossary.items():
    print(f"\n{word.title()}: {meaning.title()}")

# 6-5. Rivers: Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.
# • Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
# • Use a loop to print the name of each river included in the dictionary.
# • Use a loop to print the name of each country included in the dictionary.

rivers = {'nile': 'egypt', 'amazon': 'peru', 'niger': 'guinea'}

for river, country in rivers.items():
    print(f"\nThe {river.title()} runs through {country.title()}")

for river in rivers.keys():
    print(river.title())

for country in rivers.values():
    print(country.title())

# 6-6. Polling: Use the code in favorite_languages.py (page 97).
# • Make a list of people who should take the favorite languages poll. Include
# some names that are already in the dictionary and some that are not.
# • Loop through the list of people who should take the poll. If they have already taken the poll, print a message thanking them for responding. If they have not yet taken the poll, print a message inviting them to take the poll.

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

poll_names = ['david', 'sarah', 'samuel', 'phil', 'jen']
for name in poll_names:
    if name in favorite_languages:
        print(f"\n{name.title()}, Thanks for taking the poll")
    else:
        print(f"\n{name.title()} Can you please take the poll")

# 6-6. Polling: Use the code in favorite_languages.py (page 97).
# • Make a list of people who should take the favorite languages poll. Include
# some names that are already in the dictionary and some that are not.
# • Loop through the list of people who should take the poll. If they have already taken the poll, print a message thanking them for responding. If they have not yet taken the poll, print a message inviting them to take the poll.
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}")
