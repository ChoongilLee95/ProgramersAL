def hi(l):
    m = l.pop()
    if m !='.':
        l.append(m)
    return l


def solution(new_id):
    answer1 = new_id.lower()
    answer1 =list(answer1)
    ban ="~!@#$%^&*()=+[{]}:?,<>/"
    ban =list(ban)
    answer =[]

    for i in ban:
        a=answer1.count(i)
        if a !=0:
            for k in range(a):
                answer1.remove(i)

    for i in range(len(answer1)-1):
        if answer1[i] =='.':
            if answer1[i+1]=='.':
                continue
            else:
                answer+=[answer1[i]]
        else:
             answer+=[answer1[i]]
    answer+=[answer1.pop()]

    if answer[0] =='.':
        answer.remove('.')

    if answer == []:
        answer =['aaa']
    else:
        answer = hi(answer)
        if len(answer)>15:
            answer = answer[:15]
            answer = hi(answer)
        elif len(answer)>2:
            pass
        elif len(answer)==2:
            answer=answer+[answer[1]]
        elif len(answer)==1:
            answer=answer*3
        else:
            answer = ['aaa']

    answer= "".join(answer)
    return answer


a = "...!@BaT#*..y.abcdefghijklm"
b = ".aaaaaaaaaaaaaa.a"

print(solution(a))
print(solution(b))