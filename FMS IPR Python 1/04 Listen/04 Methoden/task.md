Methoden
=========
In den nächsten Übungen werden wir auf das Konzept einer **Methode** stoßen.

In Python gibt es für jeden Datentypen (String, Boolean, Listen etc.) eingebaute Funktionalitäten (z.B. um Daten zu erstellen, manipulieren oder sogar löschen). 
Wir nennen eine eingebaute Funktionalität eine Methode.

Bei Listen haben die Methoden die Form von `list_name.method()`. Einige Methoden erfordern einen Eingabewert, der zwischen 
die Klammern der Methode `( )` gesetzt wird.

Ein Beispiel für eine Listenmethode ist `.append()`. Mit dieser Methode können wir ein Element an das Ende einer Liste anfügen.

```python
append_example = [ 'Dies', 'ist', 'ein']
append_example.append('Beispiel')
 
print(append_example)
```

Printed folgendes:

```python
['Dies', 'ist', 'ein', 'Beispiel']
```

Auch auf Strings können diverse Methoden angewendet werden. 
Folgender Code erzeugt die Ausgabe der Zahl 2. 

````python
txt = "I love apples, apple are my favorite fruit"

x = txt.count("apple")

print(x)
````

#Aufgabe
Recherchieren Sie zu Stringmethoden. Können Sie mit der passenden Methode den ersten Buchstaben des Namens gross schreiben?
