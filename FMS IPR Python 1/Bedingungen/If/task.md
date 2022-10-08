If
=======

Das Verständnis von Booleans und booleschen Ausdrücken ist enorm wichtig. Sie sind die Bausteine von jedem Code der mit
Bedingungen arbeitet (spoiler alert: (fast) jeder Code  arbeitet mit Bedingungen ;) )

Erinnern Sie sich an das Beispiel "Aufwachen" vom Anfang dieser Lektion. Der Entscheidungsprozess von 
"Regnet es? Wenn ja, nimm einen Regenschirm mit" ist eine bedingte Aussage.

Wir versuchen es einmal etwas anderst zu formulieren:

````
Wenn es regnet, dann nimm einen Regenschirm mit.
````


Können Sie hier den booleschen Ausdruck erkennen?

Richtig, `"es regnet"` ist der boolesche Ausdruck, und diese bedingte Aussage prüft, ob er wahr ist.

Wenn `"es regnet" == True` ist, wird der Rest der bedingten Anweisung ausgeführt und Sie bringen einen Regenschirm mit.

Dies ist die Form einer bedingten Anweisung:

```
Wenn [es regnet], dann [bring einen Regenschirm mit]
```

In Python sieht es ganz ähnlich aus:

```python
if is_raining:
  print("Bring einen Regenschirm mit")
```

Sie werden feststellen, dass anstelle von "dann" ein Doppelpunkt steht, `:`. Der Doppelpunkt sagt dem Computer, dass das, 
was als Nächstes kommt, ausgeführt werden soll, wenn die Bedingung erfüllt ist.

Schauen wir uns eine weitere bedingte Anweisung an:

```python
if 2 == 4 - 2: 
  print("¯\_(ツ)_/¯ ")
 ```
Wird dieser Code etwas printen?

<div class="hint">
  Ja, denn die Bedingung der if-Anweisung, `2 == 4 - 2`, ist wahr.
</div>



Aufgaben
---------

In main.py ist ein If-statement. Das Skript wurde geschrieben, weil Naruto meinen Computer ständig unerlaubt 
   benutzt hat. Wenn `user_name` Naruto ist, sagt es ihm, dass er sich von meinem Computer 
   fernhalten soll.

1. Geben Sie einen Benutzernamen in das Feld für `user_name` ein und versuchen Sie, das Programm auszuführen.


Sh*t! Wir haben einen `SyntaxError`! Das passiert, wenn wir einen kleinen Fehler in der Syntax der bedingten Anweisung machen.

2. Lesen Sie die Fehlermeldung aufmerksam durch und versuchen Sie, den Fehler zu finden. Beheben Sie ihn dann und führen 
   Sie den Code erneut aus.

Naruto ist doch cleverer als gedacht und ist meine Sicherheitsvorkehrungen umgangen und hat sich mit dem Benutzernamen 
   seiner Kollegin Sakura, sasuke_lover, angemeldet.

3. Setzen Sie `user_name` auf sasuke_lover.

4. Erstellen Sie eine zweite if-Anweisung, damit es auch Sakuras Benutzernamen überprüft und folgendes printed

``
"Ich weiss, dass du es bist, Naruto!"
``


