Motivation
======

Kommen wir noch einmal auf die App zur Reiseplanung zurück, die wir vorher besprochen haben. Die Schritte, die wir für unser Programm besprochen haben, waren:

 1. Start- und Zielort festlegen
 2. Entfernung/Route berechnen
 3. Rückgabe der besten Route an den Benutzer

Wenn wir unsere Schritte in Python-Code umwandeln würden, könnte eine sehr einfache Version, die eine Reise zwischen zwei beliebten New Yorker Touristenzielen plant, wie folgt aussehen:

```python
print("Wir legen das Empire State Building als Startpunkt und den Times Square als Ziel fest.")
 
print("Berechne die Gesamtentfernung zwischen unseren Punkten.") 
 
print("Die beste Route ist mit dem Zug und dauert etwa 10 Minuten.") 
```

Jedes Mal, wenn wir zwischen diesen beiden Punkten hin- und herfahren wollen, müssen wir diese drei prints ausführen (für den Moment können wir davon ausgehen, dass die beste Route und die Zeit gleich bleiben).

Wenn unser Programm nun 100 neue Personen hätte, die versuchen, den besten Weg zwischen dem Empire State Building und dem Times Square zu finden, müssten wir jede unserer drei Druckanweisungen 100 Mal ausführen!

Wenn Sie jetzt denken, dass Sie hier eine Schleife verwenden sollten, dann ist Ihre Intuition genau richtig! Leider werden wir nicht immer zwischen denselben zwei Orten hin- und herfahren, was bedeutet, dass eine Schleife nicht so effektiv ist, wenn wir eine Reise anpassen wollen. Wir werden dies in den nächsten Abschnitten behandeln!

Jetzt wollen wir uns erst einmal mit den Funktionen vertraut machen.

Aufgaben
----------
1. Führen Sie die vorher geschriebenen print()-Anweisungen aus, um zu sehen, was sie ausgeben.

2. Führen Sie die print-Anweisungen drei weitere Male aus.

3. Hoffentlich verstehen Sie nun etwas besser, wie ein Leben ohne Funktionen aussehen würde! `#rip#</3`

Im nächsten Abschnitt werden wir lernen, wie wir unseren Code umgestalten können, um Funktionen zur Wiederverwendung von Code zu nutzen.
