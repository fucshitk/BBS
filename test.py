
a = []
for i in range(10):
    a.append([])
    for j in range(10):
        a[i].append(0)
        if i == j or i+j == 9:
            a[i][j] = 1

for i in a:

    print(i)


b = [[0 for i in range(10)] for j in range(10)]
print(b)
