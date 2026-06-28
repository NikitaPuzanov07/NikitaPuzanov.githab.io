n = int(input("Введите количество экспериментальных точек: "))
if n < 2:
    raise ValueError("Для линейной аппроксимации нужно минимум 2 точки.")
x = []
y = []
print("Введите значения x (по одному в строке):")
for i in range(n):
    x.append(float(input(f"x[{i}] = ")))
print("Введите значения y (по одному в строке):")
for i in range(n):
    y.append(float(input(f"y[{i}] = ")))
sum_x = sum(x)
sum_y = sum(y)
sum_xy = sum(xi * yi for xi, yi in zip(x, y))
sum_x2 = sum(xi ** 2 for xi in x)
denominator = n * sum_x2 - sum_x ** 2
if denominator == 0:
    raise ValueError("Невозможно построить линейную аппроксимацию: все значения x одинаковы.")
a = (n * sum_xy - sum_x * sum_y) / denominator
b = (sum_y - a * sum_x) / n
print(f"\nКоэффициент a (наклон): {a:.4f}")
print(f"Коэффициент b (сдвиг):   {b:.4f}")
print(f"Уравнение прямой: y = {a:.4f} * x + {b:.4f}")