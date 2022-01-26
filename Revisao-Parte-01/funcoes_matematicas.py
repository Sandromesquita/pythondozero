import math
import numpy as np
import time

start = time.process_time()
val = 10000 ** 99999
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


