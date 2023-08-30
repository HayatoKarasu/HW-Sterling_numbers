from matplotlib import pyplot as plt  

plt.text(0.01, 0.9, 'Сколько слов можно получить переставляя', fontsize=15)
plt.text(0.01, 0.8, 'буквы в слове "КОЛОБОК"?', fontsize=15)
plt.text(0.01, 0.7, 'В слове 7 букв, а так же 3 буквы "о"', fontsize=15)
plt.text(0.01, 0.6, 'и 2 буквы "к". Учтем это:', fontsize=15)
form = r"$N = \frac{7!}{2!*3!} = \frac{7*6*5*4*3!}{2!*3!} = \frac{7*6*5*4}{2*1} = 7*6*5*2 =$"
plt.text(0.01, 0.4, form, fontsize=15)
plt.text(0.01, 0.2, 'Итого: = 420 слов (комбинаций)', fontsize=15)

fig = plt.gca()
fig.axes.get_xaxis().set_visible(False)
fig.axes.get_yaxis().set_visible(False)

plt.show()