n = int(input())
s = input()

positions = [i for i in range(n) if s[i] == '1']

l = positions[0] + 1
r = positions[1] + 1


length = r - l + 1


if length % 2 == 0:
    print(l, r)
else:
    r = positions[2] + 1
    print(l, r)


