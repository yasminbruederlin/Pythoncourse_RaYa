# if Abfrage
if 3 + 2 > 4:
    print('3 + 2 ist grösser 4')

grade = 5.0
if grade >= 5.0:
    print('sehr gut!')

# if else Abfrage
a = 1
b = 2
if a < b:
    print('a < b => True')
else:
    print('a < b => False')

# if elif else Abfrage
grade = 5.0
if grade < 4.0:
    print('ungenügend')
elif (grade >= 4.0) and (grade < 5.0):
    print('genügend')
elif (grade >= 5.0) and (grade < 5.5):
    print('gut')
else:
    print('sehr gut')