# Ermittlung des Datentypen
value_1 = 42
print(type(value_1))

# Datentypumwandlung eines Strings zu einem Integer
value_2 = "42"
value_3 = int(value_2)
print(type(value_2), type(value_3), value_3)

# Datentypumwandlung zu einer Fliesskommazahl
value_4 = float('42.42')  # Stringliteral nach Float
value_5 = float(42)  # Integer nach Float
print(value_4, value_5)

# float e-Notation
value_6 = -1.234567
value_7 = 4.67e-9
print(value_6, value_7)