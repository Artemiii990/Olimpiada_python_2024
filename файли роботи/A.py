n = int(input())
m = int(input())

ans = 0
for i in range(n):
    for j in range(m):
        if (i == 0 and j > 0) or (j == 0 and i > 0):
            ans += 1

print(ans)
