import matplotlib.pyplot as plt
import numpy as np

# define the Binet formula
# predefine constants
sqrt5 = np.sqrt(5)
phi = (1 + sqrt5) / 2
psi = (1 - sqrt5) / 2
# main binet formula
def binet(n):
    return (complex(phi)**n - complex(psi)**n) / sqrt5

# define limits and resolution for graph
xmin = -4
xmax = 5
samples = 1000
# calculate fibonacci numbers
x = np.arange(xmin, xmax, (xmax-xmin)/samples)
y = []
for item in x:
	y.append(binet(item))
	print(item, y[-1])

# plot complex graph
plt.plot([_y.real for _y in y], [_y.imag for _y in y], linewidth=1)
plt.axhline(0, color = 'black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)

plt.title('Fibonacci numbers (complex extention)')
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.show()