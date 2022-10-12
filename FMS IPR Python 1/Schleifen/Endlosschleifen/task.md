Endlosschleifen
==============

Wenn wir mit while-Loops arbeiten, kommt es immer wieder vor, dass wir einen **Endlosschleife** erstellen.

Schauen wir uns doch mal das folgende Beispiel an.

```python
my_favorite_numbers = [4, 8, 15, 16, 42]
 
for number in my_favorite_numbers:
  my_favorite_numbers.append(1)
```

Was passiert in diesem Beispiel? Für die Lösung können Sie auf `Hint` klicken.

<div class="hint">
Jedes Mal, wenn wir den Loop ausführen, fügen wir eine 1 an das Ende der Liste an. Das Ergebnis ist, dass wir nie am 
Ende der Liste ankommen, da sie immer weiter wächst!
</div>

Ein Loop, der niemals endet, nennt man eine Endlosschleife (engl. infinite loop). Diese Loops sind für unseren Code sehr 
gefährlich, da sie unser Programm ewig laufen lassen und somit alle Ressourcen des Computers verbrauchen.

Ein Programm, das in eine Endlosschleife gerät, wird oft völlig unbrauchbar. 

Hinweis: Wenn Sie in eine Endlosschleife geraten, können Sie die Schleife beenden, indem Sie die Tastenkombination Strg + c verwenden, um das Programm zu beenden. 

Aufgabe
-----------

Angenommen, wir haben zwei Listen mit Schülern, `students_A` und `students_B`. Wir möchten alle Schüler:innen in 
`students_B` zusammenfassen.

1. Kommentieren Sie die Zeile 7 aus. Bevor Sie den Code ausführen, sollten Sie überlegen, warum dieser Code eine Endlosschleife verursacht.

2. Führen Sie den Code aus.

Hilfe - wir haben eine Endlosschleife! 

3. Beenden Sie das Programm.

4. Löschen Sie die Zeile, welche die Endlosschleife verursacht und korrigieren Sie das Programm so, dass das am Ende aller 
Schüler:innen in der Liste `students_B` enthalten sind.


This is a task description file.
Its content will be displayed to a learner
in the **Task Description** window.

It supports both Markdown and HTML.
To toggle the format, you can rename **task.md**
to **task.html**, or vice versa.
The default task description format can be changed
in **Preferences | Tools | Education**,
but this will not affect any existing task description files.

The following features are available in
**task.md/task.html** which are specific to the EduTools plugin:

- Hints can be added anywhere in the task text.
Type "hint" and press Tab.
Hints should be added to an empty line in the task text.
In hints you can use both HTML and Markdown.
<div class="hint">

Text of your hint

</div>

- You may need to refer your learners to a particular lesson,
task, or file. To achieve this, you can use the in-course links.
Specify the path using the `[link_text](course://lesson1/task1/file1)` format.

- You can insert shortcuts in the task description.
While **task.html/task.md** is open, right-click anywhere
on the **Editor** tab and choose the **Insert shortcut** option
from the context menu.
For example: &shortcut:FileStructurePopup;.

- Insert the &percnt;`IDE_NAME`&percnt; macro,
which will be replaced by the actual IDE name.
For example, **%IDE_NAME%**.

- Insert PSI elements, by using links like
`[element_description](psi_element://link.to.element)`.
To get such a link, right-click the class or method
and select **Copy Reference**.
Then press &shortcut:EditorPaste; to insert the link where appropriate.
For example, a [link to the "contains" method](psi_element://java.lang.String#contains).

- You can add link to file using **full path** like this:
  `[file_link](file://lesson1/task1/file.txt)`.