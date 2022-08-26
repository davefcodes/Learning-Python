# Returning a Dictionary
def build_person(first_name,last_name):
    """Return a dictionary information of a person"""
    person = {'first':first_name, 'last':last_name}
    return person

ballPlayer = build_person('michael', 'jordan')
print(ballPlayer)

# Extended the function to accept optional values like a middle name, an age, an occupation, or any other information we want to store about a person.

def build_person(first_name, last_name, age = None, occupation =''):

    person = {'first':first_name, 'last':last_name}
    if age:
        person['age'] = age
    if occupation:
        person['occupation'] = occupation
    return person
    



actor = build_person('john', 'wick', age=40, occupation='actor') 
soccer_player = build_person('lionel', 'messi', age=35)
print(actor)
print(soccer_player)

