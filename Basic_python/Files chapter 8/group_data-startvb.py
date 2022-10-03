# Voorbeeld 1: de invoerfile bevat geen titel en we drukken alleen de state af met de bijhorende cities
print('1: Top 50 cities in USA')
with open('US cities.csv') as file:
    line = file.readline().rstrip()
    record = line.split(';')
    while line:
        stateind = record[1]
        print(stateind)
        while line and record[1] == stateind:
            print("\t", record[0])
            line = file.readline().rstrip()
            record = line.split(';')


# Voorbeeld 2: de invoerfile bevat WEL titel en we drukken alleen de state af met de bijhorende cities
# Voeg dus deze lijn toe aan de invoerfile: City;State;Population
# Wat moet je veranderen: een twee readline in het begin. De rest blijft identiek.
# print('Top 50 cities in USA')
# with open('US cities.csv') as file:
#     line = file.readline().rstrip()
#     line = file.readline().rstrip()   # die dus toevoegen
#     record = line.split(';')


# vanaf hier verder werken zonder die titel
# Voorbeeld 3: we drukken de state af en nummeren de bijhorende cities
print('3: Top 50 cities in USA')
with open('US cities.csv') as file:
    line = file.readline().rstrip()
    record = line.split(';')
    while line:
        stateind = record[1]
        city_counter = 0
        print(stateind)
        while line and record[1] == stateind:
            city_counter += 1
            print('  ' + str(city_counter) + ') ' + record[0])
            line = file.readline().rstrip()
            record = line.split(';')


# Voorbeeld 4: we drukken de state af en voor elke stad het aantal inwoners.
# Op het einde van elke state vermelden we het grootst aantal inwoners in die state.
print('4: Top 50 cities in USA')
with open('US cities.csv') as file:
    line = file.readline().rstrip()
    record = line.split(';')
    while line:
        stateind = record[1]
        population_max = int(record[2])
        print(stateind)
        while line and record[1] == stateind:
            print('\t',record[0].ljust(20),record[2])  # ljust is een tip bij oefening 3 van Text files
            if int(record[2]) > population_max:   # opgelet: int niet vergeten want hij vergelijkt ze anders als strings!
                population_max = int(record[2])
            line = file.readline().rstrip()
            record = line.split(';')
        print('\t','Largest population in', stateind, '=', population_max)

# Voorbeeld 5: we drukken de state af en voor elke stad het aantal inwoners.
# Op het einde van elke state vermelden we ook de naam van de stad met het meest aantal inwoners.
print('5: Top 50 cities in USA')
with open('US cities.csv') as file:
    line = file.readline().rstrip()
    record = line.split(';')
    while line:
        stateind = record[1]
        print(stateind)
        population_max = int(record[2])
        cityname_max = record[0]
        while line and record[1] == stateind:
            print('\t',record[0].ljust(20),record[2])
            if int(record[2]) > population_max:
                population_max = int(record[2])
                cityname_max = record[0]
            line = file.readline().rstrip()
            record = line.split(';')
        print('\t','Largest population in', cityname_max, '=', population_max)

# Voorbeeld 6: laat zien dat je soms best alle info per record mee afdrukt om te weten of je groepsonderbreking juist is
# Want als je alleen dit afdrukt en het loopt fout, dan is het moeilijk zoeken
print('6: Largest population:')
with open('US cities.csv') as file:
    line = file.readline().rstrip()
    record = line.split(';')
    while line:
        stateind = record[1]
        population_max = int(record[2])
        while line and record[1] == stateind:
            if int(record[2]) > population_max:
                population_max = int(record[2])
            line = file.readline().rstrip()
            record = line.split(';')
        print('\t' + stateind + ':', population_max)

# Voorbeeld 7: als je het overzicht dat voorbeeld 6 maakte gesorteerd wil.
# let op: het blijft beter van de file lijn per lijn te lezen en dus niet met readlines alles in te lezen
print('7: Largest population (order by state name)')
states = []
with open('US cities.csv') as file:
    line = file.readline().rstrip()
    record = line.split(';')
    while line:
        stateind = record[1]
        population_max = int(record[2])
        while line and record[1] == stateind:
            if int(record[2]) > population_max:
                population_max = int(record[2])
            line = file.readline().rstrip()
            record = line.split(';')
        states.append(stateind + ': '+ str(population_max))

states.sort()
for state in states:
    print('\t'+state)