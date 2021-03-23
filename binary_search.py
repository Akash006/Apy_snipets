def binary_search(data: list, element, high: int, low: int):
    
    if high >= low:
        
        mid = (high + low) // 2

        if data[mid] == element:
            return mid

        if data[mid] > element:
            return binary_search(data, element, mid-1, low)
        else:
            return binary_search(data, element, high, mid + 1)
    else:
        return False

if __name__ == '__main__':
    data = [11, 45, 9, 1, 56, 80, 78, 34, 44, 55]
    # Binary search required sorted element list
    data.sort()
    ans = binary_search(data, 44, len(data)-1, 0)
    print("Binary search element present at index : ",str(ans))
