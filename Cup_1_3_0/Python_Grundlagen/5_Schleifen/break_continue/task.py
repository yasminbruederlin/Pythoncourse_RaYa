# break
for i in range(0, 5, 1):
    if i == 3:
        break
    print(i)

print('-------')

x = 0
while x < 10:
    x = x + 1
    if x == 3:
        break
    print(x)

print('-------')

for i in range(0, 5, 1):
    if i == 3:
        continue
    print(i)

print('-------')

x = 0
while x < 10:
    x = x + 1
    if x == 3:
        continue
    print(x)

