# .sort() method makes it relatively easy to sort a list.
# We can also sort this list in reverse alphabetical order by passing the argument reverse=True to the sort() method. 

# Printing a List in Reverse Order
# To reverse the original order of a list, you can use the reverse() method.


# Page 47 
#3-8. Seeing the World: Think of at least five places in the world you’d like to visit.Store the locations in a list. Make sure the list is not in alphabetical order.

placesToVisit = ["Singapore", "Monaco", "England", "America", "France"]

#Print your list in its original order. Don’t worry about printing the list neatly, just print it as a raw Python list.
print(placesToVisit)


# Use sorted() to print your list in alphabetical order without modifying the actual list.
print(sorted(placesToVisit))
# Show that your list is still in its original order by printing it.
print(placesToVisit)

# Use sorted() to print your list in reverse alphabetical order without chang- ing the order of the original list.

print(sorted(placesToVisit, reverse = True)) 
# Show that your list is still in its original order by printing it again.
print(placesToVisit)

# Use reverse() to change the order of your list. Print the list to show that its order has changed.
placesToVisit.reverse()
print(placesToVisit)

# Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
placesToVisit.reverse()
print(placesToVisit)
# Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
placesToVisit.sort()
print(placesToVisit)
# Use sort() to change your list so it’s stored in reverse alphabetical order. Print the list to show that its order has changed
placesToVisit.sort(reverse = True)
print(placesToVisit)