k = int(input())
list = [0] * (k * 2 + 1)
list[k + 1] = 1

for i in range(k + 2, len(list)):
    list[i] = list[i - 2] + list[i - 1]

for i in range(k, -1, -1):
    list[i] = list[i + 2] - list[i + 1]

print(list)