import random
def mergesort(l):
    if len(l) < 2:
        return l
    pivot = int(len(l)/2)
    l1 = l.copy()
    l2 = []
    i = 0
    while i < pivot:
        x = l1.pop()
        l2.append(x)
        i = i + 1
    l1 = mergesort(l1)
    l2 = mergesort(l2)
    while True:
        if len(l1) == len(l):
            return l1
        x = 0
        y = l2.pop()
        
        if len(l) == 2:
            if y <= l1[0]:
                l1.insert(0, y)
                return l1
            else:
                l1.append(y)
                return l1
        while x < len(l1):
            if y <= l1[x]:
                l1.insert(x, y)
                break
            x = x + 1
        else:
            l1.append(y)

l = [5, 3, 9, 15, 17, 14, 2, 12, 20, 8, 17, 7, 19, 12, 11, 14, 11, 4, 8, 20, 16, 3, 5, 1, 12, 18, 10, 12, 11, 8, 16, 5, 19, 13, 18, 17, 14, 3, 20, 8, 10, 13, 7, 10, 19, 5, 1, 18, 20, 7, 6, 14, 6, 7, 7, 20, 2, 1, 6, 2, 4, 18, 11, 18, 18, 11, 18, 7, 7, 18, 14, 7, 5, 4, 8, 14, 20, 18, 11, 11, 5, 14, 2, 2, 9, 9, 19, 14, 10, 10, 19, 18, 15, 16, 7, 6, 10, 6, 6, 8]

print(l, mergesort(l))






