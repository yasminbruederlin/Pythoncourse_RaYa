Funktionsdefinition
======

Eine Funktion besteht aus vielen Teilen, also machen wir uns zunächst mit ihrem Kern vertraut - einer Funktionsdefinition.

Hier ist ein Beispiel für eine Funktionsdefinition:

```python
def funktion_name():
  # functions tasks go here
```

Es gibt einige wichtige Komponenten, die wir hier beachten sollten:

- Das Schlüsselwort `def` kennzeichnet den Anfang einer Funktion (auch Funktionskopf genannt). Auf den Funktionskopf folgt ein Name im snake_case-Format, der die Aufgabe beschreibt, die die Funktion ausführt. Am besten geben Sie Ihren Funktionen einen aussagekräftigen und dennoch prägnanten Namen.
- Nach dem Funktionsnamen folgt ein Klammerpaar `( )`, das Eingabewerte enthalten kann, die als Parameter bezeichnet werden (mehr zu Parametern später in dieser Lektion!). In dieser Beispielfunktion haben wir keine Parameter.
- Ein Doppelpunkt `:` kennzeichnet das Ende des Funktionskopfes.
- Schließlich haben wir eine oder mehrere gültige Python-Anweisungen, die den _function body_ bilden (wo wir unseren Python-Kommentar haben).

Beachten Sie, dass wir unseren Kommentar `# function tasks go here` eingerückt haben. Wie Schleifen und Bedingungen muss auch der Code innerhalb einer Funktion eingerückt werden, um zu zeigen, dass er Teil der Funktion ist.

Hier ist ein Beispiel für eine Funktion, die einen Benutzer für unsere Reiseplanungsanwendung begrüßt:

```python
def trip_welcome():
  print("Willkommen bei Tripcademy!") 
  print("Bringen wir Sie zu Ihrem Ziel.")
```

Hinweis: Wenn Sie diesen Code in den Editor einfügen und ausführen, erhalten Sie ein leeres Ausgabe-Terminal. Die print()-Anweisungen innerhalb der Funktion werden nicht ausgeführt, da unsere Funktion nicht verwendet wurde. Wir werden dies in der nächsten Übung weiter erforschen; lassen Sie uns jetzt erst einmal üben, eine Funktion zu definieren.

Aufgaben
----------

1. Definieren Sie zunächst eine Funktion, `directions_to_timesSq()`. Lassen Sie den _function body_ vorerst leer.

2. Verwenden Sie innerhalb des _function bodys_ der Funktion drei print()-Anweisungen, um die folgenden Anweisungen auszugeben:
```python
Laufen Sie 4 Minuten, um zur 34th St Herald Square Bahnstation zu gelangen.
Nehmen Sie die Züge N, Q, R oder W in Richtung Norden, 1 Haltestelle.
Steigen Sie an der Haltestelle Times Square 42nd Street aus.
```

In der nächsten Übung werden Sie sehen, ob Sie die Funktion richtig implementiert haben.
