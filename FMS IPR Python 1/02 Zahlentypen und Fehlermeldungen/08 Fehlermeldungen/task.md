# Fehlermeldungen


Menschen neigen dazu, Fehler zu machen. Beim Programmieren werden Sie merken, dass dies sogar ziemlich oft der Fall ist.
 Glücklicherweise versuchen Programmiersprachen, die in ihren Programmen gemachten Fehler zu verstehen und zu erklären.
  

 Python bezeichnet diese Fehler als **errors** und verweist mit einem `^`-Zeichen auf die Stelle, an
 der ein Fehler aufgetreten ist. Wenn Programme Fehler auslösen, die wir nicht erwartet haben, nennen wir diese Fehler
 **Bugs**. Programmierer bezeichnen das Fehlerbeheben in einem Programm deshalb auch als **debuggen**.
  

 Zwei häufige Fehler, die beim Programmieren mit Python auftreten, sind `SyntaxError` und `NameError`.
- `SyntaxError` bedeutet, dass etwas mit der Art und Weise, wie Ihr Programm geschrieben ist, nicht stimmt - Satzzeichen,
 die nicht dazugehören, ein Befehl, der nicht erwartet wird, oder eine fehlende Klammer können einen SyntaxError auslösen.
   

Ein Syntaxfehler kann zum Beispiel auftreten, wenn Sie einen String mit doppelten Anführungszeichen beginnen und mit
 einem einfachen Anführungszeichen beenden.

  

- Ein `NameError` tritt auf, wenn der Python-Interpreter ein Wort sieht, das er nicht kennt. Code, der etwas enthält, das
 wie eine Variable aussieht, aber nie definiert wurde, löst einen `NameError` aus.
   

 Ein `NameError` kann auftreten, wenn Sie versuchen, einen String zu printen, aber keine Anführungszeichen
 um den String setzen. Python denkt dann, dass der String eine Variable ist und versucht herauszufinden, wo diese definiert wurde.
Da es aber keine Variable ist, wird keine Definition gefunden und der `NameError` tritt auf.




## Aufgabe


Lassen Sie das Programm laufen, lesen Sie die angezeigte Fehlermeldung und korrigieren Sie anschliessend die Fehler.
