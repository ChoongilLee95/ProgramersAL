#문제를 너무 어렵게 생각했다.
def solution(s):
    length_s = len(s)
    answer = length_s
    for i in range(1, length_s//2+1):
        n= i
        k = 0
        h = 0
        t = 0
        while n < length_s-i+1:
            if s[n:n+i] == s[n-i:n]:
                h += 1
                n += i
                k = 1
            else:
                t += k
                n+=i
                k=0
        t += k
        ans = length_s -i*h + t
        print(h,t)
        if answer >= ans:
            answer = ans
    return answer

test = input()
print(solution(test))


