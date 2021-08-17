import time
import concurrent.futures

'''
    Purpose: Use concurrent.futures
'''

def do_something(seconds):
    print(f"Sleepinig {seconds} sec ...")
    time.sleep(seconds)
    return f"Done sleepinig ...{seconds}"

if __name__ == "__main__":
    start = time.perf_counter()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        secs = [5, 4, 3, 2, 1]
        results = [executor.submit(do_something, sec) for sec in secs]
        
        for f in concurrent.futures.as_completed(results):
            print(f.result())

    finish = time.perf_counter()
    print(f"Finished in {round(finish - start, 2)} second(s)")
