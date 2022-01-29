import matplotlib.pyplot as plt
import numpy as np
work = open('workx.txt', 'r')
e = int(input('количество итераций') or 10)
y1 = []
y2 = []
for i in range(1, e + 1):
    y1.append(i)
    y2.append(i)
y1 = np.array(y1)
y2 = np.array(y2)
x11 = []
x12 = []
x13 = []
#x14 = []
x21 = []
x22 = []
x3 = {}
x4 = {}
x23 = []
plt.style.use('seaborn-bright')
figure = plt.figure(figsize=(19, 9))
ax1 = figure.add_subplot(2, 2, 1)
ax2 = figure.add_subplot(2, 2, 2)
ax3 = figure.add_subplot(2, 2, 3)
ax4 = figure.add_subplot(2, 2, 4)
for j in work.readlines():
    i = j.split(', ')

    if i[0] == '1':
        if str(i[5]) in x4.keys():
            x4[i[5]] += 1
        else:
            x4[i[5]] = 1
    if i[0] == '2':
        if i[3] in x4.keys():
            x4[i[3]] += 1
        else:
            x4[i[3]] = 1
    if i[0] == '3':
        x11.append(int(i[2]))
        x12.append(int(i[4]))
        x13.append(int(i[6]))
        x21.append(round(float(i[3]), 1))
        x22.append(round(float(i[5]), 1))
        x23.append(round(float(i[10]), 1))
    if i[0] == '4':
        if i[3] in x3.keys():
            x3[i[3]] += 1
        else:
            x3[i[3]] = 1
    if i[0] == 5:
        pass
x3 = sorted(x3.items(), key=lambda x: int(x[0]))
x4 = sorted(x4.items(), key=lambda x: int(x[0]))
x3 = dict(x3)
x4 = dict(x4)
x11 = np.array(x11)
x12 = np.array(x12)
x13 = np.array(x13)
x23 = np.array(x23)
x21 = np.array(x21)
x22 = np.array(x22)
print(x3.keys(), x3.items(), x4.keys(), x4.items(), sep='\n')
ax1.plot(y1, x11, color='black',  linewidth=2, linestyle='-', label='Погибли')
ax1.plot(y1, x12, color='red',    linewidth=2, linestyle='-', label='выжили')
ax1.plot(y1, x13, color='green',  linewidth=2, linestyle='-', label='прибавилось')
ax2.plot(y2, x21, color='black',  linewidth=2, linestyle='-', label='Размер умерших')
ax2.plot(y2, x22, color='red',    linewidth=2, linestyle='-', label='Размер выживших')
ax2.plot(y2, x23, color='green',  linewidth=2, linestyle='-', label='Размер мутаций')
ax3.bar(x3.keys(), x3.values(), color='green')
ax4.bar(x4.keys(), x4.values(), color='black')
ax1.set_yticks(np.arange(0, 50, 5))
ax1.set_yticks(np.arange(0, 100, 10))
ax1.grid(color='pink', linewidth=1, linestyle='-.', alpha=0.3)
ax1.legend()
ax2.grid(color='pink', linewidth=1, linestyle='-.', alpha=0.3)
ax2.legend()

ax1.set_title('количество бактерий', fontsize=15)
ax1.set_xlabel('цикл')
ax1.set_ylabel('количество')
ax2.set_title('размер бактерий', fontsize=15)
ax2.set_xlabel('цикл')
ax2.set_ylabel('размер')
ax3.set_title('размножение в зависимости от размера', fontsize=10)
ax3.set_xlabel('размер')
ax3.set_ylabel('количество')
ax4.set_title('смертность в зависимости от размера', fontsize=10)
ax4.set_xlabel('размер')
ax4.set_ylabel('количество')
"""
marker='X'
marker='P' 
marker='d'
marker='^'
marker='X'
marker='P' 
marker='d'"""
plt.show()
