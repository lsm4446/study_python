import collections

num_firends = [100,40,30,54,25,3,100,100,100,3,3]
friend_counts = collections.Counter(num_firends)
print('friends:', friend_counts)


#-*- coding: utf-8 -*-

import collections
import matplotlib.pyplot as plt

num_firends = [100,40,30,30,30,30,30,30,30,30,54,54,54,54,54,54,54,54,25,3,100,100,100,3,3]
friend_counts = collections.Counter(num_firends)
print('friends:', friend_counts)

# 가시화 추가

xs = range(101)
ys = [friend_counts[x] for x in xs] # 파이썬에는 이렇게 List구축을 할 수 있습니다. list comprehension 라고 말합니다.

plt.bar(xs,ys)
plt.axis([0,101,0,25])
plt.xlabel("# of friends")
plt.ylabel("# of people")
plt.show()


num_firends = [100,40,30,30,30,30,30,30,30,30,54,54,54,54,54,54,54,54,25,3,100,100,100,3,3]
num_points = len(num_firends)
print num_points # 25

max_value = max(num_firends)
print max_value # 100
min_value = min(num_firends)
print min_value # 3
