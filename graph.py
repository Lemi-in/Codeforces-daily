import numpy as np
import matplotlib.pyplot as plt

# Budget line: 12A + 6B = 400
A = np.linspace(0, 35, 400)
B = (400 - 12*A) / 6

# Indifference curve: U = A^0.6 * B^0.4
def indifference_curve(A, U):
    return (U / A**0.6)**(1/0.4)

U = 14.89
B_utility = indifference_curve(A, U)

plt.figure(figsize=(10, 6))
plt.plot(A, B, label='Budget Line: 12A + 6B = 400')
plt.plot(A, B_utility, label=f'Indifference Curve: U = {U:.2f}', linestyle='--')
plt.scatter(17.32, 20, color='red', zorder=5)
plt.text(17.32, 20, 'Equilibrium (17.32, 20)', fontsize=9, verticalalignment='bottom')

plt.xlabel('Apples (A)')
plt.ylabel('Bananas (B)')
plt.title('Consumer Choice: Budget Line and Indifference Curve')
plt.legend()
plt.grid(True)
plt.show()
