# Chapter 3 Introduction to List 

# What is a List? 
# A list is a collection of items in a particular order. You can make a list that includes the letters of the alphabet, the digits from 0–9, or the names of all the people in your family. It’s a good idea to make the name of your list plural, such as letters, digits, or names.

# 3-1. Names: Store the names of a few of your friends in a list called names. Print each person’s name by accessing each element in the list, one at a time.

friend_names = ["Brenda", "Sammy", "Fabio"]
print(friend_names[0])
print(friend_names[1])
print(friend_names[2])

# 3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just printing each person’s name, print a message to them. The text of each mes- sage should be the same, but each message should be personalized with the person’s name.

message_1 = f"\nI love {friend_names[0].title()}"
print(message_1)

message_2 = f"\n{friend_names[1].title()} Loves Baseball"
print(message_2)

message_3 = f"\n{friend_names[2].title()} loves to code in Java"
print(message_3)

# 3-3. Your Own List: Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list that stores several examples. Use your list to print a series of statements about these items, such as “I would like to own a Honda motorcycle.”


my_cars = ["Audi Q8", "BMW", "Mercedes Benz"]
affrim_1 = "\nI will own an {} when I get my software engineer job".format(my_cars[0])
print(affrim_1)

affrim_2 = "\nI will own a {} when I get my software engineer job".format(my_cars[1])
print(affrim_2)

affrim_3 = "\nI will buy Mum a {} in the future".format(my_cars[2])
print(affrim_3)

# 3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that includes at least three people you’d like to invite to dinner. Then use your list to print a message to each person, inviting them to dinner.

guest_list = ["Mum", "Brothers", "Girlfriend"]
invite_msg1 = "\n\tDear, {} you're invited to David's Dinner".format(guest_list[0])
print(invite_msg1)

invite_msg2 = "\n\tDear, {} you're invited to David's Dinner".format(guest_list[1])
print(invite_msg2)
invite_msg3 = f"\n\tDear, {guest_list[2]} you're invited to David's Dinner"
print(invite_msg3)


# 3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.
# Start with your program from Exercise 3-4. Add a print() call at the end of your program stating the name of the guest who can’t make it.
print(f"\n{guest_list[2]}, won't make it the Dinner")

# Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
guest_list[2] = "Friends"
print(guest_list)

# Print a second set of invitation messages, one for each person who is still in your list.
new_invite = "\n{}, you're invited to the Dinner".format(guest_list[0])
print(new_invite)
new_invite_2 = "\n{} you're invited to the Dinner".format(guest_list[1])
print(new_invite_2)
new_invite_3 = "\n{} you're invited to the Dinner".format(guest_list[2])
print(new_invite_3)

# 3-6. More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.

#Start with your program from Exercise 3-4 or Exercise 3-5. Add a print() call to the end of your program informing people that you found a bigger dinner table.
print("We found a Bigger Guest")

#•Use insert() to add one new guest to the beginning of your list.
guest_list.insert(0,"Sammy")
print(guest_list)
#• Use insert() to add one new guest to the middle of your list.
guest_list.insert(2, "Murphy")
print(guest_list)
#• Use append() to add one new guest to the end of your list.
guest_list.append("Brenda")
print(guest_list)
#• Print a new set of invitation messages, one for each person in your list.
final_invite = "\n{} this is a final invite to the Dinner".format(guest_list[0])
print(final_invite)
final_invite_1 = "\n{} this is a final invite to the Dinner".format(guest_list[1])
print(final_invite_1)
final_invite_2 = "\n{} this is a final invite to the Dinner".format(guest_list[2])
print(final_invite_2)
final_invite_3 = "\n{} this is a final invite to the Dinner".format(guest_list[3])
print(final_invite_3)
final_invite_4 = "\n{} this is a final invite to the Dinner".format(guest_list[4])
print(final_invite_4)
final_invite_5 = "\n{} this is a final invite to the Dinner".format(guest_list[5])
print(final_invite_5)



 # 3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.


#• Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
print("\nI'm sorry can only invite two people")


#• Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
removed_guest = guest_list.pop(0)
removed_message = "Sorry {} I can't invite you to dinner".format(removed_guest)
print(removed_message)

#• Print a message to each of the two people still on your list, letting them know they’re still invited.
removed_guest1 = guest_list.pop(1)
removed_guest2 = guest_list.pop(2)

print(f"Sorry {removed_guest1} can't invite you for Dinner")
print(f"Sorry {removed_guest2} can't invite you for Dinner")
#• Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.

del guest_list[0]
del guest_list[1]
del guest_list[-1]
print(guest_list)


