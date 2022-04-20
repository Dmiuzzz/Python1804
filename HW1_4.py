n = int(input("Vvedite chislo "))
max_n = 0
while n >= 1:
    if max_n < n % 10:
        max_n = n % 10
    n = int(n / 10)
print(max_n)
