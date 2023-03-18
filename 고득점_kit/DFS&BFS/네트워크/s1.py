

def dfs(computers,n, dp, idx):
    for i in range(n):
        if computers[idx][i]==1 and dp[i] == 0:
            dp[i] = 1
            dfs(computers,n,dp,i)
def solution(n, computers):
    dp = [0]*n
    answer = 0
    for i in range(n):
        if dp[i] == 0:
            answer +=1 
            dfs(computers,n,dp,i)
    return answer