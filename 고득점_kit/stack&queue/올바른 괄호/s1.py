def solution(s):
    answer = True
    stack = []
    if s[0] == ")":
        return False
    else:
        stack.append(s[0])
    for i in range(1,len(s)):
        if s[i] == ")":
            if stack != [] and stack.pop() == "(":
                continue
            else:
                answer = False
                break
        else:
            stack.append(s[i])
    if stack:
        answer = False
    return answer