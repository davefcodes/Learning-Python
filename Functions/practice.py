# 8-6. City Names: Write a function called city_country() that takes in the name of a city and its country.
# The function should return a string formatted like this:   "Santiago, Chile"

# def city_country(city, country):
#     formated = print(f"{city.title()} {country.title()}")
#     return formated


# city_country("santiago,", "chile")
# city_country("rio,", "brazil")
# city_country("accra,", "ghana")



#8-7. Album: Write a function called make_album() that builds a dictionary describing a music album. 
# The function should take in an artist name and an album title, and it should return a dictionary containing these two pieces of information. 
# Use the function to make three dictionaries representing different albums. 
# Print each return value to show that the dictionaries are storing the album information correctly.

# def make_album(name, title, tracks= None):
#     """Building a dictionary containing information about an album."""
#     album_info = {
#         'Artist name':name.title(), 
#         'Album title':title.title()
#         }
#     if tracks:
#         album_info['Tracks'] = tracks
#     return album_info 

# music = make_album('drake', 'take care')
# print(music)

# music = make_album('wizkid', 'more love, less ego')
# print(music)

# music = make_album('yaw tog', 'time', 7)
# print(music)

# 8-8. User Albums: Start with your program from Exercise 8-7. Write a while loop that allows users to enter an album’s artist and title. 
# Once you have that information, call make_album() with the user’s input and print the dictionary that’s created. 
# Be sure to include a quit value in the while loop.

def make_album(name, title):
    album_dict = {
        'Artist Name': name.title(),
        'Album Title': title.title()
    }
    return album_dict

while True:
    print("\nPlease enter album artist and title: ")

    artist_name = input("\nEnter artist name: ")
    if artist_name == 'q':
        print('GoodBye')
        break

    album_title = input("\nEnter album title: ")
    if album_title == 'q':
        print('GoodBye')
        break

    print("-----------------------------------------")

    album_info = make_album(artist_name, album_title)
    print(album_info )
