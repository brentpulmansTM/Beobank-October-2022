# Example 3: group data

with open('popular_cities.csv', encoding = 'UTF-8') as file:
    list_cities = file.readlines()
list_cities.sort()

i = 0
while i < len(list_cities):
    city_counter = 0
    cityind = list_cities[i].rstrip()
    while i < len(list_cities) and cityind == list_cities[i].rstrip():
        i += 1
        city_counter += 1
    print(cityind, city_counter)


# Example 4: use a dictionary -> possibility to search afterwards
dict_cities = {}
with open('popular_cities.csv', encoding = 'UTF-8') as file:
    city = file.readline().rstrip()
    while city:
        if city in dict_cities:
            dict_cities[city] += 1            # increase value via key
        else:
            dict_cities[city] = 1             # create new key/value pair
        city = file.readline().rstrip()

for city in dict_cities:
   print(city.ljust(20), dict_cities[city])


# Example 5: function to create a dictionary -> to search afterwards
def create_dictionary():
    dict_cities = {}
    with open('popular_cities.csv', encoding = 'UTF-8') as file:
        city = file.readline().rstrip()
        while city:
            if city in dict_cities:
                dict_cities[city] += 1            # increase value via key
            else:
                dict_cities[city] = 1             # create new key/value pair
            city = file.readline().rstrip()
    return dict_cities

# main
topcities = create_dictionary()
name = input('Name of the city you want to check: ')
if name not in topcities:
    print('This city is not so popular')
else:
    print(topcities[name], 'people voted for this city')

# other method
# print('Number of votes: ', end='')
# result = topcities.get(name, 'none')
# print(result)