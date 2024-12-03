a, b, c = map(int, input().split())

def solution(a, b, c):
    remaining_time = b - c
    if remaining_time < a:
        print("YES")
    else:
        print("NO")

solution(a, b, c)

