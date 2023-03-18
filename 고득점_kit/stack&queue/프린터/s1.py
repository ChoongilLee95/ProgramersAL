from collections import deque
import heapq

def solution(priorities, location):
    answer = 0
    work_queue = deque()
    max_priority = []
    for idx in range(len(priorities)):
        heapq.heappush(max_priority, -priorities[idx])
        work_queue.append((idx,priorities[idx]))
    while work_queue:
        document = work_queue.popleft()
        if document[1] == -max_priority[0]:
            answer+=1
            if document[0] == location:
                break
            heapq.heappop(max_priority)
        else:
            work_queue.append(document)
    return answer