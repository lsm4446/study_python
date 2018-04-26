'''
Created on 2018. 4. 26.

@author: lsm
'''
def find_max(a):
    n = len(a)
    print (n)
    max_v = a[0]
    for i in range(1, n): # for 문장은 n 미만까지 반복한다.
        print (i) 
        if a[i] > max_v:
            max_v = a[i] 
    return max_v

v = [23, 26, 45, 83, 64, 69, 93, 34]
print(find_max(v))