Verschiedene Arten von Argumenten
======

In Python gibt es 3 verschiedene Arten von Argumenten, die wir einer Funktion geben können.

- _positional arguments_: Argumente, die durch ihre Position in der Funktionsdefinition aufgerufen werden können.
- _keyword arguments_: Argumente, die über ihren Namen aufgerufen werden können.
- _default arguments_: Argumente, die mit Standardwerten versehen sind.

_Positional arguments_ sind Argumente, die wir bereits verwendet haben! Ihre Zuweisung hängt von ihrer Position im Funktionsaufruf ab. 
Schauen wir uns eine Funktion namens `calculate_taxi_price()` an, mit der unsere Benutzer sehen können, wie viel ein Taxi zu ihrem Zielort kosten würde.

```python
def calculate_taxi_price(miles_to_travel, rate, discount):
  print(miles_to_travel * rate - discount )
```

In dieser Funktion steht `miles_to_travel` als erster Parameter, `rate` als zweiter Parameter und `discount` als dritter Parameter. Wenn wir unsere Funktion aufrufen, wird die Position der Argumente auf die in der Funktionsdeklaration definierten Positionen abgebildet.

```python
# 100 ist miles_to_travel
# 10 ist rate
# 5 ist discount
calculate_taxi_price(100, 10, 5)
```

Alternativ können wir auch _keyword arguments_ verwenden, bei denen wir explizit darauf verweisen, was den einzelnen Argumenten im Funktionsaufruf zugewiesen ist. Beachten Sie im folgenden Codebeispiel, dass die Argumente nicht in der gleichen Reihenfolge wie in der Funktionsdeklaration angegeben sind.

````python
calculate_taxi_price(rate=0,5, discount=10, miles_to_travel=100)
````

Manchmal möchten wir unseren Argumenten auch `default`-Werte zuweisen. Wir können einem Argument einen `default`-Wert zuweisen, indem wir `=`verwenden. Dies geschieht in der Funktionsdeklaration und nicht im Funktionsaufruf.

Hier ein Beispiel, bei dem das Argument `discount` in unserer Funktion `calculate_taxi_price` immer den `default`-Wert 10 hat:

```python
def calculate_taxi_price(miles_to_travel, rate, discount = 10):
  print(miles_to_travel * rate - discount )
```

Wenn wir einen `default`-Wert verwenden, können wir entweder die Funktion aufrufen, ohne einen Wert für `discount` anzugeben (dann verwendet unsere Funktion den zugewiesenen `default`-Wert), oder wir überschreiben das _default argument_, indem wir unseren eigenen Wert angeben:

```python
# Verwendung des `default`-Wert 10 für discount.
calculate_taxi_price(10, 0.5)
 
# Überschreiben des `default`-Werts 10 mit 20
calculate_taxi_price(10, 0.5, 20)
```

Aufgaben
----------

1. Schreibe eine Funktion namens `trip_planner()`, die drei Parameter hat: `first_destination`, `second_destination` und `final_destination`.

Geben Sie dem Parameter `final_destination` den _default_-Wert `"Informatikprojekte HQ"`.

2. Zuerst wollen wir den Benutzern die Reise vorstellen. Verwenden Sie `print()` in unserer Funktion, um Folgendes auszugeben: `So wird Ihre Reise aussehen!`

3.
In unserer Funktionsdefinition geben wir eine Reiseroute an, die die Ziele beschreibt, die unser Benutzer nacheinander besuchen wird. Geben Sie etwas aus, die dieser Form folgt:

```python
Zuerst halten wir in <first_destination>, dann in <second_destination> und zuletzt in <final_destination>
```
Um Ihre Funktion zu testen, rufen Sie `trip_planner()` mit den folgenden Werten für die Parameter auf:

- first_destination: `"Frankreich"`
- second_destination: `"Deutschland"`
- final_destination: `"Dänemark"`


4.
Rufen Sie die Funktion `trip_planner()` erneut mit den folgenden Werten für die Parameter auf:

- first_destination: `"Dänemark"`
- second_destination: `"Frankreich"`
- final_destination: `"Deutschland"`

5.
Rufen Sie die Funktion `trip_planner()` erneut auf und verwenden Sie die Schlüsselwortargumente in genau dieser Reihenfolge:

- first_destination: `"Island"`
- final_destination: `"Deutschland"`
- second_destination: `"Indien"`

6.
Zum Schluss rufen Sie die Funktion `trip_planner()` mit nur zwei _positional arguments_ auf, um das _default argument_ in Aktion zu sehen:

- first_destination: `"Brooklyn"`
- second_destination: `"Queens"`
