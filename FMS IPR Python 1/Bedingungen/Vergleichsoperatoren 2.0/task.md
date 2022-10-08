Vergleichsoperatoren 2.0
===========

Bislang kennen wir zwei Vergleichsoperatoren, nämlich `=` und `!=`. Es gibt noch eine viiieeeel (na ja, vier) mehr:

- `>` größer als
- `>=` größer als oder gleich
- `<` kleiner als
- `<=` kleiner als oder gleich

Nehmen wir an, wir betreiben eine Streaming-Plattform. Nun wollen wir ein Programm schreiben, das überprüft, 
ob unsere Benutzer über 13 Jahre alt sind, wenn wir ihnen einen Film ab 13 Jahren zeigen. 
Wir könnten etwas schreiben wie:

````python
if age <= 13:
  print("Du bist leider noch zu jung!")
````

Diese Funktion vergleicht das Alter des Benutzers mit der Zahl 13. Wenn das Alter kleiner oder gleich 13 ist, 
wird eine Meldung ausgedruckt.

Aufgaben
----------
1. Erstellen Sie ein if-statement, die prüft, ob `x` und `y` gleich sind. Wenn dies der Fall ist printen Sie:

> "Die zwei Zahlen sind gleich."

2. Die FMS verlangt von ihren Schüler:innen, dass Sie einen Notenschnitt von
mindestens 4.0 erreichen, um abschliessen zu können. Schreiben Sie ein zweites if-statement,
   das überprüft, ob der Notenschnitt für einen Abschluss reicht. Wenn ja, printen Sie:
   
> "Bravo! Ihr Notenschnitt reicht für einen Abschluss."


