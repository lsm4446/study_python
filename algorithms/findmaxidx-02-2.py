def find_max_idx(a):
    n = len(a)
    max_idx = 0
    for i in range(1, n):
        if a[i] > a[max_idx]:
            max_idx = i
    return max_idx

v = [23, 26, 45, 83, 64, 69, 93, 34]

print(find_max_idx(v))
