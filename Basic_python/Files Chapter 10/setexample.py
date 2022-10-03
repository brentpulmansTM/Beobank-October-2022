# Example 1: use a list and check whether the city is already in the list
list_cities = []
with open('popular_cities.csv', encoding = 'UTF-8') as file:
    city = file.readline().rstrip()
    while city:
        if city not in list_cities:
            list_cities.append(city)
        city = file.readline().rstrip()

list_cities.sort()
print(len(list_cities), 'popular cities in the world')
for city in list_cities:
    print(city)


# Example 2: use a set -> you don't have to check yourself
set_cities = set()
with open('popular_cities.csv', encoding = 'UTF-8') as file:
    city = file.readline().rstrip()
    while city:
        set_cities.add(city)
        city = file.readline().rstrip()

print(len(set_cities), 'popular cities in the world')
for city in set_cities:
    print(city)

# list_cities = list(set_cities)
# list_cities.sort()
# print(len(list_cities), 'popular cities in the world')
# for city in list_cities:
#     print(city)

