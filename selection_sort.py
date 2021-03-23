import timeit

def decorator(func):
    def wrapper(*args):
        start = timeit.default_timer()
        func(*args)
        stop = timeit.default_timer()
        print('Time taken : ', stop - start, "\n")
    return wrapper

@decorator
def selection_sort_inplace(data: list) -> list:
    '''
        Repeatedly finding min element and place it on its position 
    '''

    for i in range(len(data)):
        min_index = i
        for j in range(i+1, len(data)):
            if data[min_index] > data[j]:
                min_index = j

        data[i], data[min_index] = data[min_index], data[i]
    
    print(data)

@decorator
def selection_sort_outplace(data: list) -> list:
    '''
        Repeatedly finding min element and place it on its position 
    '''

    ans = []

    while len(data) > 0:
        min_ele = min(data)
        ans.append(min_ele)

        data.remove(min_ele)
    
    print(ans)

if __name__ == '__main__':
    data = [11, 45, 9, 1, 56, 80, 78, 34, 44, 55, 98]
    selection_sort_inplace(data)
    selection_sort_outplace(data)

    '''
    OUTPUT:
        [1, 9, 11, 34, 44, 45, 55, 56, 78, 80, 98]
        Time taken :  0.0003379999999999911 

        [1, 9, 11, 34, 44, 45, 55, 56, 78, 80, 98]
        Time taken :  0.0001320000000000071
    '''
