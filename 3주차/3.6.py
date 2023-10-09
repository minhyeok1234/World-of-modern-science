sum = 0
for n in range(101):
    if n % 3 == 2:
        sum = sum + n
print(sum)

sum = 0
for n in range(101):
    if n % 7 == 2:
        sum = sum + n
print(sum)

sum = 0
for n in range(1, 10001):
    if n % 7 == 2:
        if n % 3 == 0:
            sum = sum + n
print(sum)

sum = 0
for n in range(1, 10001):
    if n % 7 == 2:
        if n % 3 == 0:
            if n % 5 == 3:
                sum = sum + n
print(sum)
