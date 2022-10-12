# Funktionen

Bis jetzt haben wir Funktionen als Aufrufe, welche mit runden Klammern am Ende abgeschlossen wurden, betrachtet. 
als exemplarische Beispiele können an dieser Stelle die Funktionen `len()` und `range()` aufgeführt werden.

Grundsätzlich trennen Funktionen Codeblöcke in kleinere Einheiten mit definierter Schnittstellenbeschreibung.
Anstatt die immer gleichen Ablaufschritte wiederholend niederzuschreiben, kann durch den Einsatz einer Funktion
diese Problemstellung in einer allgemeinen Form zusammengefasst werden.

# Struktureller Aufbau von Funktionen
Eine Funktion besteht aus zwei Elementen:

1. Die Signatur bestehend aus Name und den erwarteten Übergabeparametern.
2. Dem Funktionskörper in welchem der Quellcode hinterlegt wird.

Dieses Konzept soll exemplarisch an einer Funktion aufgezeigt werden welche zwei Zahlen multipliziert und anschliessend
um eine weitere Zahl addiert.
```python
def fmac(a, b, c):
    result = a * b + c
    return result
```

Bei der Syntax für die Erstellung von Funktionen gilt es zu beachten:

- Eine Funktion wird durch das Schlüsselwort `def` eingeleitet.
- Anschliessend folgt der Funktionsname.
- In runden Klammern werden die Uebergabewerte (Parameter der Funktion) aufgelistet.
- Ein Doppelpunkt `:` welcher die Signatur abschliesst. 
- Der Funktionskörper ist eingerückt.
- Falls die Funktion Rückgabewerte liefert, werden diese an das `return` Schlüsselwort angehängt.

Der Aufruf der Funktion `fmac` erfolgt  im Anschluss an die Funktionsdefintion:
```python
result_1 = fmac(1.0, 2.0, 3.0)
result_2 = fmac(4.0, 5.0, 6.0)
result_3 = fmac(7.0, 8.0, 9.0)
```

## Funktionsparameter
Funktionen ermöglichen eine allgemeingültige Beschreibung einer Aufgabenstellung. Durch die Uebergabe
von Parametern an die Funktion, wird der Wert von der Variablen welche im Funktionsaufrug als Übergabe
benutzt wird von der eigentlichen Funktion entkoppelt. 

```python
a_caller = 1.0
b_caller = 2.0
c_caller = 3.0
result = fmac(a_caller, b_caller, c_caller)
```

Bei der Funktionsübergabe übergibt wird der Wert der Variablen `a_caller` an den Funktionsparameter
`a` der Funktion fmac übergeben. Im inneren der Funktion erfolgt der Zugriff auf den Wert über den
Funktionsparameter `a`, welcher wie eine normale Variable behandelt wird.
