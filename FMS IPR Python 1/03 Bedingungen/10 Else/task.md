Else
=============

Wie Sie bei der letzten Aufgabe gemerkt haben, wir ein Code mit vielen if-statements schnell unübersichtlich.

Mit **else**-statements können wir auf elegante Weise beschreiben, was unser Code tun soll, wenn bestimmte Bedingungen nicht erfüllt sind.

Else-statements treten immer in Verbindung mit if-statements auf. 

```python
if weekday:
  print("Aufwachen um 6:30")
else:
  print("Weiterschalfen")
```

 
Auf diese Weise müssen wir nicht für jede mögliche Bedingung eine if-statement schreiben. Stattdessen können wir ein
pauschales else-statement für alle Fälle schreiben, in denen die Bedingung nicht erfüllt ist.

Kehren wir zu unserer Streaming-Plattform zurück. Bisher wurde nur geprüft, ob die Benutzer:in älter als 13 Jahre ist. 
Wir können nun ein else-statement verwenden, um zwei verschiedene Meldungen zu printen.

```python
if age >= 13:
  print("Zugang gewährt.")
else:
  print("Du musst mindestens 13 Jahre alt sein, um diesen Film zu sehen.")
```

Aufgabe
------

1. Passen Sie den Code so an, dass er bei Nichterfüllung der Bedingung folgendes printed:

> "Sie erfüllen die notwendigen Bedingungen nicht."