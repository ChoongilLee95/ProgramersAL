from re import T


def solution(s):
    length_s = len(s)
    answer = length_s
    i =1
    while i < length_s//2+1:
        n= i
        h=0
        out = 0
        ss = ''#¤±¤¤¤·¤©
        t=1
        k=0
        while n < length_s-i+1:
            if s[n:n+i] == s[n-i:n]:
                h+=1
                t =0
            else:
                ss+=f'{h+1}'
                out +=h
                k+=t
                t=1
                h=0
            n += i
        ss += f'{h+1}'
        out +=h
        k+=t
        ans = length_s -out*i + len(ss)-k
        if answer > ans:
            answer = ans
        i +=1
    return answer

test = input()
print(solution(test))

