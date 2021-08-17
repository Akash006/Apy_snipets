import time
import multiprocessing

'''
    Purpose: Use arguments in functions
'''

def do_something(seconds):
    print(f"Sleepinig {seconds} sec ...")
    time.sleep(seconds)
    print("Done sleepinig ...")

if __name__ == "__main__":
    start = time.perf_counter()
    
    # do_something()

    processes = list()
    for _ in range(10):
        # arg should be tickle compatible
        p = multiprocessing.Process(target=do_something, args=[1.5])
        p.start()
        processes.append(p)

    for process in processes:
        process.join()

    finish = time.perf_counter()
    print(f"Finished in {round(finish - start, 2)} second(s)")
