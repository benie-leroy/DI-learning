import random

def get_words_from_file():
    with open("file.txt", 'r') as f:
        l = f.readlines()
        lis = [i.replace("\n","") for i in l]
        print(lis)
        return lis
get_words_from_file()
def get_random_sentence(length):
    a = get_words_from_file()
    length =
    print(random.choice(a))
get_random_sentence(7)



