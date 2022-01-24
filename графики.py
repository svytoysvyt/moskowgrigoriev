import matplotlib.pyplot as plt
import numpy as np
work = open('work.txt', 'r')
y1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
                29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54,
                55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
                81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104,
                105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120])
y2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
                29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54,
                55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
                81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104,
                105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120])
x11 = [0]
x12 = [50]
x13 = [0]
x14 = [50]
x21 = []
x22 = []
x23 = []
plt.style.use('seaborn-bright')
figure = plt.figure()
ax1 = figure.add_subplot(1, 2, 1)
ax2 = figure.add_subplot(1, 2, 2)
for j in work.readlines():
    i = j.split(', ')

    if i[0] == '1':
        pass
    if i[0] == '2':
        pass
    if i[0] == '3':
        x11.append(int(i[2]))
        x12.append(int(i[4]))
        x13.append(int(i[6]))
        x14.append(int(i[9]))
        x21.append(round(float(i[3]), 1))
        x22.append(round(float(i[5]), 1))
        x23.append(round(float(i[8]), 1))
    if i[0] == '4':
        pass
x11 = np.array(x11)
x12 = np.array(x12)
x13 = np.array(x13)
x14 = np.array(x14)
x23 = np.array(x23)
x21 = np.array(x21)
x22 = np.array(x22)
print(y1, x11, x12, x13,x14,  sep='\n')
ax1.plot(y1, x11, color='black', linewidth=2, linestyle='-', marker='X', label='Погибли')
ax1.plot(y1, x12, color='red', linewidth=2, linestyle='-', marker='P', label='выжили')
ax1.plot(y1, x13, color='green', linewidth=2, linestyle='-', marker='d', label='прибавилось')
ax1.plot(y1, x14, color='yellow', linewidth=2, linestyle='-', marker='^', label='всего бактерии')
ax2.plot(y2, x21, color='black', linewidth=2, linestyle='-', marker='X', label='Размер умерших')
ax2.plot(y2, x22, color='red', linewidth=2, linestyle='-', marker='P', label='Размер выживших')
ax2.plot(y2, x23, color='green', linewidth=2, linestyle='-', marker='d', label='Размер мутаций')
ax1.set_yticks(np.arange(1, 50, 1))
#ax1.set_yticks(np.arange(0, 100, 10))
ax1.grid(color='pink', linewidth=1, linestyle='-.', alpha=0.3)
ax1.legend(loc='lower left')
ax2.grid(color='pink', linewidth=1, linestyle='-.', alpha=0.3)
ax2.legend(loc='lower right')

plt.show()
