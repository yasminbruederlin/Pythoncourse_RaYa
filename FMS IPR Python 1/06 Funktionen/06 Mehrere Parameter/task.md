Mehrere Parameter
======

Die Verwendung eines einzelnen Parameters ist nützlich, aber mit Funktionen können wir so viele Parameter verwenden, wie wir wollen! Auf diese Weise können wir mehr als einen Parameter an unsere Funktionen übergeben.

Wir können eine Funktion schreiben, die mehr als einen Parameter annimmt, indem wir Kommas verwenden:

```python
def my_function(parameter1, parameter2, parameter3):
  # Some code
```

Wenn wir unsere Funktion aufrufen, müssen wir Argumente für jeden der Parameter angeben, die wir in unserer Funktionsdefinition zugewiesen haben.

```python
# Aufruf von my_function
my_function(argument1, argument2)
```

Nehmen wir zum Beispiel die Funktion `trip_welcome()` unserer Reiseapp, die zwei Parameter hat:

```python
def trip_welcome(origin, destination):
  print("Willkommen bei Tripprojekte")
  print("Sieht aus, als kämen Sie von " + origin)
  print("Und Sie sind auf dem Weg nach " + destination)
```

Unsere beiden Parameter in dieser Funktion sind `origin` und `destination`. Um unsere Funktion richtig aufzurufen, müssen wir für beide Argumente Werte übergeben.

Die Reihenfolge der Parameter ist wichtig, da ihre Position der Position der Argumente entspricht und den ihnen zugewiesenen Wert im Funktionskörper bestimmt (mehr dazu in der nächsten Übung!).

Unser Funktionsaufruf könnte wie folgt aussehen:

```python
trip_welcome("Prospect Park", "Atlantic Terminal")
```

In diesem Aufruf wird das Argument `"Prospect Park"` dem `origin`-Parameter und das Argument `"Atlantic Terminal"` dem `destination`-Parameter zugewiesen.

Es wird folgendes geprinted:

```python
Willkommen bei Tripprojekte
Sieht aus, als kämen Sie von Prospect Park
Und Sie sind auf dem Weg nach Atlantic Terminal
```

Aufgaben
----------

Die Benutzer unserer Reiseapp möchten die Gesamtkosten berechnen, die auf einer Reise entstehen können.

1. Schreiben Sie eine Funktion namens `calculate_expenses`, die vier Parameter hat (in genauer Reihenfolge):

- plane_ticket_price
- car_rental_rate
- hotel_rate
- trip_time

Jeder dieser Parameter steht für eine andere Ausgabe, die unseren Benutzern entstehen wird.

2. Im _function body_ beginnen wir mit einigen Berechnungen für unsere Ausgaben. Berechnen wir zunächst den Gesamtpreis für eine Autovermietung.
Erstellen Sie eine neue Variable namens `car_rental_total`, die das Produkt aus `car_rental_rate` und `trip_time` ist.


Als Nächstes wollen wir die gleiche Logik anwenden, aber für unsere `hotel_rate`.

3. Erstellen Sie eine neue Variable namens `hotel_total`, die das Produkt aus `hotel_rate` und `trip_time` ist.

Wir haben auch einen Gutschein, um unseren Nutzern etwas Cashback für ihren Hotelbesuch zu geben, also subtrahieren Sie 10 von dieser Summe in der gleichen Anweisung. Woohoo, Gutscheine! `#allescoolichhab'money`


4. Zum Schluss geben wir eine nette Nachricht aus, damit unsere Benutzer die Gesamtsumme sehen können. Verwenden Sie print, um die Summe von `car_rental_total`, `hotel_total` und `plane_ticket_price` auszugeben.

5. Rufen Sie Ihre Funktion mit den folgenden Argumenten für die aufgeführten Parameter auf:

- plane_ticket_price : 200
- car_rental_rate : 100
- hotel_rate: 100
- trip_time: 5
