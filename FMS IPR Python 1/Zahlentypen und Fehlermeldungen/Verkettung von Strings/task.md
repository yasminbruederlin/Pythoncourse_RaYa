
# Verkettung von Strings


Der Operator `+` kann nicht nur zwei Zahlen addieren, sondern auch zwei Strings! Dieser Vorgang wird als
 **Verkettung von Strings** bezeichnet. Dabei wird ein neuer String erstellt, die aus dem Inhalt des ersten Strings
 und dem Inhalt des zweiten Strings besteht (ohne dazwischen liegende Leerzeichen).

   

  
````python
greeting = "Hallo"
question = "Wie geht es dir?"
text = greeting + question

# printed "Hallo!Wie geht es dir?"
print(text)
````
  


In diesem Codebeispiel fehlt ein Leerzeichen zwischen den beiden Strings.
 Wir können das Leerzeichen wieder mit dem `+` Operator hinzufügen.

````python
greeting = "Hallo"
question = "Wie geht es dir?"
text = greeting + " " + question

# printed "Hallo! Wie geht es dir?"
print(text)
````

Jetzt printed der Code die erwartete Nachricht.
  

  

Wenn wir einen String mit einer Zahl verknüpfen wollen, müssen wir zuerst die Zahl in einen String umwandeln.
 Dafür verwenden wir die Funktion `str()`.
   
```python
first = "Ich bin heute"
age = 17
second = "Jahre alt!"

# Verkettung von Strings mit einer Zahl
text = first + " " + str(age) + " " + second

# printed "Ich bin heute 17 Jahre alt!
print(text)
```

Wenn wir eine Zahlenvariable zusammen mit Strings nur printen möchten, können wir dies mit der Hilfe von Kommas machen.

```python
first = "Ich bin heute"
age = 17
second = "Jahre alt!"

# printed "Ich bin heute 17 Jahre alt!
print("first", age, "second")

```
  

Wenn wir nur eine ganze Zahl ausgeben wollen
können wir eine Variable als Argument an print() übergeben, unabhängig davon, ob es ein String ist.




## Aufgabe


Verketten Sie die Strings und speichern Sie die Nachricht, die sie bilden, in der Variablen `message`. Printen Sie
 den Inhalt der Variable `message`



