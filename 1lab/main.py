from random import randint

path = "c://"
def get_rand():
    return [randint(0,5) for _ in range(5)]

l = []

l = get_rand()
l = get_rand()
l = get_rand()
l = get_rand()
l = get_rand()
l = get_rand()

print(l)