Built-in Funktionen vs. benutzerdefinierte Funktionen
======

In der Welt von Python gibt es zwei verschiedene Kategorien von Funktionen. Was wir bisher in unseren Übungen geschrieben haben, nennt man **benutzerdefinierte** **Funktionen** - Funktionen, die von Benutzern (wie uns!) geschrieben werden.

Eine andere Kategorie sind die **built-in Funktionen** - Funktionen, die in Python eingebaut sind und die wir verwenden können. Erinnern Sie sich noch daran, wie wir `print` oder `str` benutzt haben? Diese beiden Funktionen sind für uns in die Sprache eingebaut, was bedeutet, dass wir die ganze Zeit über eingebaute Funktionen verwendet haben!

Es gibt viele verschiedene built-in Funktionen, die wir in unseren Programmen verwenden können. Schauen Sie sich dieses Beispiel für die Verwendung von `len()` an, um die Länge eines Strings zu ermitteln:

```python
destination_name = "Venkatanarasimharajuvaripeta"

# built-in Funktion: len()
length_of_destination = len(destination_name)
 
# built-in Funktion: print()
print(length_of_destination)

```
Würde den Wert von length_of_destination ausgeben:
 


`28`

Hier verwenden wir insgesamt zwei built-in Funktionen: `print()` und `len()`.

Und ja, falls Sie sich wundern, das ist ein echter Bahnhof in Indien! (;

Es gibt sogar noch andere Funktionen wie `help()`, bei denen Python einen Link zur Dokumentation ausgibt und uns einige Details liefert:

```python
help("string")
```

Würde Folgendes printen (zur besseren Lesbarkeit gekürzt):

```python
NAME
    string - Eine Sammlung von String-Konstanten.
 
MODUL-REFERENZ
    https://docs.python.org/3.8/library/string
 
    Die folgende Dokumentation wird automatisch aus den Python
    Quelldateien generiert.  Sie kann unvollständig oder fehlerhaft sein oder Merkmale enthalten, die
    die als Implementierungsdetails betrachtet werden und zwischen verschiedenen Python
    Implementierungen variieren.  Im Zweifelsfall konsultieren Sie bitte die Modulreferenz an der
    oben genannten Ort.
.....
```

Aufgaben
----------

Wir haben eine Liste mit Preisen für einige Geschenkartikel erhalten:

- T-shirt: 9.75
- Shorts: 15.50
- Mug: 5.95
- Poster: 2.00

1. Erstellen Sie eine Variable mit dem Namen `max_price` und rufen Sie die eingebaute Funktion `max()` mit den Variablen der Preise auf, um den Höchstpreis zu erhalten.
Printen Sie `max_price`.

2. Erstellen Sie mit denselben Preisen eine neue Variable namens `min_price` und verwenden Sie die eingebaute Funktion `min()` mit den Preisvariablen, um den Mindestpreis zu ermitteln. 
   Printen Sie `min_price`.

3. Verwenden Sie die eingebaute Funktion `round()`, um den Preis der Variablen `tshirt_price` um eine Dezimalstelle zu runden.
Speichern Sie das Ergebnis in einer Variablen namens `rounded_price` und printen Sie das Ergebnis.
