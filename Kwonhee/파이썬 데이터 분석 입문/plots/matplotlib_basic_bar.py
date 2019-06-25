#!/usr/bin/env python3
import matplotlib.pyplot as plt
plt.style.use('ggplot')

customers = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO']
customers_index = range(len(customers))
print(customers_index)
sale_amounts = [127, 90, 201, 111, 232]

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1) # ax1이 1행 1열 1개의 하위 그래프(유일한 하위 그래프)
ax1.bar(customers_index, sale_amounts, align='center', color='darkblue')
ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')
plt.xticks(customers_index, customers, rotation=0, fontsize='small')

plt.xlabel('Customer Name')
plt.ylabel('Sale Amount')
plt.title('Sale Amount per Customer')

plt.savefig('D:/OneDrive/Github/study_python/Kwonhee/파이썬 데이터 분석 입문/plots/bar_plot.png', dpi=400, bbox_inches='tight')
plt.show()
