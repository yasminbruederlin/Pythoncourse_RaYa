from microbit_wings import *  # importiere die benötigten Bibliotheken

print('verfügbare Ports auf diesem Rechner:')
print(get_serial_ports())  # zeige die verfügbaren Ports

# =======================================================================================
microbit.config.write_uart_port('COM10')  # schreibe den Standarport in die Konfiguration
# =======================================================================================

print('Standardport für den Zugriff auf den Microbit:')
microbit.config.read()  # lese die Konfigurationseinstellungen
print(microbit.config.uart_port)  # zeige den gespeicherten Standardport
