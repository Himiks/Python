import matplotlib.pyplot as plt


x1 = [2, 4, 5]
y1 = [2, 3, 6]


plt.plot(x1,y1, color='green', linestyle='dashed', linewidth=3, marker='o', markerfacecolor='blue', markersize=12, label='Line 1')
plt.ylim(1,8)
plt.xlim(1,8)
x2 = [1, 2, 3, 4]
y2 = [1, 2, 4, 4]

plt.plot(x2, y2, label='Line 2')


plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Demo Graph - Two Lines')

plt.legend()

plt.show()