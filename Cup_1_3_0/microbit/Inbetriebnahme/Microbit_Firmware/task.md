# Microbit Firmware
Der Microbit ist ein kleiner Computer, welcher für den schulischen Einsatz konzipiert wurde.
Das Ziel des Microbit besteht darin, eine Verbindung zwischen einem PC / Mac (Personal Computer) und den
physikalischen Ein- und Ausgabepunkten zu erstellen. Im Rahmen des Kurses Computertechnik und Programmierung I
dient der Microbit als Ein- / Ausgabemodul für den Pythoncode, welcher auf dem PC / Mac läuft. Da es sich um einen
eingenständigen Computer handelt, benötigt der Microbit auch ein spezielles Programm, damit er mit dem PC / Mac
kommunizieren kann. Software für diese Art von Kleinstcomputer wird als Firmware bezeichnet.

<img src="img/microbit_hardware.jpg" width="100%">

Weitere Informationen sind der Website [microbit.org](https://microbit.org/) zu entnehmen.

## Systemstruktur
Der Microbit wird über USB an den PC / Mac gekoppelt. Aus der Sicht des Betriebssystems (Windows, Mac) erscheint der
Microbit als serielles Endgerät ([UART](https://de.wikipedia.org/wiki/Universal_Asynchronous_Receiver_Transmitter)).
Die serielle Kommunikation, auch UART-Kommunikation, wird insbesondere zum Datenaustausch mit
leistunsschwächeren Endgeräten eingesetzt. 

Weitere Information zur Hardware des Microbit sind den folgenden Links zu entnehmen:  
- [Microbit Hardware Spezifikation](https://tech.microbit.org/hardware/)
- [Microbit Schema](https://github.com/microbit-foundation/microbit-reference-design/blob/master/PDF/Schematic%20Print/Schematic%20Prints.PDF)  
- [Microcontroller Nordic nFRF51822](https://www.nordicsemi.com/Products/Low-power-short-range-wireless/nRF51822)  


## Programmierung der Firmware
<img src="img/connection_uart_system_bw.png" width="50%">  

Um eine Kommunikation zwischen dem PC / Mac und dem Microbit erstellen zu können, ist die Firmware (Programm des Microbit) in
den Flashspeicher zu übertragen.  

In den beiden folgenden Videos wird die Programmierung der Firmware für den micro:bit (Windows und Mac) ausführlich erläutert.

### Windows
[https://w2y.ch/2zi](https://w2y.ch/2zi)
<img src="img/vimeo_win_installation_firmware_microbit.png" width="20%">

### Mac
[https://w2y.ch/sfc](https://w2y.ch/sfc)
<img src="img/vimeo_mac_installation_firmware_microbit.png" width="20%">
