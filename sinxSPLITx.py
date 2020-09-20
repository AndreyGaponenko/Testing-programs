import numpy as np
import matplotlib.pyplot as plt
y = lambda x: np.sin(x)
fig = plt.subplots()
x=np.linspace(-6,6,100)
plt.plot(x,y(x))
plt.title("график синусоиды", fontsize=15)
plt.xlabel("значение аргумента", fontsize=10)
plt.ylabel("значение функции", fontsize=10)
plt.show()