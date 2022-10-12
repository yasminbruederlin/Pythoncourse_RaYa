# Modulo


Eine wichtiger Bestandteil von Python ist der **Modulo-Operator**. Wir verwenden ihn mit dem Zeichen `%`.
 Er gibt den Rest einer Divisionsberechnung an.

```python
# printed "3" da 23/5 = 3 mit Rest 1
print(23 % 5)

# Mit modulo können wir herausfinden, ob eine ganze 
# Zahl gerade oder ungerade ist.
# Wenn das Ergebnis 0 ist, ist die Zahl gerade.
# Wenn das Ergebnis 1 ist, ist die Zahl ungerade.
# printed 0, da 42 gerade ist
print(42 % 2)
```
  


Der Modulo-Operator ist in der Programmierung sehr nützlich. Wir brauchen ihn zum Beispiel, wenn wir eine Aktion nur jedes
 n-te Mal durchführen wollen, wenn der Code ausgeführt wird.



## Aufgabe


Sie versuchen, eine Gruppe in vier Teams aufzuteilen. 
Sie nummerieren die Personen durch und erhalten für sich die Zahl 27. 

1. Finden Sie heraus in welchem Team Sie landen und speichern Sie den Wert in `my_team`. Printen Sie das Ergebnis.

2. **Bonus:** Kann das Ergebnis einer Modulo-Operation grösser als der Teiler sein?