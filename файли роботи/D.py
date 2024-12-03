a = int(input())
b = int(input())
c = int(input())

def solution(a, b, c):
    total_balls = a + b + c

    if total_balls % 3 != 0:
        return -1

    target_balls = total_balls / 3

    moves_of_balls = abs(a - target_balls) + abs(b - target_balls) + abs(c - target_balls)

    return moves_of_balls / 2

result = solution(a, b, c)
print(result)






