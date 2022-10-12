# Stringoperationen

Im Umgang mit Strings werden von Python diverse Funktionen zur Verfügung gestellt.  
https://docs.python.org/3/library/string.html  

Die am häufigsten verwendeteten Operationen werden nachfolgend aufgeführt.

## Länge eines Strings
Die Längenbestimmung einer Zeichenkette erfolgt mittels `len()`

## Frage nach einem String in einem String
Die Abfrage ob ein String in einem String enthalten ist erfolgt mittels dem `in` Schlüsselwort.
```python
print('au' in 'Haus')
```
Da es sich um eine boolsche Abfrage handelt, lautet die Antowrt `True` oder `False`.

# Stringaddition (conatenation)
Zwei oder mehrere Strings werden durch den `+` Operator verbunden.

## Indexierung
Jedes Zeichen in einem String wird über eine eindeutige Position nummeriert. Diese
Positionsangabe wird Index benannt. Der Zugriff auf ein einzelnes Zeichen erfolgt durch
die Angabe einer Postion i zwischen zwei eckigen Klammnern.
```python
'abcde'[0] => 'a'
'abcde'[2] => 'c'
'abcde'[3] => 'd'
```
In Python, und vielen anderen Programmiersprachen, beginnt der Zähler jeweils mit dem Wert 0.

Hinweis: Der Umgang mit der Nullindexierung ist für Programmierneulinge zu Beginn nicht ganz einfach.
Im Kapitel micro:bit Lauflichter erfolgt die Festigung anhand konkreter Beispiele.

## Stringteilung (slicing)
Der Zugang zu einer Untermenge von Zeichen (Substring) erfolgt über die Stringteilung. Dabei
wird ein Bereich definiert in welchem einzelne Zeichen extrahiert werden sollen.
Die Stringteilung ist wie die Indexierung nullbasierend. Die erste Zahl definiert das Startzeichen,
das zweite Element das Endzeichen - 1. In Python werden die Bereich so ausgelegt, dass das Zeichen
mit dem Endindex nicht in dem Substring enthalten ist.
```python
'abcde'[1:3] => 'bc'
```

Wird ein Substring mit Start vom ersten Zeichen (Index 0) oder mit Ende des letzten Zeichens (Index -1) 
angefordert, kann der entsprechende Index ausgelassen werden.

```python
'abcde'[2:] => 'cde' 
'abcde'[-1] => 'e'
'abcde'[:-1] => 'abcd'
'abcde'[:-2] => 'abc'
'abcde'[1:3] => 'bc'
```
Weitere Infos zur Indexierung sind in der Pythondokumentation verfügbar.    
https://docs.python.org/3/library/functions.html?highlight=slice#slice  