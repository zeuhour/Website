import time
from django.test import TestCase

from concurrent.futures import ThreadPoolExecutor
# Create your tests here.

def test(n : int)->None:
    time.sleep(n)
    print(n)
    
with ThreadPoolExecutor(max_workers=8) as ths:

    pool = [ths.submit(test, i) for i in range(1,5)]
    time .sleep(3)
    for i in range(len(pool)):
        print(pool[i].done())