favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

# language = favorite_languages['sarah'].title()
# language_2 = favorite_languages['jen'].title()
# print(f"Sarah's favorite language is {language}")

# print(f"Jen's favorite language is {language_2}")

for name, language in favorite_languages.items():
    print(f"\n{name.title()}'s, favorite language is {language}\n")

# for name in favorite_languages.keys():
#     print(name.title())


