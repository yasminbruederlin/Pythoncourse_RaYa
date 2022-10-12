# Standardwerte bei Funktionen
Betrachten wir nochmals die Funktion `fmac`
```python
def fmac(a, b, c):
    result = a * b + c
    return result
```
Bei einem Funktionsaufruf sind stehts alle Parameter zu übergeben.  
Diese Funktion möchten wir nun so eweitern, dass ein Funktionsaufruf möglich ist, auch wenn nicht
alle Parameter übergeben werden. Dies kann erreicht werden durch hinzufügen von Standardwerten in der
Funktionssignatur.
```python
def fmac(a=1.0, b=2.0, c=3.0):
    result = a * b + c
    return result
```
Der Funktionsaufruf ist nun auch möglich, auch wenn nur 2 der drei Parameter übergeben werden.
```python
result_1 = fmac(1.0, 2.0)
```
In diesem Konzept folgt Python der Reihenfolge gemäss der Funktionssignatur. Wird beim Aufruf nebst dem Wert auch 
der Parametername hinzugefügt, kann die Reihenfolge der Parameter anders geordnet werden. Sind sämtliche Parameter
einer Funktion mit Standardwerten belegt, kann auch ein Funktionsaufruf ohne Angabe von Parametern erfolgen.
```python
result_2 = fmac(b=4.0, c=5.0)
result_3 = fmac(c=6.0)
result_4 = fmac()
```

# Return

Jede Funktion liefert einen Rückgabewert. Auch wenn dieser nicht explizit verwendet wird. In
diesem Fall wird ein `None` als Rückgabewert der Funktion geliefert.

```python
def fun():
    print('fun')

fun_return = fun()
```

Funktionen müssen nicht zwingend einen Rückgabewert enthalten. Wird der Rückgabewert `return`
nicht verwendet, wird die entsprechende Funktion mit `None` abgeschlossen.
