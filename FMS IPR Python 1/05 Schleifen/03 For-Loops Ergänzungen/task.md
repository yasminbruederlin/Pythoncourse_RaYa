# Hinweise zu For-Schleifen

##Temporäre Variablen

Der Name einer temporären Variable ist frei wählbar und muss nicht vorher definiert werden. Die beiden folgenden 
Codeschnipsel tun genau das Gleiche:

```python
for i in ingredients:
  print(i)
for item in ingredients:
 print(item)
```

Da bei jeder Iteration unserer Schleife auf eine Zutat zugegriffen wird, ist es aus Gründen der Lesbarkeit sinnvoller, unsere temporäre Variable 
`ingredient` zu nennen anstatt `i` oder `item`, da.

##Einrückungen

Bei einem Loop muss die `<Aktion>` immer eingerückt sein. Alles, was auf eingerückt nach dem for-Loop steht, 
wird bei jeder Iteration der Schleife ausgeführt.

```python
for ingredient in ingredients:
  # Jeder Code auf dieser Ebene der Einrückung 
  # wird bei jeder Iteration der Schleife ausgeführt
  print(ingredient)
```

Falls wir das Einrücken vergessen, erhalten wir einen `IndentationError` (Einrückungsfehler) oder ein unerwartetes Verhalten.

<span style="color:turquoise;font-weight:700;font-size:25px">
Aufgabe
</span>

1. Führen Sie den Code aus. Es sollte ein IndentationError geben.

2. Korrigieren Sie den Code, indem Sie die richtige Zeile korrekt einrücken.

3. Schreiben Sie einen for-Loop, um alle Sportarten zu printen.
