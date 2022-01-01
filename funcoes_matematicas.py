# POTENCIAÇÃO

print(5 ** 6)
print(pow(6, 2))

import math

print(math.pow(5, 2))

import numpy as np

print(np.power(8, 2))

import time

start = time.process_time()
val = 1000 ** 99999
print('** demora', time.process_time() - start, 'ms')

start = time.process_time()
val = pow(10000, 99999)
print('pow() demora', time.process_time() - start, 'ms')

start = time.process_time()
val = np.power(10000, 99999)
print('np.power() demora', time.process_time() - start, 'ms')

start = time.process_time()
val = math.pow(10000, 99999)
print('math.pow() demora', time.process_time() - start, 'ms')

print(math.sqrt(9, 2)) #raiz quadrada

print(8%2) #resto da divisao


