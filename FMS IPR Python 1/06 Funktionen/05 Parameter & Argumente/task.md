Parameter & Argumente
======

Als nächstes betrachten wir die Funktion `trip_welcome()`. Sie ist wie folgt definiert

```python
def trip_welcome():
  print("Willkommen bei Tripprojekte!") 
  print("Sieht aus, als würden Sie heute zum Times Square gehen.")
```

Als nächstes ändern wir unsere Funktion, um eine etwas ausführlichere Begrüßung zu geben.

```python
def trip_welcome():
  print("Willkommen bei Tripprojekte!") 
  print("Sieht aus, als würden Sie heute zum Times Square gehen.")

trip_welcome()
```

Wenn wir den Code ausführen, wird folgendes geprinted:

```python
Willkommen in der Tripprojekte!
Sieht aus, als würden Sie heute zum Times Square gehen.
```

Unsere Funktion funktioniert gut bei der Begrüßung von Personen, die zum Times Square fahren, aber schlecht, wenn sie woanders hinfahren. Um unsere Funktion ein wenig dynamischer zu gestalten, werden wir das Konzept von Parametern verwenden.

Parameter ermöglichen es unserer Funktion, Daten als Eingabewert zu akzeptieren. Wir führen die Parameter, die eine Funktion als Eingabe akzeptiert, zwischen den Klammern einer Funktion `( )` auf.

Hier ist eine Funktion, die einen einzelnen Parameter definiert:

```python
def meine_funktion(einzelner_parameter)
  # etwas Code
```

Im Zusammenhang mit unserer Funktion `trip_welcome()` würde das so aussehen:

````python
def trip_welcome(destination):
  print("Willkommen bei Tripprojekte!") 
  print("Sieht aus, als würden Sie heute nach " + destination + " fahren.")
````

Im obigen Beispiel definieren wir einen einzelnen Parameter namens `destination` und verwenden ihn in unserem _function body_ in der zweiten print-Anweisung. Wir teilen unserer Funktion mit, dass sie einige Daten erwarten soll, die für `destination` übergeben werden und die sie auf alle Anweisungen im _function body_ anwenden kann.

Aber wie verwenden wir diesen Parameter tatsächlich? Unser Parameter für das Ziel wird verwendet, indem wir der Funktion ein Argument übergeben, wenn wir sie aufrufen.

`trip_welcome("Times Square")`

Dies printed folgendes:

```python
Willkommen bei Tripprojekte!
Sieht so aus, als würden Sie heute zum Times Square fahren. 
```

Zusammenfassend wird hier kurz der Unterschied zwischen einem Parameter und einem Argument erläutert:

- Der Parameter ist der Name, der in der Klammer der Funktion definiert ist und im _function body_ verwendet werden kann (im Beispiel: `destination`).


- Das Argument sind die Daten, die beim Aufruf der Funktion übergeben und dem Parameternamen zugewiesen werden (im Beispiel `"Times Square"`).

Aufgaben
----------

Wir wollen ein Programm erstellen, mit dem unsere Benutzer die Wegbeschreibung für ihre bevorstehende Reise generieren können!

1. Erstellen Sie eine Funktion namens `generate_trip_instructions()`, die einen Parameter namens `location` definiert.


2. `generate_trip_instructions()` sollte das Folgende printen:

```python
Sieht aus, als planten Sie eine Reise zu <location>.
```
Dabei steht <location> für den Ortsparameter.

3. `generate_trip_instructions()` sollte unsere Benutzer auch wissen lassen, dass sie ihren Standort mit öffentlichen Verkehrsmitteln erreichen können.

Lassen wir `generate_trip_instructions()` auch das Folgende in einer neuen Zeile printen:

```python
Sie können die öffentliche U-Bahn benutzen, um nach <location> zu gelangen.
```
Dabei steht <location> für den Ortsparameter.


   
4. Zeit für etwas Grünes! Schauen wir uns an, was passiert, wenn wir die Funktion aufrufen und das Argument `"Central Park"` eingeben, ein Hinterhofwunder im Herzen von New York City.


5. Der Tagesausflug ist vorbei und wir müssen zurück zum Bahnhof, um nach Hause zu fahren. Ändern Sie das Argument zu `"Grand Central Station"` und rufen Sie die Funktion erneut auf.

Was hat sich an der Ausgabe geändert?
