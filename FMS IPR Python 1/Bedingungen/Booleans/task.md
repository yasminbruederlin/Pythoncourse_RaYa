Booleans
=======

Bevor wir fortfahren, sollten wir ein wenig über `True` und `False` sprechen. Wie Sie wahrscheinlich gemerkt haben, 
erscheinen die Ausdrücke bei der Eingabe im Code-Editor in einer anderen Farbe. Das liegt daran, dass `True` und `False` ein 
eigener Typ sind: **Boolean** (kurz: bool).

`True` und `False` sind die einzigen booleschen Typen. Eine Variable, der einer dieser Werte zugewiesen wurde, wird als Boolean
 bezeichnet.

Booleans können auf verschiedene Weise erstellt werden. Der einfachste Weg ist, einer Variablen einfach `True` oder `False` zuzuweisen:

````python
set_to_true = True
set_to_false = False
````

Sie können auch eine Variable gleich einem booleschen Ausdruck setzen.
```python
bool_one = 5 != 7 
bool_two = 1 + 1 != 2
bool_three = 3 * 3 == 9
```

Wenn Sie diese Variablen nun printen, erscheint jeweils der zugewiesene Boolean.

```python
print(bool_one) # True
print(bool_two) # False
print(bool_three) # True
```

Aufgabe
------
1. Erstellen Sie eine Variable `cool_bool` und weisen Sie ihr den Wert `"true"`zu.

2. Printen Sie den Typen der Variablen indem Sie den Befehl `type(cool_bool)` verwenden.

Hoppla - es handelt sich nicht um einen Boolean! `True` und `False` müssen immer gross geschrieben werden und haben 
   keine Anführungszeichen!

3. Erstellen Sie eine zweite Variable `cool_bool_two` und weisen Sie Ihr den Wert `True`zu.

4. Printen Sie den Typen der neuen Variable.

