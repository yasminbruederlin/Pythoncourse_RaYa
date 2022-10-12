# Boolsche Operatoren
In den vorhergehenden Kapiteln bestand der betrachtete Pythoncode aus einer
linearen Aneinanderreihung von Codezeilen. Mit Hilfe der boolschen Operatoren
besteht die Möglichkeit, den Pythoncode in Abhängigkeit von Fragestellungen
gezielt zu steuern.  

Das Resultat einer boolschen Operation erfolgt stehts in einer binären Form als
`True` oder `False`.

## Vergleichsoperatoren
Die Vergleichsoperatoren dienen der Umwandlung von Abfragetermen mit
einem grossen Werteraum in die zwei Zustände `True` oder `False`.
Die nachfolgenden Liste beschreibt die wichtigsten Vergleichsoperatoen welche
in Python zur Verfügung stehen:

<table>
  <tr>
    <th>Vergleichsoperator</th>
    <th>Beispiel</th>
    <th>Bedeutung</th>
  </tr>
  <tr>
    <td><</td>
    <td>a < b</td>
    <td>a ist kleiner als b</td>
  </tr>
    <td>></td>
    <td>a > b</td>
    <td>a ist grösser als b</td>
  </tr>
    <td><=</td>
    <td>a <= b</td>
    <td>a ist kleiner gleich b</td>
  </tr>
    <td>!=</td>
    <td>a != b</td>
    <td>a ist ungleich b</td>
  </tr>
    <td>==</td>
    <td>a == b</td>
    <td>a ist gleich b</td>
  </tr>
</table>

**Hinweis**:  
Ein häufiger Programmierehler besteht darin, dass bei einem Vergleich auf
Gleichheit nur ein einzelnes Gleicheitszeichen `=` eingesetzt wird. Im Gegensatz
zur mathematischen Gleichheit sind bei einem logischen Vergleich in Python zwei 
Gleichheitszeichen `==` zu verwenden.

## Logische Operatoren
Für die logische Verknüpfung von boolschen Datentypen können die logischen Operatoren
eingesetzt werden. Die drei wichtigsten lauten:
- and
- or
- not

Die dazugehörigen Wertetabellen lauten:  

---
**and** (Maximalfunktion)  
**x = a and b**
<table>
  <tr>
    <th>a</th>
    <th>b</th>
    <th>x</th>
  </tr>
  <tr>
    <td>False</td>
    <td>False</td>
    <td>False</td>
  </tr>
  <tr>
    <td>False</td>
    <td>True</td>
    <td>False</td>
  </tr>
  <tr>
    <td>True</td>
    <td>False</td>
    <td>False</td>
  </tr>
  <tr>
    <td>True</td>
    <td>True</td>
    <td>True</td>
  </tr>
</table>

---
**or** (Minimalfunktion)  
**x = a or b**
<table>
  <tr>
    <th>a</th>
    <th>b</th>
    <th>x</th>
  </tr>
  <tr>
    <td>False</td>
    <td>False</td>
    <td>False</td>
  </tr>
  <tr>
    <td>False</td>
    <td>True</td>
    <td>True</td>
  </tr>
  <tr>
    <td>True</td>
    <td>False</td>
    <td>True</td>
  </tr>
  <tr>
    <td>True</td>
    <td>True</td>
    <td>True</td>
  </tr>
</table>

---
**not** (Invertierung)  
**x = not a**
<table>
  <tr>
    <th>a</th>
    <th>x</th>
  </tr>
  <tr>
    <td>False</td>
    <td>True</td>
  </tr>
  <tr>
    <td>True</td>
    <td>False</td>
  </tr>
</table>

---
