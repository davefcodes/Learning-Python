# Returning a Simple Value

def get_formatted_name(first_name,last_name):
    """Return a full name, neatly formated."""
    full_name = f"{first_name},{last_name}"
    return full_name.title()

my_name = get_formatted_name('david', 'faibil')
print(my_name)

# Making an Argument Optional

def get_formatted_names(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted """
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {middle_name} {last_name}"
    
    return full_name.title()

musicians = get_formatted_names('Jimi','Hendrix')
print(musicians)

musicians = get_formatted_names('john', 'hooker', 'lee')
print(musicians)

