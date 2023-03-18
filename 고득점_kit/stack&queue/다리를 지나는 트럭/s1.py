from collections import deque
def solution(bridge_length, weight, truck_weights):
    #  완전히 오르지 않은 트럭의 무게는 무시합니다. -> 아무도 없는 시간은 시작할 때 뺴고 없다.
    answer = 0
    total_weight = 0
    truck_on_bridge = deque()
    idx = 0
    num_trucks = len(truck_weights)
    time = 0
    while idx < num_trucks:
        time +=1
        # 1. 먼저 빠져야 할 친구가 있다면 빼내자
        if truck_on_bridge and time - truck_on_bridge[0][0] == bridge_length:
            truck_out = truck_on_bridge.popleft()
            total_weight -= truck_out[1]
        # 2-1. 새로 들어가는 트럭의 무게를 더한 값이 weight보다 작다면 올리자
        if truck_weights[idx] + total_weight <= weight:
            truck_on_bridge.append([time,truck_weights[idx]])
            total_weight += truck_weights[idx]
            idx +=1
        # 2-2. 새로 누군가가 들어갈 수 없다면 하나의 트럭이 빠질때까지 시간을 흐르게 하자
        else:
            time = truck_on_bridge[0][0]+bridge_length-1
    # 마지막 트럭이 들어가고 시간이 아직 지나지 않음 -> 따라서 마지막 트럭이 지나가는 시간만큼 총 시간(time) 추가
    time+=bridge_length
    answer = time
    return answer
