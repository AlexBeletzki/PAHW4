import random
import timeit
n = 15
k = 15

# Выполнение алгоритма 1
def array1(n):
    from random import random
    n = 15
    arr = [0]*n
    for i in range(n):
        arr[i] = int(random()*100)
        #print(arr[i], end = ' ')
    #print()

    mn = min(arr)
    mx = max(arr)
    imn = arr.index(mn)
    imx = arr.index(mx)
    #print(f'arr[{imn+1}] = {mn} arr[{imx+1}] = {mx}')
    arr[imn], arr[imx] = arr[imx], arr[imn]

print(timeit.timeit('array1(n)', setup='from __main__ import array1, n', number = 100000))

# Выполнение алгоритма 2
def array2(k):
    s = 10
    mn = -100
    mx = 100
    arr = [random.randint(mn, mx) for _ in range(s)]
    
    idx_min = 0
    idx_max = 0
    for i in range(len(arr)):
        if arr[i] < arr[idx_min]:
            idx_min = i
        elif arr[i] > arr[idx_max]:
            idx_max = i

    #print('arr[%d] = %d arr[%d] = %d' % (idx_min+1, arr[idx_min], idx_max+1, arr[idx_max]))
    b = arr[idx_min]
    arr[idx_min] = arr[idx_max]
    arr[idx_max] = b

print(timeit.timeit('array2(k)', setup='from __main__ import array2, k', number = 100000))
