# Plus-Gleich


Python bietet eine Kurzform für die Aktualisierung von Variablen. Wenn Sie eine Zahl in einer Variablen gespeichert haben und zum aktuellen Wert der Variablen addieren wollen, können Sie den Operator += (plus-gleich) verwenden.

   

  
```python
# Zuerst weisen wir der Variablen einen Startwert zu.
nr_hiked_km = 12

# Dann verändern wir den Wert der Variablen.
# Nehmen wir an, dass wir 2 weitere Kilometer 
# gewandert sind.
nr_hiked_km += 2

# Der neue Wert ist der alte Wert
# plus die Zahl nach dem Plus-Gleich-Zeichen.
# printed "14"
print(nr_hiked_km)
```

  

Die Variable oben speichert die Anzahl Kilometer, die eine Person im Laufe der Zeit gewandert ist. Anstatt den Wert der
 Variable jeweils neu zu berechnen, können wir den alten Wert einfach aktualisieren.

   

  


Der Plus-Gleich-Operator kann auch für die Verkettung von Strings verwendet werden:

```python
hike_caption = "Was für eine tolle Zeit, um durch die Natur zu wandern!"

# Fast hätte ich die Hashtags vergessen! #Boomer
hike_caption += " #nofilter"
hike_caption += " #blessed"
```

   



## Aufgabe


Sie sind gerade beim Online-Shopping und finden ein Paar neue Turnschuhe. Kurz bevor wir Sie zum Checkout gehen,
 entdecken Sie einen schönen Pullover und ein paar tolle Bücher, die Sie auch kaufen wollen.

   

  


 1. Verwenden Sie den `+=`-Operator, um die Variable `total_price` zu aktualisieren und die Preise
 von `nice_sweater` und `fun_books` dazuzurechnen. Printen Sie anschliessend das Ergebnis.
 

2. **Bonus:** Ist das Resultat ein `int` oder ein `float`?

