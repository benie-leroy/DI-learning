'''
my_fav_numbers = {7,8}
my_fav_numbers.add(90)
my_fav_numbers.add(65)
print(my_fav_numbers)
my_fav_numbers.remove(7)
print(my_fav_numbers)
friend_fav_numbers = {1,2,3}
x = my_fav_numbers + friend_fav_numbers
print(x)


#exercice 2 Tuple

# no it's not possible to add more integers to the tuple

#exercice 3: Print A Range Of Numbers

for i in range(0,21):
    print (i)


# exercice 4: Floats
i = 1
list = []
while i<5:
    i +=0.5
    list.append(i)
print(list)

# exercice 5

basket = ["Banana", "Apples", "Oranges", "Blueberries"];
basket.pop(0)
basket.pop(2)
basket.append("kiwi")
basket.insert(0,"Apples")
basket.clear()
print(basket)

# exercice 6
x = 'benie'
name = ""
while name != x:
    name = input("please enter your name :")
'''

# exercice 7

list = [65, 64, 7, 4, 73, 87, 46, 37, 3]
for i in list:
    x = list.index(i)
    if x % 2 == 0:
        print(i)
'''
list = [65, 64, 7, 4, 73, 87, 46, 37, 3]
i = 0
while i < len(list):
    if i% 2 == 0:
        print(list(i))
'''








