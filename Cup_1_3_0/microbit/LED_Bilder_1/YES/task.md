# YES, das erste LED Bild

Eine der grossen Stärken von Python besteht darin, Pythonfunktionalität mithilfe von Modulen nachzurüsten.
Während der Kursinstallation wurde im Hintergrund das Modul [microbit-wings](https://pypi.org/project/microbit-wings/)
installiert. Mithilfe dieses Moduls und der dazugehörigen Firmware im Microbit kann eine Kommunikation zwischen
dem PC / Mac und dem Microbit erstellt werden.
Damit auf die Funktionalität des [microbit-wings](https://pypi.org/project/microbit-wings/) Moduls im Code zugegriffen
werden kann, ist am Anfang des Pythonskriptes der Modulimport `from microbit_wings import *` notwendig. 

Nachdem das Modul [microbit-wings](https://pypi.org/project/microbit-wings/) in Python importiert worden ist,
kann die Kommunikationsschnittstelle (UART) zum Microbit geöffnet werden. Dies erfolgt
 mit dem Befehl `microbit.open()`.  

<img src="img/yes_nsd.png" width="40%">

Mit dem Kommandoaufruf `microbit.leds_update(....)` erfolgt anschliessend die Übertragung und Aktualisierung
der 25 LEDs auf dem Microbit.

Am Ende des Programmes ist der Kommunikationskanal zu schliessen mit dem Befehl `microbit.close()`

<img src="img/yes.png" width="50%">

Hinweis 1: Das [Cheatsheet ToDo](ToDo) zeigt in kompakter Form eine Übersicht der integrierten Bilder.

Hinweis 2: In PyCharm ist es nicht notwendig sämtliche Befehle auszuschreiben. Mit der Tastenkombination  
Win: CTRL + SPACE (Leertaste)  
Mac: CONTROL + SPACE (Leertaste)  
wird ein Auswahlpopup mit den verfügbaren Befehlen und Variablen geöffnet.
