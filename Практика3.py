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
