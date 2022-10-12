Boolesche Operatoren: Not
==============

`not` ist ganz einfach: Wenn er auf einen beliebigen booleschen Ausdruck angewendet wird, kehrt er den booleschen Wert um. 
Wenn wir ihn also vor einen Ausdruck, der `True` zurückgibt, setzen, erhalten wir einen `False`.

```python
not True == False
not False == True
```

Betrachten wir die folgenden Beispiele:

```python
not 1 + 1 == 2 # False
not 7 < 0 # True
```

Wichtig: `not` steht immer vor dem Ausdruck!

Aufgabe
---------

Die Schulleitung hat von Ihren Programmierskills erfahren und ist beeindruckt. Sie möchte, dass Sie Ihr Skript folgendermassen 
anpassen.

1. Wenn eine Schüler:in **nicht** einen Notendurchschnitt von 4.0 oder höher hat, printen Sie:

> "Ihr Notendurchschnitt reicht leider nicht für einen Abschluss aus."

2. Wenn eine Schüler:in **nicht** weniger als 20 unentschuldigte Versäumnisse besitzt, printen Sie:

> "Sie haben leider zu viele unentschuldigte Versäumnisse, um an der FMS abzuschliessen."

3. Wenn Sie beide Bedingungen nicht erfüllen, printen Sie:

> "Sie erfüllen keine der Bedingungen. Somit verpassen Sie Ihren Abschluss."

