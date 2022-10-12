# Die if Abfrage

Um die Resultate der boolschen Operationen in Kontext mit einem Programmablauf setzen zu können, bietet Python
die Möglichkeit das boolsche Resultat mit einer if (wenn) Abfrage zu integrieren.

Das folgende Beispiel demonstriert den Strukturaufbau:
```python
if 3 + 2 > 4:
    print('3 + 2 ist grösser 4')
```
Die Syntax der einfachen if Abfrage besteht aus drei Elementen:
1. Das if Schlüsselwort (Abschluss mit einem Doppelpunkt `:`).
2. Ein booscher Test (3 + 2 > 4) welcher mit `True` oder `False` beantwortet werden kann.
3. Ein eingerückter Block mit Anweisungen falls die Bedingung `True` ist.

## Das else Schlüsselwort
Das `else` Schlüsselwort markiert den Block welcher ausgeführt wird, falls die boolsche Bedingung
'False' ist.

```python
if 5 < 2:
    print('5 < 2 => True')
else:
    print('5 < 2 => False')
```

## Das elif Schlüsselwort
Das `elif` Schlüsselwort ist die Kombination aus `if` und `else` und wird benutzt um die 
'if' Abfrage zu erweitern. Sind sämtliche `if elif` Abfragen `False`. wird der Code im `else` Block ausgeführt.

```python
grade = 5.0
if grade < 4.0:
    print('ungenügend')
elif (grade >= 4.0) and (grade < 5.0):
    print('genügend')
elif (grade >= 5.0) and (grade < 5.5):
    print('gut')
else:
    # wird aufgerufen falls keine der obigen 
    # Testblöcke True sind
    print('sehr gut')
```

---
**Hinweis 1**: Mit der Einrückung in Python werden untergeordnete Textblöcke markiert. Die Einrückungen sollten
entweder aus 4 Leerzeichen oder 1 Tabulator bestehen. Erfolgt die Einrückung in einer nicht homogenen 
Art und Weise, wird ein IndentationError von Python erzeugte
```python
# Beispiel 1: Einrückungen mit unterschiedlicher Anzahl Leerzeichen bei der Einrückung
if a == True:
    print('Einrückung')
   print('Einrückung')
....
IndentationError: unindent does not match any outer indentation level

# Beispiel 2: Keine Einrückung
if a == True:
print('Einrückung')
print('Einrückung')
....
IndentationError: expected an indented block
```
---
**Hinweis 2**: Die Teilbedingungen sind zwingend mit einem Doppelpunkt abzuschliessen. Wird dies nicht gemacht,
wird ein Syntax Error von Python erzeugt.
```python
if 2 + 4 == 9:
    print('interessant!')
elif 2 + 6 == 12
    print('noch interessanter!')

....
SyntaxError: invalid syntax
```
---