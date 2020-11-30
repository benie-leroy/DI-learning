birthday = input('enter your birthday please dd/mm/yyyy : ')
val = birthday.split("/")
year = int(val[2])
age = 2020 - year
age = str(age)
i = int(age[1])
candle = ''
if i > 0:
    candle = print('i' * i)
    print('     ___{}___'.format(candle))
    print('    | :H:a:p:p:y: |')
    print(' ___|_____________|___')
    print('|^^^^^^^^^^^^^^^^^^^^^|')
    print('|                     |')
    print('|   :B:i:r:t:h:d:a:y: |')
    print('|                     |')
    print('|                     |')
    print('~~~~~~~~~~~~~~~~~~~~~~~')
elif i == 0:
    candle = print('i' * 2)
    print('     ___{}___'.format(candle))
    print('    | :H:a:p:p:y: |')
    print(' ___|_____________|___')
    print('|^^^^^^^^^^^^^^^^^^^^^|')
    print('|                     |')
    print('|   :B:i:r:t:h:d:a:y: |')
    print('|                     |')
    print('|                     |')
    print('~~~~~~~~~~~~~~~~~~~~~~~')


