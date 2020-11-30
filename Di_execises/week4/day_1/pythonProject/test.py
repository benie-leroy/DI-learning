a = 3
b =4
c = a + b
print(c)

name = input('entrer votre nom svp : ')
age = input('entrer votre age svp : ')
print('votre nom est {} et votre age est {}'.format(name,age))
age = int(age)
if age > 90:
    print('bonjour le vieux')
elif age < 2:
    print('bonjour bb')
else:
    print ('bonjour le jeune')

