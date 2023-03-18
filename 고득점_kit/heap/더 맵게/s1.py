import heapq

def solution(scoville,K):
    answer = 0
    heapq.heapify(scoville)
    min_sco_food = heapq.heappop(scoville)
    while min_sco_food < K and len(scoville) != 0:
        food_for_adding = heapq.heappop(scoville)
        sco_of_new = min_sco_food + food_for_adding *2
        heapq.heappush(scoville, sco_of_new)
        min_sco_food = heapq.heappop(scoville)
        answer+=1
    if min_sco_food < K:
        answer = -1
    return answer
