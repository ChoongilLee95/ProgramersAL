import heapq

def solution(jobs):
    answer = 0
    # heapq.heapify(jobs)
    # [작업이 들어온 시점, 남은 작업시간, 작업에 다시 들어온 시점]
    # 시간이 변하는 시점은 다음 적업이 돌아온 시점에 작업이 들어온 시간으로 초기화
    # 작업중인 작업의 남은 시간이 더 작다면 이전 작업을 처리시간을 기준으로 작업큐(최소힙)에 넣는다
    # 작업중인 작업의 남은 시간이 더 크다면 이전 작업의 남은시간을 처리시간으로 초기화하고 작업큐(최소힙)에 넣는다. 
    # for문이 끝나고 작업중인 작업이 끝날 때 까지 대기
    job_doing = jobs[0]
    job_doing.append(jobs[0])
    for idx in range(len(jobs)):
        new_job = jobs[idx]
        # 작업이 들어온 시점에 이미 처리하고 있는 작업의 남은 처리시간과 들어온 작업과의 처리시간을 비교하고
        timer = jobs[idx][0]
        # 이미 끝났으면 다음 작업 시작
        if timer - job_doing[0] <= job_doing[1]:
            pass
    return answer