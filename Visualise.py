import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    A = -1
    B = -1
    C = 0

    x = np.linspace(0, 32, 32)
    y = (C - A * x) / B

    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Linear Equation Plot')
    plt.grid(True)
    plt.show()


    # start:    A = 0.00901624      B = 0.00086087              C = 0.12326962231228267
    # end:      A = 496.00901624    B = 1041.60086087           C = 99.32326962231092
