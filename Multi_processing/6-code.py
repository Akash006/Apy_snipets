import time
import concurrent.futures

'''
    Purpose: Retain the order 5 sec first then others
'''

def do_something(seconds):   
    print(f"Sleepinig {seconds} sec ...")
    time.sleep(seconds)
    return f"Done sleepinig ...{seconds}"

if __name__ == "__main__":
    start = time.perf_counter()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        secs = [5, 4, 3, 2, 1] 
        results = executor.map(do_something, secs)

        for result in results:
            print(result)
 
    finish = time.perf_counter()
    print(f"Finished in {round(finish - start, 2)} second(s)")
