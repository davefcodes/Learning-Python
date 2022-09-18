# 8-9. Messages: Make a list containing a series of short text messages. 
# Pass the list to a function called show_messages(), which prints each text message.

# def show_message(messages):
#     for message in messages:
#         print(message)

# msg = ['Hello, Welcome', 'Have Fun Coding' ':)']

# show_message(msg)


# 8-10. Sending Messages: Start with a copy of your program from Exercise 8-9. Write a function called send_messages() that prints each text message and moves each message to a new list called sent_messages as it’s printed. 
# After calling the function, print both of your lists to make sure the messages were moved correctly.

def show_messages(unsent_messages):
    """Print all messages in the list"""
    print("Showing all messages:")
    for message in unsent_messages:
        print(message)
        
        
def send_messages(unsent_messages, sent_messages):
    """Print each message, and then move it to sent_meesages."""
    print("\nSending all messages:")

    while unsent_messages:
        current_message = unsent_messages.pop()
        print(current_message)
        sent_messages.append(current_message)
    

unsent_messages = ['how are you?', ':)', 'thnx talk later', "working on a project"]
sent_messages = []

show_messages(unsent_messages)
send_messages(unsent_messages, sent_messages)

print("\nThe final list:")

print(unsent_messages)
print(sent_messages)





#8-11. Archived Messages: Start with your work from Exercise 8-10. Call the function send_messages() with a copy of the list of messages. 
# After calling the function, print both of your lists to show that the original list has retained its messages.
def show_messages(unsent_messages):
    """Print all messages in the list"""
    print("\nShowing all messages:")
    for message in unsent_messages:
        print(message)
        
        
def send_messages(unsent_messages, sent_messages):
    """Print each message, and then move it to sent_meesages."""
    print("\nSending all messages:")

    while unsent_messages:
        current_message = unsent_messages.pop()
        print(current_message)
        sent_messages.append(current_message)
    

unsent_messages = ['how are you?', ':)', 'thnx talk later', "working on a project"]
show_messages(unsent_messages)

sent_messages = []
send_messages(unsent_messages[:], sent_messages) # function_name(list_name[:]) slice notation makes a copy of the list to send to the function.

print("\nThe final list:")
print(unsent_messages)
print(sent_messages)