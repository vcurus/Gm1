import time

print(' = "первый цикл"' * 3)
i = 0
while i < 10:
    time.sleep(0.2)
    print(i)
    i += 1
    continue
    if i > 5:
        break

print(' = "второй цикл"' * 3)
for j in range(10):
    time.sleep(0.2)
    print(j)
    continue
    if j > 5:
        break

print(' = "третий цикл"' * 3)
for s in 1, 2, 3:
    print(s)

print(' = "есле иначе"' * 3)
if i == 9:
    print('да i это 9')
if i == 10:
    print('да i это 10')
elif i != 9:
    print('что то напичатется?')
else:
    print('да i это 9')
