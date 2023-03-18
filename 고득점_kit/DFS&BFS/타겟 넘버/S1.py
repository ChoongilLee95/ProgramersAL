def dfs(number_list, idx,target, sum_now):
    if idx == len(number_list)-1:
        answer=0
        if sum_now + number_list[idx] == target:
            answer +=1
        if sum_now - number_list[idx] == target:
            answer +=1
        return answer
    else:
        return dfs(number_list, idx+1, target, sum_now + number_list[idx]) + dfs(number_list, idx+1, target, sum_now - number_list[idx])


def solution(numbers, target):
    answer = dfs(numbers,0,target,0)
    return answer