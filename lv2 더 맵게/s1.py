f_list = [1, 2, 3, 9, 10, 12]
k = 7

def solution(scoville, K):
    while k != 1:
        k = int(k/2)
    dis_scov = []
    dis_scov2 = []
    answer = 0
    for i in scoville:
        if i < K:
            dis_scov.append(i)
            dis_scov2.append(i*2)

    while dis_scov !=[]:
        t = dis_scov2.pop()
        complete = 0
        for i in range(1,len(dis_scov)):
            if dis_scov[i] + t>=k:
                answer += 1
                dis_scov2.pop(i)
                dis_scov.pop(i)
                dis_scov.pop()
                complete = 1
                break
        if complete == 0:
            t += dis_scov.pop(0)*2
            dis_scov.append(t)
            dis_scov2.append(t*2)


    return answer
print(1/3)