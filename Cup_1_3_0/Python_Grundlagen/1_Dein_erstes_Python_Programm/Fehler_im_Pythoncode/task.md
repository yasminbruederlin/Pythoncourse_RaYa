# Fehler im Pythoncode

Jeder macht Fehler, insbesondere beim programmieren!
Grundsätzlich sind in Python die Syntax- und Laufzeitfehlern zu 
unterscheiden.

## Syntaxfehler (syntax errors)

````python
File "../Fehler_im_Pythoncode/task1.py", line 1
    print('Hallo Welt)                 ^
SyntaxError: EOL while scanning string literal
````
siehe task1.py

Syntaxfehler sind somit Fehler, welche den Sprachdefinition von Python verletzen. Im Beispiel `task1.py` 
ist dies beispielsweise das fehlende Hochkomma (`'` oder `"`).

## Laufzeitfehler (runtime errors)

````python
File "../Fehler_im_Pythoncode/task2.py", line 1, in <module>
    print(Hallo, Welt)
NameError: name 'Hallo' is not defined
````
siehe task2.py

Laufzeitfehler sind Fehler welche während der Ausführung des Programmes entstehen.
Im Beispiel `task2.py` wird der Fehler erzeugt als Folge der fehlenden Hochkommas. 
Der Pythoninterpreter betrachtet den Ausdruck `Hallo, Welt` als zwei Variablen, welche
im Terminal mittels dem `print` ausgegeben werden sollen. Variablen welche keine vorgängige
Zuweisung erhalten haben, sind undefiniert.