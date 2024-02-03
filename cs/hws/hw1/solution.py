def find_max(L):
    m = L[0]
    for x in L:
        if (x > m):
            m = x
    return m

L = [10, 20, 4, 45, 99]
print("The largest element is:", find_max(L))
