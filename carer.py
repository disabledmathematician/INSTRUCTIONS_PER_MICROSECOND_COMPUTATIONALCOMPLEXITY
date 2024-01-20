import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

def f(x, y):
	return x ** 1/3 + y ** 1/3
	
def plot():
	plt.figure(0)
	ax = plt.axes(projection='3d')
	x, y = np.linspace(-10, 10, 200), np.linspace(-10, 10, 200)
	x, y = np.meshgrid(x, y)
	z = f(x, y)
	z **= 1/3
	ax.set_title("Charles Truscott Watters. $z = (x^{1/3}+ y^{1/3})^{1/3}$")
	ax.plot_surface(x, y, z, cmap='rainbow')
	plt.show()
plot()