# if Abfrage
a = True
b = False

if a == True:  # kann auch vereinfacht werden!
    print('Bedingung True')

if a:
    print('Bedingung True')

if a and b:
    print('Bedingung True')
else:
    print('Bedingung False')

# elif Abfrage
grade = 5.0
if grade < 4.0:
    print('ungenügend')
elif (grade >= 4.0) and (grade < 5.0):
    print('genügend')
elif (grade >= 5.0) and (grade < 5.5):
    print('gut')
else:
    # wird aufgerufen falls keine der obigen
    # Testblöcke True sind
    print('sehr gut')
