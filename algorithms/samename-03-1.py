'''
Created on 2018. 4. 26.

@author: lsm
'''
def find_same_name(a):
    n = len(a)
    result = set()
    for i in range(0, n-1):
        for j in range(i+1, n):
            if a[i] == a[j]:
                result.add(a[i])
    return result

name = ["이상면", "Tom", "Jerry", "Mike", "이상면", "Tom"]
print(find_same_name(name))

name = ["이상면", "Tom", "Jerry", "Mike", "이상면", "Mike"]
print(find_same_name(name))

name = ["이상면", "Tom", "Jerry", "Mike", "Mike", "Jerry", "tom"]
print(find_same_name(name))
