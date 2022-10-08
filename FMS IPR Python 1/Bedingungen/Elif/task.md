Elif
==========

Wir haben if-statements gesehen und wir haben else-statements gesehen. Als letzes werden wir uns nun **elif**-statements anschauen.
Ein elif-statement ist genau das, wonach es klingt: "else if". Ein elif-statement prüft eine andere Bedingung, nachdem die Bedingungen der vorherigen if-statements nicht erfüllt wurden.
Mit elif-statements können wir steuern, in welcher Reihenfolge unser Programm die einzelnen bedingten Anweisungen prüfen soll. 
Zuerst wird das if-statement geprüft. Danach wird jedes elif-statement von oben nach unten geprüft. Falls keines der if- und elif-statements wahr war, wird schließlich der else-Code ausgeführt.

Schauen wir uns dies einmal an einem Beispiel an. Das folgende if-statement zeigt eine Dankesnachricht an, nachdem jemand 
für eine Wohltätigkeitsorganisation gespendet hat. Die Nachricht ist abhängig von der Höhe der Spende.

```python
print("Vielen Dank für die Spende!")
 
if donation >= 1000:
    print("Sie haben den Status eines Platin-Spenders erreicht.")
elif donation >= 500:
    print("Sie haben den Status eines Gold-Spenders erreicht.")
elif donation >= 100:
    print("Sie haben den Status eines Silber-Spenders erreicht.")
else:
    print("Sie haben den Status eines Bronze-Spenders erreicht.")
```

Was würde passieren, wenn alle elif-statements einfach if-statements wären? 
Wenn wir 1100,00 CHF gespendet hätten, würden die ersten drei Meldungen alle gedruckt, da jedes if-statement wahr wäre.
Da wir aber elif-statements verwendet haben, wird jede Bedingung nacheinander geprüft und nur eine Meldung gedruckt. 
Wenn wir 600,00 CHF spenden, prüft der Code zuerst, ob der Betrag über 1000 CHF liegt. Da dies nicht der Fall ist, prüft er, ob er über 500 CHF liegt.
Da dies wahr ist, printed er die entsprechende Meldung. Da alle anderen statements elif- und else-statements sind, wird 
keine von ihnen geprüft und es werden keine weiteren Meldungen geprinted.

Aufgabe
---------
1. Die FMS hat festgestellt, dass die Schüler:innen lieber Buchstaben anstatt Noten zurückbekommen.
Schreiben Sie ein if/elif/else-statement, das:
- Wenn die Note 5.5 oder höher ist, printe "A".
- Wenn die Note 5 oder höher ist, printe "B".
- Wenn die Note 4.5 oder höher ist, printe "C".
- Wenn die Note 4.0 oder höher ist, wird "D" geprinted.
- Sonst wird "F" geprinted.

