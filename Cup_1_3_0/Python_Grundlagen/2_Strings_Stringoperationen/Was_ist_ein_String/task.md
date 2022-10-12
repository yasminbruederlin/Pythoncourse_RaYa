# Was ist ein String?

Strings (oder Zeichenketten) gehören zu den elementaren Datentypen in Python.
Datentypen bilden unterschiedliche Eigenschaften von Variablen ab. 
Der Stringdatentyp repräsentiert Zeichen und Zeichenketten.

## Eigenschaften von Strings
Strings erfüllen drei wichtige Eigenschaften:

1. Strings enthalten einzelne Buchstaben oder Zeichen. Diese Einzelzeichen werden als
   Charakter (character) bezeichnet.

2. Strings weisen eine definierte Länge auf. 
  
3. Strings erscheinen als Sequenz von Charaktern. Somit ist die Position des Charakters
   im String definiert.
   
Hinweis: In den folgenden Kapiteln werden weitere Datentypen besprochen.

## Zeichenketten (string literals)
Zeichenketten werden in Python gebildet durch Einbettung des Strings in
einfache oder doppelte Hockhommas.
```python
str_value_1 = 'einfache Hochkommas'
str_value_2 = "doppelte Hochkommas"
```
Die Verwendung von einfachen oder doppelten Hochkommas kann gleichwertig
betrachtet werden.

Wird ein String mit Hochkommas am Anfang und am Ende versehen, wird dieser
String zur Zeichenkette (string literal).

### Sonderzeichen in Zeichenketten
Sonderzeichen (wie `"\' ` ...) sind in Python mittels Escapenotation 
zu integrieren. Dabei wird vor dem jeweiligen Sonderzeichen ein Backslash
eingefügt.

### Mehrzeilige Strings
Die PEP 8 Stilrichtlinie von Python beschreibt zwei Möglichkeiten Zeichenketten
auf mehrere Zeilen aufzuteilen:

1. Durch Einfügen von drei Hochkommas `""" string """"` bzw. `''' string ''''`
2. Trennung des Ausdrucks mittel Backslash `\`