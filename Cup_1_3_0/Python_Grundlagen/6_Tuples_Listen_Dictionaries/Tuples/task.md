# Tuples

Die vermutlich einfachste Datenstruktur ist das Tuple. Ein Tuple ist eine Sequenz von Elementen
welche zur Laufzeit des Programmes nicht verändert werden kann. Somit ist der Dateninhalt
**vor** dem Programmstart vollständig zu definieren.

Die Erstellung erfolgt denkbar einfach. Die Elemente werden zwischen runden Klammern `()` durch 
Kommas `,` getrennt aufgelistet.

```python
tuple_sequence = (1, 2, 3)
```

Zulässig ist die Mischung unterschiedlicher Datentypen inherhalb der Auflistung.
```python
tuple_sequence = (1, 3.141, 'abc')
```

## Anzahl Einträge im Tupel
Über die Funktion `len()` kann die Länge bzw. die Anzahl Einträge abgefragt werden.
```python
tuple_sequence_len = len(tuple_sequence)
```

## Abfrage der einzelnen Einträge
Die einzelnen Elemente werden über einen Index abgefragt, beginnend mit 0. In Python ist das erste Element
einer Auflistung stehts mit dem Index 0 behaftet. Das heisst, dass eine Auflistung der Länge 3, die Indexwerte
0, 1 und 2 aufweist.
```python
tuple_sequence = ('eins', 'zwei', 'drei')
print(tuple_sequence[0])
print(tuple_sequence[1])
print(tuple_sequence[2])
```
Bei der Abfrage eines Elementes welches nicht verfügbar ist, generiert Python einen Indexerror
```python
print(tuple_sequence[3])
IndexError: tuple index out of range
```

## Auswertung eines Tuples mit Hilfe einer for - Schleife
Die einzelenne Elemente eines Tuples sind in einer `for` Schleife abrufbar.
```python
for item in tuple_sequence:
    print(item)
```
