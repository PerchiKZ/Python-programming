import matplotlib.pyplot as plt
import numpy as np

def y_function(x):
    return np.where(x != 0, (np.sin(10 * x) * np.sin(3 * x)) / (x ** 2), 0)


x = np.linspace(0, 4, 1000)
y = y_function(x)

plt.plot(x, y, color='blue', linewidth=2, linestyle='-', label=r'$Y(x)=\frac{\sin(10x) \sin(3x)}{x^2}$')


plt.title("Графік функції $Y(x) = \\frac{\\sin(10x) \\sin(3x)}{x^2}$")
plt.xlabel("x")
plt.ylabel("Y(x)")
plt.axhline(0, color='gray', lw=0.5)
plt.axvline(0, color='gray', lw=0.5)
plt.legend()
plt.grid(True)
plt.show()
