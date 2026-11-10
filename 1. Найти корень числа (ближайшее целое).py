def binarySearchSqrt(target):
    l = 0
    r = target
    while l <= r:
        middle = (l + r) // 2
        if middle ** 2 > target:
            r = middle - 1
            continue
        elif middle ** 2 < target:
            l = middle + 1
            continue
        else:
            return middle
    return r

'''
Алгоритм работает за O(log n), так как при поиске отрезок каждый раз уменьшается вдвое, поэтому шагов не более, чем log2(target).
'''