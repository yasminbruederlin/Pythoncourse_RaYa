Verändern von Listen
=================

Kehren wir zu unserem Garten zurück.

```python
garden = ["Tomaten", "Grüne Bohnen", "Blumenkohl", "Trauben"]
```

Leider haben wir vergessen, unseren Blumenkohl zu gießen. 

Zum Glück kam unser Freund Krillin von Petal Power zur Rettung. Krillin hat uns ein paar Erdbeersamen geschenkt. Wir 
werden den Blumenkohl durch unsere neuen Erdbeersamen ersetzen.

Wir müssen die Liste anpassen, um die Änderung in unserer Gartenliste zu berücksichtigen. Um einen Wert in einer Liste 
zu ändern, weisen Sie den Wert mithilfe des spezifischen Index neu zu.

```python
garten[2] = "Erdbeeren"

print(garten)
```

Printed folgendes:

```python
["Tomaten", "Grüne Bohnen", "Erdbeeren", "Trauben"]
```

Aufgaben
------------

Wir haben beschlossen, einige unserer Dinge zu verkaufen. Es hat sich in unserer Stadt herumgesprochen, und die Leute 
   sind daran interessiert, etwas von unserem köstlichen Gemüse und Obst zu bekommen.

Um sicherzustellen, dass wir an alle unsere neuen Kunden verkaufen können, möchten wir eine Warteliste erstellen!

1. Definieren Sie eine Liste namens `garden_waitlist`. Die Liste soll die Namen unserer Kunden enthalten (in der Reihenfolge): "Krillin", "Adam", "Sonny" und "Alisha".

"Adam" hat beschlossen, dass sein Kühlschrank im Moment zu voll ist, und hat uns gebeten, ihn von der Warteliste zu streichen und Platz für einen unserer anderen Stadtbewohner zu schaffen.

2. Ersetzen Sie "Adam" durch unseren anderen interessierten Kunden "Calla".

Alisha stellte fest, dass sie bereits mit allen Artikeln, die wir verkaufen, eingedeckt war. Sie bittet uns, sie durch ihre Freundin Alex zu ersetzen, der gerade die Artikel ausgegangen sind.

3. Ersetzen Sie "Alisha" durch "Alex", indem Sie einen negativen Index verwenden und printen Sie die Liste.
