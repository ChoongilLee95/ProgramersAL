def solution(progresses, speeds):
    # 뒤에 완료된 배포사항은 앞의 작업 이후 같이 배포
    answer = []
    (share, remain) = divmod((100-progresses[0]),speeds[0])
    if remain:
        share +=1
    time_first_func = share
    num_finished = 1
    for i in range(1,len(progresses)):
        (share, remain) = divmod((100-progresses[i]),speeds[i])
        if remain:
            share +=1
        if time_first_func < share:
            answer.append(num_finished)
            num_finished = 1
            time_first_func = share
        else:
            num_finished +=1
    if num_finished:
        answer.append(num_finished)
    return answer

progresses = [93, 30, 55]
speeds = [1, 30, 5]

print(solution(progresses, speeds))