# Tuples
tuple_sequence_1 = (1, 2, 3)
print(tuple_sequence_1)

tuple_sequence_2 = (1, 3.141, 'abc')
print(tuple_sequence_2)

tuple_sequence_2_len = len(tuple_sequence_2)
print(tuple_sequence_2_len)

print('------')

# Indexierung
tuple_sequence_3 = ('eins', 'zwei', 'drei')
print(tuple_sequence_3[0])
print(tuple_sequence_3[1])
print(tuple_sequence_3[2])
# print(tuple_sequence_3[3])  # erzeugt einen IndexError!

print('------')

# Aufruf der einzelnen Elemente mit Hilfe einer for Schleife
for item in tuple_sequence_3:
    print(item)
