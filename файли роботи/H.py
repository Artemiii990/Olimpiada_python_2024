n = int(input())
a = list(map(int, input().split()))

counts = {}
for x in a:
    counts[x] = counts.get(x, 0) + 1

replacements = 0
for i in range(n // 2):
    if a[i] != a[n - 1 - i]:
        replacements += 2

max_count = 0
for count in counts.values():
    max_count = max(max_count, count)

if max_count > n // 2:
    print(replacements)
else:
    print(replacements + (n // 2 - max_count))

