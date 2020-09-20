import numpy as np
import matplotlib.pyplot as plt
y = lambda x: np.sin(x)/x
fig = plt.subplots()
x=np.linspace(-50,50,100)
plt.plot(x,y(x))
plt.title("график синусоиды, делённой на x", fontsize=15)
plt.xlabel("значение аргумента", fontsize=10)
plt.ylabel("значение функции", fontsize=10)
plt.show()