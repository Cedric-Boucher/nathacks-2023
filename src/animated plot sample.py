import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy

fig = plt.figure()
subplot = fig.add_subplot(1,1,1)
x = numpy.array([])
y = numpy.array([])

def animate(i, x1, y1, z, w):
    global x
    global y
    print(x1, y1, z, w)
    new_x = numpy.arange(i, i+1)
    new_y = numpy.random.random(1)
    x = numpy.append(x, new_x)
    y = numpy.append(y, new_y)
    subplot.clear()
    subplot.plot(x, y)

ani = animation.FuncAnimation(fig, animate, fargs = (1, 2, 3, 4), interval=100)
plt.show()
