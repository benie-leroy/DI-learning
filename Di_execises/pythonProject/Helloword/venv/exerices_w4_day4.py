'''
# Exercise 1 : What Are You Learning ?
def display_message():
    print('hello everyone, in this chapter, we have learn how to use fonctions in python')


display_message()


# Exercise 2: What’s Your Favorite Book ?

def favorite_book(title):
    print("One of my favorite book is {}".format(title))


favorite_book('the little red chaperone')


# Exercise 3 : Some Geography
def describe_city(city_name, country='Cameroun'):
    print('{} is in {}.'.format(city_name, country))


describe_city('Abidjan', "Cote d'ivoire")
describe_city('Yaounde')
describe_city('Dschang')


# Exercise 4 : Let’s Create Some Personalized Shirts !

def make_shirt(size='large', text='i love python'):
    print("this shirt is size {} and it's {}".format(size, text))


make_shirt('16', 'the first of our new collection')
make_shirt(size='19', text='our greater size')
make_shirt('large')
make_shirt('medium')
make_shirt('s', 'the biggest one')

# Exercise 5 : Magicians …

magician_names = ['Neil', 'Lens', 'Herve', 'Paul']


def show_magicians():
    for i in magician_names:
        print(i)


show_magicians()


def make_great(name):
    return "the great {}".format(name)


map_list = list(map(make_great, magician_names))
print(map_list)

new_magicians = make_great(magician_names)


# Exercise 6: When Will I Retire?

def get_age(year, month, day):
    current_year = 2020
    current_month = "november"
    imp = input("please enter your birthday 'year,month,day' : ")
    s_imp = imp.split(",")
    b_year = int(s_imp[0])
    age = current_year - b_year
    return age
get_age(1990, 8, 0)

'''
def get_age(year, month, day):
    current_year = 2020
    current_month = 'November'
    year = int(year)
    age = current_year - year
    print(age)
get_age(1900, 8, 3)






