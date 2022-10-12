Returns
======

Bis jetzt haben unsere Funktionen `print()` verwendet, um die Ausgabe zu visualisieren. Funktionen können auch einen Wert an das Programm zurückgeben, damit dieser Wert später geändert oder verwendet werden kann. Dazu verwenden wir `return`.

Hier ist ein Beispiel für ein Programm, das eine umgerechnete Währung für einen bestimmten Ort zurückgibt, den ein Benutzer in unserer Reise-App besuchen möchte.

```python
def calculate_exchange_chf(chf, exchange_rate):
  return chf * exchange_rate
 
new_zealand_exchange = calculate_exchange_chf(100, 1.51)
 
print("Für 100 CHF erhalten Sie " + str(new_zealand_exchange) + " neuseeländische Dollar")

```

Printed folgendes:

```python
Für 100 CHF erhalten Sie 151 neuseeländische Dollar
```
Wenn wir unsere von einer Funktion zurückgegebenen Werte speichern, wie wir es mit `new_zealand_exchange` getan haben, können wir den Wert (in Form einer Variablen) im restlichen Programm wiederverwenden.

Wenn das Ergebnis einer Funktion in einer Variablen gespeichert wird, nennt man es einen `returned function value`.

Aufgaben
----------

Unsere Reiseanwendung ist sehr beliebt. Einige unserer Benutzer haben in den sozialen Medien gepostet, dass es nützlich wäre, wenn unsere Anwendung ihnen helfen könnte, ihr Budget während der Reise zu verfolgen. Wir möchten ihnen helfen, ihr Startbudget zu verfolgen und sie wissen lassen, wie viel sie nach einer Ausgabe noch übrig haben.

1. Nehmen Sie sich eine Sekunde Zeit, um den bereits vorhandenen Code zu verstehen, klicken Sie dann auf Ausführen und sehen Sie sich die Ausgabe an.
2. Erstellen Sie eine neue Funktion namens `deduct_expense()`, die zwei Parameter benötigt.
Der erste Parameter ist `budget` und der zweite Parameter `expense`.

Unsere Funktion soll das Budget abzüglich der Ausgaben, die unsere Reisenden tätigen, zurückgeben.

3. Die häufigste Ausgabe, die unsere Reisenden tätigen, ist der Kauf eines T-Shirts.
Wir erstellen eine Variable mit dem Namen `shirt_expense` und geben ihr den Wert `9 `(Währungsänderungen werden im Moment nicht berücksichtigt). Stellen Sie sicher, dass diese Variable außerhalb der Funktionen in Ihrem Skript definiert ist.

4. Da wir nun eine Ausgabe abziehen müssen, erstellen Sie eine neue Variable mit dem Namen `new_budget_after_shirt` und berechnen Sie den Wert mit `deduct_expense()`.

Übergeben Sie unsere Variable `current_budget` als erstes Argument und die Variable `shirt_expense` als zweites Argument.

5. Zum Schluss möchten wir, dass unsere Benutzer das verbleibende Budget sehen.
Rufen Sie die Funktion `print_remaining_budget()` auf und übergeben Sie `new_budget_after_shirt` als einziges Argument.
   






