n = int(input())
a = list(map(int, input().split()))

a.sort()

ans = [0] * n

mid = (n + 1) // 2

for i in range(mid):
    ans[i * 2] = a[i]

for i in range(n - mid):
    ans[i * 2 + 1] = a[mid + i]

print(" ".join(map(str, ans)))


