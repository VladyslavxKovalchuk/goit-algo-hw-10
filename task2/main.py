import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа

# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()

def monte_carlo_integration(a, b,num_experiments, y_max):
    x_random = np.random.uniform(a, b, num_experiments)
    y_random = np.random.uniform(0, y_max, num_experiments)
    under_curve = y_random < f(x_random)
    return (b - a) * y_max * np.mean(under_curve)

y_max = f(b)
num_experiments = 100000
estimate_area = monte_carlo_integration(a, b, num_experiments, y_max)
print(f"Оцінка площі методом Монте-Карло: {estimate_area:.4f}")

result, error = spi.quad(f, a, b)
print(f"Аналітичне значення інтегралу: {result:.4f}")