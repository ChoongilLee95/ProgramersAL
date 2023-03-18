from functools import cmp_to_key


def xy_compare(a,b):
    a = str(a)
    b = str(b)
    if a+b > b+a:
        return -1
    elif a+b == b+a:
        return 0
    return 1

def solution(numbers):
    answer = ''
    numbers.sort(key=cmp_to_key(xy_compare))
    answer = "".join(str(s) for s in numbers)
    if answer[0] == "0":
        answer = "0"
    return answer

print(solution([0,0,0]))