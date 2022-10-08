Vergleichsoperatoren
========

Wir wissen nun, was boolesche Ausdrücke sind. Als nächstes wollen wir lernen, wie man sie in Python erstellt. 

Einen booleschen Ausdruck erstellen wir, indem wir **Vergleichsoperatoren** verwenden.
Vergleichsoperatoren vergleichen zwei Elemente und geben entweder `True` oder `False` zurück. 

Die beiden Vergleichsoperatoren, die wir zuerst behandeln werden, sind:

- Gleich: `==`
- Ungleich: `!=`


Diese Operatoren vergleichen zwei Elemente und geben `True` oder `False` zurück, wenn sie gleich oder ungleich sind.

Wir können boolesche Ausdrücke erstellen, indem wir zwei Werte mit diesen Operatoren vergleichen:

```python
1 == 1 # Wahr
 
2 != 4 # Wahr
 
3 == 5 # Falsch
 
'7' == 7 # Falsch
```

Jeder dieser Ausdrücke ist ein Beispiel für einen booleschen Ausdruck.

Warum ist die letzte Aussage falsch? Durch die ''-Markierungen in '7' handelt es sich um einen String. Somit unterscheidet 
er sich vom Integer 7. Bei der Verwendung von Vergleichsoperatoren ist es also wichtig, immer auf den Typ zu achten.

Aufgabe
----

Weisen Sie den Variablen jeweils den Wert `True` oder `False`zu.

Statement one:

`(5 * 2) - 1 == 8 + 1`

Statement two:

`13 - 6 != (3 * 2) + 1`

Statement three:

`3 * (2 - 1) == 4 - 1`
