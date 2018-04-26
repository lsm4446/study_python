def find_max(a):
    n = len(a)
    max_v = a[0]
    for i in range(1, n-1):
        if a[i] > max_v:
            max_v = a[i]
    return max_v

v = [17, 92, 18, 33, 58, 7, 33, 42, 79, 37]
print(find_max(v))
