# break und continue

# break
Das `break` Schlüsselwort beendet eine `for` oder `while` Schlaufe.
```python
for i in range(0, 5, 1):
    if i == 3:
        break
    print(i)
```
bzw. mit `while`
```python
x = 0
while x < 10:
    x = x + 1
    if x == 3:
        break
    print(x)
```

# continue
Das `continue` Schlüsselwort unterbricht eine `for` oder `while` Schlaufe und fährt mit der
nächsten Iteration fort.
```python
for i in range(0, 5, 1):
    if i == 3:
        continue
    print(i)
```
bzw. mit `while`
```python
x = 0
while x < 10:
    x = x + 1
    if x == 3:
        continue
    print(x)
```
