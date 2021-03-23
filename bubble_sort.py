import timeit

def bubble_sort(data: list) -> list:
    '''
        Repeatedly swaping adjecent element if they are in wrong order
    '''
    start = timeit.default_timer()

    for pre in range(1, len(data)):
        for index in range(1, len(data)):
            if data[index] < data[index - 1]:
                data[index], data[index-1] = data[index-1], data[index]

    stop = timeit.default_timer()
    print('Normal Bubble sort time : ', stop - start)
    print(data)

def modified_bubble_sort(data: list) -> list:
    '''
        Repeatedly swaping adjecent element if they are in wrong order
        and stop iteration if there is no swap 
    '''
    start = timeit.default_timer()

    for pre in range(1, len(data)):
        flag = 0
        for index in range(1, len(data)):
            if data[index] < data[index - 1]:
                data[index], data[index-1] = data[index-1], data[index]
                flag = 1

        if flag == 0:
            break

    stop = timeit.default_timer()
    print('\nModified Bubble sort time : ', stop - start)
    print(data)

if __name__ == '__main__':
    data = [11, 45, 9, 1, 56, 80, 78, 34, 44, 55]

    bubble_sort(data)
    modified_bubble_sort(data)

    '''
    OUTPUT:
        Normal Bubble sort time :  6.670000000000287e-05
        [1, 9, 11, 34, 44, 45, 55, 56, 78, 80]

        Modified Bubble sort time :  1.0700000000002374e-05
        [1, 9, 11, 34, 44, 45, 55, 56, 78, 80]
    '''
