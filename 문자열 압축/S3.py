def solution(s):
    length_s = len(s)
    answer = length_s
    i =1
    while i < length_s//2+1:
        n= i # しぉいしぉいし
        k = 0
        h = 0
        t1 = 0
        t2 = 0
        while n < length_s-i+1:
            if s[n:n+i] == s[n-i:n]:
                h += 1
            elif h>0:
                t1 += len(str(h))
                t2 += h
                h=0
            else:
                continue
            n += i
        if h:
            t1 += len(str(h+1))
            t2 += h
        ans = length_s -i*t2 + t1
        if answer > ans:
            answer = ans
        i +=1
    return answer