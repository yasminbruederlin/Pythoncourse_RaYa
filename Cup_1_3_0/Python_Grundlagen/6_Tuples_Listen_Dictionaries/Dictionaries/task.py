# einfaches Dictonary
names_dict = {'name': 'Peter', 'nickname': 'Pesche', 'age': 29}
print(names_dict)

print(names_dict['name'])

print(names_dict.keys())
print(names_dict.values())
print(list(names_dict.keys()))
print(list(names_dict.values()))

print('-----')

# hinzufügen und entfernen von Einträgen
names_dict['best_friend'] = 'Frank'
names_dict.pop('nickname')
print(names_dict)

print('-----')

# Listen mit Dictionaries
phone_numbers = []  # leere Liste
phone_numbers.append({'name': 'Heidi', 'nr': '079 548 23 78'})
phone_numbers.append({'name': 'Peter', 'nr': '076 897 14 21'})
phone_numbers.append({'name': 'Frand', 'nr': '078 365 17 28'})
phone_numbers.append({'name': 'Andrea', 'nr': '079 405 98 41'})
print(phone_numbers)

# Iteration über eine Liste mit Dictionaryeinträgen
for item in phone_numbers:
    # Iteration über sämtliche key value Einträge
    for key, value in item.items():
        print(key, value)