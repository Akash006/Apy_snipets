import time
import concurrent.futures

'''
    Purpose: Use concurrent.futures
'''

def do_something(seconds):
    print(f"Sleepinig {seconds} sec ...")
    time.sleep(seconds)
    return "Done sleepinig ..."

if __name__ == "__main__":
    start = time.perf_counter()
    
    # do_something()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        f1 = executor.submit(do_something, 1)
        print(f1.result())

    finish = time.perf_counter()
    print(f"Finished in {round(finish - start, 2)} second(s)")
