# Dictionaries
In einem Dictionary ist für jedes Element nebst dem Wert noch ein Schlüssel hinterlegt. 
Die Kombination von Schlüssel bietet die Möglichkeit auch komplexe Datenstrukturen 
verhältnismässig einfach zu strukturieren.
Hinsichtlich der Syntax werden die Einträge zwischen geschweiften Klammern `{}`
beschrieben.

```python
names_dict = {'name': 'Peter', 'nickname': 'Pesche', 'age': 29}
```
Die Abfrage einzelner Attribute erfolgt mittels Klartextindexierung.
```python
names_dict['name']
```
Besteht das Interesse nur an den Schlüsseln bzw. den Werten können diese mittels `keys()` bzw. `values()` 
abgefragt werden. In Abhängigkeit der Fragestellung ist die Konvertierung in eine Liste sinnvoll.
```python
names_dict.keys()
names_dict.values()
list(names_dict.keys())
list(names_dict.values())
```
Zur Laufzeit kann das Dictionary einfach erweitert oder verkleinert werden mittels.
```python
names_dict['best_friend'] = 'Frank'
names_dict.pop('nickname')
```

# Speicherung von Listen mit Dictioanries
Oft werden Dictionaries in Kombination mit Listen eingesetzt. 
Die dabei entstehenden Kombination von äusserer Liste, welche es erlaubt viele unterschiedliche Datensätze zu
verwalten, mit den effektiven Nutzdaten in der Form eines Dictionaries.

Schritt 1: Erstellung einer Liste mit Dictionaryelementen
```python
phone_numbers = []  # leere Liste
phone_numbers.append({'name': 'Heidi', 'nr': '079 548 23 78'})
phone_numbers.append({'name': 'Peter', 'nr': '076 897 14 21'})
phone_numbers.append({'name': 'Frand', 'nr': '078 365 17 28'})
phone_numbers.append({'name': 'Andrea', 'nr': '079 405 98 41'})
```

Schritt 2: Iteration über die Listenelemente sowie die einzelen Schlüssel Wertekombinationen
```python
# Iteration über eine Liste mit Dictionaryeinträgen
for item in phone_numbers:
    # Iteration über sämtliche key value Einträge
    for key, value in item.items():
        print(key, value)
```