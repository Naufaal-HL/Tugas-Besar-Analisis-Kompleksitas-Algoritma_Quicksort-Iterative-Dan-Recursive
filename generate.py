import numpy as np
import os

os.makedirs('data', exist_ok=True)
size = [1000, 2000, 3000, 4000, 5000]

def random_number():
    for n in size:
        array = list(np.random.randint(1, 5000,  n))
        name = 'rand' + str(n) + '.dat'
        np.savetxt('data/'+name, array, fmt=['%i'])

def reversed_number():
    for x in size:
        number = []

        for n in range(x, 0, -1):
            number.append(n)

        name = 'reversed' + str(x) + '.dat'
        np.savetxt('data/'+name, number, fmt=['%i'])

def equal_number():
    for x in size:
        number = []
        for _ in range(x):
            number.append(5)

        name = 'equal' + str(x) + '.dat'
        np.savetxt('data/' + name, number, fmt=['%i'])

random_number()
reversed_number()
equal_number()
