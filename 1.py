a = [i for i in range(1, 20)]
print(sum(i for i in a if a.index(i) % 2 != 0))
