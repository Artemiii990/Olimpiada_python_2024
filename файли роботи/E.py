n = int(input())
s = input()

time = 0
def going_to_school(n, s, time):
    for i in range(n):
        time += 1
        if s[i] == 'R':
            time += 1
    return time

result = going_to_school(n, s, time)
print(result)

