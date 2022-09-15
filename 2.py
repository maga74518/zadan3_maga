a, b = [2, 3, 4, 5, 6], []
if len(a) % 2 == 0:
    for i in range(len(a) // 2):
        b.append(a[i] * a[-1 - i])
elif len(a) % 2 != 0:
    for i in range(len(a) // 2):
        b.append(a[i] * a[-1 - i])
    b.append(a[len(a) // 2] * a[len(a) // 2])
print(b)
