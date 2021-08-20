# Activity 1
# a list of 3 favorite websites
favorite_websites = [
    "Football365.com",
    "YouTube.com",
    "Netflix.com"
]
print (favorite_websites)
# add another 2
favorite_websites.append("Google.com")
favorite_websites.append("PirateBay.co.uk")
print (favorite_websites)
# remove the last one
favorite_websites.pop()
print (favorite_websites)

# Activity 2
# remove()
# remove the specified item
animal_list = ["dog", "cat", "bird"]
animal_list.remove("cat")
print(animal_list)
# remove by index
animal_list = ["dog", "cat", "bird"]
animal_list.pop(2)
print(animal_list)

# reverse() - reverse the order of list elements
animal_list = ["dog", "bird", "cat"]
animal_list.reverse()
print('Reversed animal list:', animal_list)

# sort()
animal_list = ["dog", "cat", "bird"]
animal_list.sort()
print('Sorted animal list:', animal_list)

# count()
# returns the number of times the specified element appears in the list
animal_list = ["dog", "cat", "bird", "dog"]
count = animal_list.count("dog")
print(f"The count of 'dog' is {count}")

# extend()
animal_list = ["dog", "cat", "bird"]
# create another list
exotic_animal_list = ["crocodile", "macaw"]
# add all elements of animal_list to exotic_animal_list
exotic_animal_list.extend(animal_list)
print('List after extend():', exotic_animal_list)

# Tuples are identical to lists in all respects, except for the following properties:

# Tuples are defined by enclosing the elements in parentheses (()) instead of square brackets ([]).
# Tuples are immutable.

