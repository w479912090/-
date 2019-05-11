def binary(s1, data):
    min = 0
    max = len(s1) - 1
    mid = 0
    while min <= max:
        mid = min + ((max - min) >> 1)
        if s1[mid] > data:
            max = mid - 1
        elif s1[mid] < data:
            min = mid + 1
        else:
            return mid
    return -1

print(binary([1,2,4,6,10,12,15,16,78,453,2322], 10))