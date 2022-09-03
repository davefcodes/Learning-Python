# 8-9. Messages: Make a list containing a series of short text messages. 
# Pass the list to a function called show_messages(), which prints each text message.

# def show_message(messages):
#     for message in messages:
#         print(message)

# msg = ['Hello, Welcome', 'Have Fun Coding' ':)']

# show_message(msg)


# 8-10. Sending Messages: Start with a copy of your program from Exercise 8-9. Write a function called send_messages() that prints each text message and moves each message to a new list called sent_messages as it’s printed. 
# After calling the function, print both of your lists to make sure the messages were moved correctly.
unsent_messages = ['Hi, how are you doing?', 'Hope all is good', 'Please give me a call back', "Let's work on a project :)"]
sent_messages = []

def send_messages(unsent_messages, sent_messages=''):
    for message in unsent_messages:
        print(message)
        sent_messages.append(message)
        
    
send_messages(unsent_messages, sent_messages)
print(sent_messages)



#8-11. Archived Messages: Start with your work from Exercise 8-10. Call the function send_messages() with a copy of the list of messages. 
# After calling the function, print both of your lists to show that the original list has retained its messages.

send_messages(unsent_messages[:], sent_messages) # function_name(list_name[:]) slice notation makes a copy of the list to send to the function.
print(unsent_messages)