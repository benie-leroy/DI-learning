"""
i = 0
while i < 100:
    i +=1
    if i % 5 == 0 and i % 3 == 0:
        print('FizzBuzz')
    if i % 3 == 0:
        print ('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)

# exercice 1
print ('hello world\n ' *4)


# exercice 2

calcul = (99^3) * 8
print (calcul)

# exercice 4
computer_brand = input('please insert the brand of your computer')
print('i have a {} computer '.format(computer_brand))



# exercice 5
name = 'benie'
age = 64
shoe_size = 42
info = ('my name is {} i am {} years old and my shoe size is {}'.format(name,age,shoe_size))
print(info)


# exercice 6
number = int(input('enter a number please'))
if number % 2 == 0:
    print('{} is and odd number'.format(number))
else: print('{} is an odd number'.format(number))

# exercice 7: what's your name?
name = input("what's your name ? ")
if name == 'benie':
    print("hello {} my twin's name let us go and take a lunch ".format(name))
else:
    print ("{} sorry but u're not my friend ".format(name) )
"""

# exercice 8: Tall Enough To Ride A Roller Coaster

height = int(input('please enter your height in inches'))
Height = height * 2.54
if Height > 145:
    print('hello, you cqn ride a roller coaster' )
else:
    print('sorry, but you cannot ride a roller coaster')











