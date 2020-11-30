# question 1
import random
string = input('please enter a string :')
str = len(string)
if str < 10:
    print('string is not long enough')
else:
    print('string to long')
# question 2
print(string[0:str:str-1])
# question 3
i = 0
while i < len(string)+1:
    i +=1
    print(string[0:i-1])
string = list(string)
random.shuffle(string)
string = "".join(string)
print(string)
print("".join(random.sample(string, len(string)))