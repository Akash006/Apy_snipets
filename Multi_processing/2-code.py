import time
import multiprocessing

'''
    Purpose: Use for loop for multiprocess
'''

def do_something():
    print("Sleepinig 1 sec ...")
    time.sleep(1)
    print("Done sleepinig ...")

if __name__ == "__main__":
    start = time.perf_counter()
    
    # do_something()

    processes = list()
    for _ in range(10):
        p = multiprocessing.Process(target=do_something)
        p.start()
        processes.append(p)

    for process in processes:
        process.join()

    finish = time.perf_counter()
    print(f"Finished in {round(finish - start, 2)} second(s)")
