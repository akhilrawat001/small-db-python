import random
def get_entry():
    file = open('words.txt' ,'r')
    data = file.read()
    data = data.split()
    return random.sample(data,2)