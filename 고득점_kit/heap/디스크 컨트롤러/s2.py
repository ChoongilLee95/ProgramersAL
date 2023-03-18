import heapq
def solution(jobs):
    answer = 0
    job_doing = [jobs[0][1], jobs[0][0]]
    # 일단 시작한 작업은 끝날 떄 까지 지속된다고 가정한다면 시간은 이미 시작한 작업의 끝나는 시점으로 흐른다
    timer = job_doing[0] + job_doing[1]
    waiting_job = []
    idx = 1
    num_jobs = len(jobs)
    heapq.heapify(jobs)
    for _ in range(1,num_jobs):
        answer += timer - job_doing[1]
        # 흐른 시간을 기준으로 jobs 리스트에 있는 작업들을 heap리스트로 옮긴다. 기준은 작업시간
        while idx<num_jobs and jobs[idx][0] <= timer:
            heapq.heappush(waiting_job, [jobs[idx][1],jobs[idx][0]])
            idx+=1
        if len(waiting_job):
            # 작업을 하나 추가하고 작업시간만큼 timer 시간 추가.
            job_doing = heapq.heappop(waiting_job)
            timer += job_doing[0]
        else:
            timer = jobs[0][0]
    answer += timer - job_doing[1]
    answer = answer//num_jobs
    return answer