Break
========


Manchmal ist es hilfreich einen Loop zu beenden, wenn ein bestimmtes Ereignis während des Loops eintritt.

Nehmen wir die folgende Liste `items_on_sale` als Beispiel:

```python
items_on_sale = ["blue shirt", "striped socks", "knit dress", "red headband", "dinosaur onesie"]
```

Wie sieht unser Loop aus, wenn wir nach dem Wert `"knit dress"` suchen und `"Found it"` printen wollen, wenn er existiert?

Der Loop würde etwa so aussehen:

```python
for item in items_on_sale:
  if item == "knit dress":
    print("Found it")
```

Dieser Code durchläuft jeden Artikel in `items_on_sale` und sucht nach einer Übereinstimmung. 
Das ist alles schön und gut, aber was ist das Problem?

Sobald `"knit_dress"` in der Liste `items_on_sale` gefunden wurde, brauchen wir den Rest der Liste `items_on_sale` nicht mehr zu durchlaufen. 
Leider wird unsere Schleife aber so lange laufen, bis wir das Ende der Liste erreicht haben.

Da die Liste nur 5 Elemente umfasst, ist das Durchlaufen der gesamten Liste in diesem Fall keine große Sache. Aber was
würde passieren wenn `items_on_sale` 1'000'000 Elemente hätte? Das wäre eine enorme Zeitverschwendung für unser Programm!

Glücklicherweise können Sie die Iteration innerhalb der Schleife mit der Anweisung `break` stoppen.

Wenn das Programm auf eine break-Anweisung trifft, wird die Schleife sofort beendet. Zum Beispiel:

```python
items_on_sale = ["blue shirt", "striped socks", "knit dress", "red headband", "dinosaur onesie"]
 
print("Checking the sale list!")
 
for item in items_on_sale:
  print(item)
  if item == "knit dress":
    break
 
print("End of search!")
```

Printed folgendes:

```python
Checking the sale list!
blue shirt
striped socks
knit dress
End of search!
```

Sobald wir zur break-Anweisung kamen, wurde der Loop sofort beendet. 
Wir mussten also die Elemente "read headband" oder "dinosaur onesie" gar nicht überprüfen.

Aufgaben
---------

Sie möchten einen Hund adoptieren. Zur Auswahl steht eine Liste von Hunderassen, die Sie in 
`dog_breeds_available_for_adoption` finden.

1. Verwenden Sie einen for-Loop, um die Liste `dog_breeds_available_for_adoption` zu durchlaufen und jede Hunderasse zu printen.
Tipp: Verwenden Sie eine temporäre Variable namens `dog_breed`.

2. Prüfen Sie im for-Loop, ob das aktuelle Element in `dog_breed` gleich `dog_breed_I_want` ist (nachdem Sie geprinted haben). 
   Wenn ja, printen Sie "They have the dog I want!"

3. Fügen Sie eine break-Anweisung ein, sobald dog_breed_I_want gefunden wurde. 
