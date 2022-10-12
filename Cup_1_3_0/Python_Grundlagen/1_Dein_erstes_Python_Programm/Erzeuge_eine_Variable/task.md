# Erzeuge eine Variable
Variablen sind in Python Namen welche mit einer Wertzuweisung versehen werden. 
Auf diesen zugewiesenen Wert kann im Programmablauf zurückgegriffen werden.
Variablen sind fundamentale Elemente eines Programmes aus zwei Gründen:

1. Variablen erlauben einen Wertezugriff.  
   Nach der Zuweisung eines Ausdrucks an eine Variable, kann dieser Wert an
   einer anderen Stelle im Programm wieder verwendet werden.
   
2. Variablen assoziieren Zusammenhänge. Die Zahl `42` kann die unterschiedlichsten 
   Bedeutungen aufweisen. Durch Zuweisung der Zahl `42` an eine Variable
   `the_answer_of_all_questions = 42` wird eine Assoziotion zum Wert gebildet.
   
## Der Zuweisungsoperator
Ein Operator ist ein Symbol welche eine Operation auf einen oder mehrere Werte 
ausübt. Zum Beispiel bildet der `+` Operator die Summe zweier Zahlen. Die Zuweisung
eines Wertes an eine Variable erfolgt mithilfe des Gleichheitszeichens `=`. Dabei wird
der vom `=`-Zeichen rechts angeordnete Term dem Namen auf der linken Seiten zugewiesen.
=> siehe task.py <=

### Namenskonventionen
Variablennamen können beliebig lange oder kurz sein, allerdings gilt es bei der Namenvergabe
einige Regeln zu beachten:

- Erlaubt sind: `a-z`, `A-Z`, `0-9` und `_`
  * Grundsätzlich auch Umlaute (`ä ö ü`) bzw. Buchstaben aus nichlatinischen Sprachen wie Chinesisch, Japanisch.... 
    Diese Zeichen sollten aber vermieden werden.
- Gross- und Kleinschreibung wird unterschieden
- Ein Variablennamen darf nicht mit einer Zahl beginnen

Folgende Beispiele sind gültige Variablennamen:

- hello_world
- _nominator
- variablennahmen_bestehend_aus_mehreren_woertern_welcher_durch_underscore_getrennt_wird

Nicht zulässige Zuweisungen:
- 42_is_the_answer
- das-Haus 

Ein ausführliche Beschreibung der Namenskonvention von Python wird in der PEP 8 aufgeführt:  
https://www.python.org/dev/peps/pep-0008/#naming-conventions  
Der PEP 8 Styleguide gilt als die Referenz hinsichtlich der Strukturierung
von Pythoncode.

### Beschreibende Namen sind besser als kurze Namen
Bei komplexeren Programmstrukturen erleichtern beschreibende Namen die Lesbarkeit.  
`a = 42` versus `the_answer_of_all_questiion = 42`

---
Nachtrag:  
Die Antwort 42 ist ein Zitat aus der mehrfach verfilmten Roman- und Hörspielreihe Per Anhalter durch 
die Galaxis des englischen Autors Douglas Adams.
Im Roman ist „42“ die von einem Supercomputer nach einigen Millionen Jahren Rechenzeit gegebene Antwort 
auf die Frage "nach dem Leben, dem Universum und dem ganzen Rest" 
(englisch "life, the universe and everything"), mit der die Protagonisten letztlich nichts anfangen können, 
weil die Frage zu vage gestellt war.  
https://de.wikipedia.org/wiki/42_(Antwort)   


  