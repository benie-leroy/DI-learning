# exercice 1 : Convert Lists Into Dictionaries
'''
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
dic = dict(zip(keys, values))
print(dic)
'''
# exercice 2: Cinemax #2

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
cost = 0
for x in family:
    if family[x] < 3:
        print(x + ' ,your ticket is free')
    elif family[x] >= 3 and family[x] < 12:
        cost = cost + 10
        print(x + ', your ticket is $10')
    elif family[x] >= 12:
        cost += 15
        print(x+' , your ticket is $15')
print(cost)

names = input("please enter your family's names, separate by coma: name1,name2,... : ")
age = input("please enter in order the age of those persons, also separate by comma : ")
names = names.split(',')
age = age.split(',')
print(names)
print(age)
fam = dict(zip(names,age))
print(fam)

# exercice 3: Zara
brand = {"creation_date": 1975, }


