import subprocess
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

A = [5,4,2,3,6,2,1,1]
# The threads will call this function
def sleepSort(num):
    time.sleep(num/50) # workss well for num, num/10 to num/100. But for num/100 there are a few inaccuracies. Especially if the numbers are close enough 
    return num

with ThreadPoolExecutor() as thread_executor:
    # Await all results
    await_results = [thread_executor.submit(sleepSort, num=i) for i in A]
    for f in as_completed([future for future in await_results]):
        print(f.result(),' ', end='')
