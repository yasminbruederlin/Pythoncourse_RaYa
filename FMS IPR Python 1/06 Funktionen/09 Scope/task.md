Scope
======

Wenn wir unsere Programme um weitere Funktionen erweitern, stellen wir uns vielleicht die Frage: Wo genau haben wir Zugriff auf unsere Variablen? (Man spricht bei dieser Frage auch von der Sichtbarkeit der Variablen, i.e. welche Funktion _sieht_ die Variablen?) Um dies zu untersuchen, schauen wir uns eine modifizierte Version der ersten Funktion an, die wir gemeinsam entwickelt haben:

```python
def trip_welcome(destination):
  print(" Sieht aus, als würden Sie nach " + destination + " fahren.")
```

Was wäre, wenn wir auf die Variable `destination` außerhalb der Funktion zugreifen wollten? Könnten wir sie verwenden? Nehmen Sie sich einen Moment Zeit, um darüber nachzudenken, was das folgende Programm printen wird, und überprüfen Sie dann das Ergebnis unten!

```python
def trip_welcome(destination):
  print(" Sieht aus, als würden Sie nach " + destination + " fahren.")
 
print(destination)
```

Der Output würde folgendermassen aussehen:

```python
NameError: name 'destination' is not defined
```

Wenn wir versuchen, diesen Code auszuführen, erhalten wir einen `NameError`, da `destination` nicht definiert ist. Der Grund dafür ist, dass die Variable `destination` nur innerhalb einer Funktion definiert wurde, sie existiert also nicht außerhalb der Funktion.

Wir nennen den Teil eines Programms, in dem auf `destination` zugegriffen werden kann **scope**. Der **scope** von `destination` befindet sich nur innerhalb von `trip_welcome()`.

Schauen Sie sich ein weiteres Beispiel an:

```python
budget = 1000
 
# Hier verwenden wir einen default-Wert für unseren Parameter destination. 
def trip_welcome(destination="California"):
    print(" Sieht aus, als würden Sie nach " + destination + " fahren")
    print(" Ihr Budget für diese Reise ist " + str(budget))
 
print(budget)
trip_welcome()
```

Das Beispiel würde folgendes printen:

```python
1000
Sieht aus, als würden Sie nach Kalifornien fahren 
Ihr Budget für diese Reise beträgt 1000
```

Hier können wir auf `budget` sowohl in der Funktion `trip_welcome` als auch in der Anweisung `print()` zugreifen. Wenn sich eine Variable außerhalb einer Funktion befindet, kann auf sie überall in der Datei zugegriffen werden.

Wir werden das Konzept des scopes nach dieser Lektion noch genauer anschauen. Jetzt wollen wir erst einmal ein bisschen herumspielen!

Hinweis: Die Arbeit mit mehreren Funktionen kann anfangs etwas überwältigend sein. Zögern Sie nicht, mich mit Fragen zu löchern :)

Aufgaben
----------

Unsere Benutzer möchten eine Liste ihrer Lieblingsorte in unserer Reise-App speichern können.
Wir haben einen groben Entwurf für diese Implementierung von einem anderen Programmierer erhalten, aber es gibt einige Probleme mit dem scope der Variablen, die verhindern, dass es richtig funktioniert.

1. Führen Sie den Code aus und untersuchen Sie den Fehler.

2. Wenn man sich den Fehler ansieht, scheint das Hauptproblem zu sein, dass `favorite_locations` nicht definiert ist. Warum sollte unser Programm nicht in der Lage sein, die Variable `favorite_locations` zu sehen?

Aha! Es muss ein Problem mit dem scope der Variable geben. Ändern Sie den scope von `favorite_locations`, damit unsere beiden Funktionen darauf zugreifen können.

