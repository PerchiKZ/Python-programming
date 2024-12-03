n = 7
array = [[n - i for j in range(n)] for i in range(n)]
for row in array:
    print(*row)