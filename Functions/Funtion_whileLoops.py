# Using a function in a while Loop

def get_formatted_name(first_name, last_name):
    """Return a fullname, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# infinte Loop 
while True: 
    print("\nPlease tell me your name:")
    print("(enter 'q' at anytime to quit)") # added a message that informs users how to quit 

    f_name = input("first_name:")
    if f_name == 'q':
       break # break out of the loop if the user enters the quit value at either prompt

    l_name = input("last_name:")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\n Hello, {formatted_name}!") 

