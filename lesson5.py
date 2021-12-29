s = 10
for i in range(1, s, 1):
    i = ' ' * ((s - i) // 1) + '*' * i
    print(i)

for i in reversed(range(1, s+1, 2)):
    i = ' ' * ((s - i) // 1) + '*' * i
    print(i)