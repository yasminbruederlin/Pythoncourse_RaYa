# Listen
colors = ['rot', 'blau', 'grün']
print(colors)

# hinzufügen von Elementen
colors.append('weiss')
print(colors)

# löschen von Elementen
colors.pop()  # Entfernung des letzten Elementes
print(colors)

colors.pop(0)  # Entfernung des Elementes mit dem Index 0
print(colors)

# hinzufügen von mehreren Elementen
colors = colors + ['weiss', 'türkis', 'violett']
print(colors)

print('------')

print(colors[0])  # erstes Element
print(colors[-1])  # letztes Element
print(colors[:3])  # die ersten drei Elemente
print(colors[-3:])  # die letzten drei Elemente
print(colors[1:4])  # das 1. bis zum 3. Element

print('------')

# überschreiben von bestehenden Einträgen
print(colors[1])
colors[1] = 'schwarz'
print(colors[1])
