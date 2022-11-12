import random


empty_list = []

def add_to_end(number):
    empty_list.append(number)

def add_to_middle(number):
    random_number = random.randint(0,len(empty_list))
    empty_list.insert(random_number, number)

def remove():
    empty_list.pop()

for _ in range(5):
    add_to_end(5)
    add_to_middle(4)
    remove()

print(empty_list)