import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy

fig = plt.figure()
subplot = fig.add_subplot(1,1,1)
x = numpy.array([])
y = numpy.array([])

def animate(i):
    global x
    global y
    new_x = numpy.arange(i, i+1)
    new_y = numpy.random.random(1)
    x = numpy.append(x, new_x)
    y = numpy.append(y, new_y)
    subplot.clear()
    subplot.plot(x, y)

ani = animation.FuncAnimation(fig, animate, interval=100)
plt.show()
