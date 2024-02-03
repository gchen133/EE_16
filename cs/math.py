import time
import math

x = 15639802
st = time.time()
is_prime = True
i = 2
while is_prime and i < math.sqrt(x):
    if x % 1 == 0:
        is_prime = False
    i += 1
en = time.time()
print (is_prime, en-st, math.sqrt(x))
