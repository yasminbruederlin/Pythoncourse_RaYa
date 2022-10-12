Mehrere Returns
======

Manchmal möchte man mehr als einen Wert aus einer Funktion zurückgeben. Wir können mehrere Werte zurückgeben, indem wir sie mit einem Komma trennen. Sehen Sie sich dieses Beispiel einer Funktion an, die es den Benutzern unserer Reise-App ermöglicht, das Wetter für die kommende Woche (ab Montag) zu überprüfen:

```python
weather = ['sonnig', 'sonnig', 'bewölkt', 'regnerisch', 'bewölkt']
 
def threeday_weather_report(weather):
  first_day = "Morgen wird das Wetter " + weather[0]
  second_day = "Übermorgen wird es " + weather[1]
  third_day = "In zwei Tagen wird es " + weather[2] 
  return first_day, second_day, third_day
```

Diese Funktion nimmt eine Reihe von Daten in Form einer Liste für das Wetter der kommenden Woche entgegen. Wir können unsere zurückgegebenen Funktionswerte erhalten, indem wir sie beim Aufruf der Funktion Variablen zuweisen:

```python
monday, tuesday, wednesday = threeday_weather_report(weather_data)
 
print(monday)
print(tuesday)
print(wednesday)
```

Printed folgendes:

```python
Morgen wird das Wetter sonnig
Übermorgen wird es sonnig
In zwei Tagen wird es bewölkt
```

Aufgaben
----------
Unsere Benutzer mochten die Funktionen, die wir unserer Reise-App haben. In letzter Zeit hatten wir aber einen Zustrom von Benutzern, die Reisen in Italien planen. Wir möchten eine kleine Funktion erstellen, die die besten Reiseziele in Italien angibt. Ein anderes Mitglied unseres Teams hat bereits mit der Implementierung dieser Funktion begonnen, aber es fehlen noch ein paar wichtige Details.

1. Nehmen Sie sich einen Moment Zeit, um den Code zu überprüfen und klicken Sie auf Ausführen, wenn Sie bereit sind, weiterzumachen. Im Moment gibt es noch keine Ausgabe.
2. Wir möchten die drei beliebtesten Reiseziele aus unserer Funktion top_tourist_locations_italy() zurückgeben.
Fügen Sie eine Zeile in die Funktion `top_tourist_locations_italy()` ein, die die Werte von `first`, `second`, `third` in genau dieser Reihenfolge zurückgibt.
3. Um die drei von `top_tourist_locations_italy()` zurückgegebenen Werte zu verwenden, müssen wir sie nach dem Aufruf unserer Funktion neuen Variablen zuweisen.
Legen Sie den Rückgabewert der Funktion `top_tourist_locations_italy()` so fest, dass er in drei neuen Variablen namens `most_popular1`, `most_popular2` und `most_popular3` in genau dieser Reihenfolge gespeichert wird.
4.Verwenden Sie drei prints, um die Werte von `most_popular1`, `most_popular2` und `most_popular3` auszugeben.


