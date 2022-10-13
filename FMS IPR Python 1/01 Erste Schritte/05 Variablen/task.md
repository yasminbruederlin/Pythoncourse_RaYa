# Variablen
Programmiersprachen bieten Ihnen die Möglichkeit Daten zu speichern, damit Sie diese später wiederverwenden können.
 Wenn Sie sich also beispielsweise ein Datum, ein Name oder eine Benutzer-ID merken müssen, können Sie einfach eine
 Variable erstellen, die diesen Wert speichert. In Python weisen wir Variablen mit dem Gleichheitszeichen
 `(=)` zu.

`nachricht = "Hallihallo"`

In obigen Beispiel wurde die Nachricht `"Hallihallo"` in einer Variable mit dem Namen
 `nachricht` gespeichert. Variablen dürfen außer einem Unterstrich (`_`) keine Leerzeichen oder Symbole in
 ihrem Namen enthalten. Sie dürfen ausserdem nicht mit Zahlen beginnen, aber sie können Zahlen nach dem ersten
 Buchstaben haben (z. B. `coole_variable_1337`).

Welche der folgenden Variablen tragen valide Namen? (Lösung im Hint)
- up_
- _down 
- 2big
- _2big 
- down-under

<div class="hint">
 <ul>
  <li>up_</li>
  <li>_down</li>
  <li>_2big</li>
 </ul>
</div>

Es ist kein Zufall, dass wir diese Dinge *"Variablen"* nennen. Wir können den gespeicherten Wert einer Variable
 nämlich jederzeit aktualisieren (der Wert ist also *variabel*).

````python
# Begrüssung
nachricht = "Hallihallo"
print(nachricht)

# Verabschiedung
nachricht = "Hasta la vista"
print(nachricht)
````

In diesem kleinen Programm wurde der Wert der Variable `nachricht` durch eine erneute Zuweisung verändert. ~~zuerst eine Begrüssung zugewiesen und anschliessend ausgegeben.
 Danach wurde der Wert der Variable aktualisiert und erneut ausgegeben.~~

<span style="color:turquoise;font-weight:700;font-size:25px">
Aufgabe
</span>

Aktualisieren Sie die Variable `essen`, um die verschiedenen Mahlzeiten des Tages auszugeben.
Diese Aufgabe wird nicht überprüft.
