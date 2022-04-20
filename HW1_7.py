a = int(input('Enter the result of the fist day '))
b = int(input('Enter the desired result '))
day = 1
while a < b:
    print(day, 'day: ', a)
    a *= 1.1
    day += 1
print(day, 'day: ', a)
print('Answer: on the ',  day, ' day , the athlete achieved a result of at least ', b, ' km .')