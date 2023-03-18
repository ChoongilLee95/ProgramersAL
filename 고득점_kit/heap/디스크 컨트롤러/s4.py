import heapq
def solution(jobs):
    answer = 0
    num_jobs = len(jobs)
    heapq.heapify(jobs)
    timer = 0
    waiting_jobs = []
    while jobs or waiting_jobs:
        while jobs and jobs[0][0] <= timer:
            new_waiter = heapq.heappop(jobs)
            heapq.heappush(waiting_jobs, [new_waiter[1],new_waiter[0]])
        if waiting_jobs:
            job_doing = heapq.heappop(waiting_jobs)
            timer += job_doing[0]
            answer += timer - job_doing[1]
        else:
            timer = jobs[0][0]
    answer = answer//num_jobs
    return answer
print(solution([[0, 3], [1, 9], [2, 6]]))