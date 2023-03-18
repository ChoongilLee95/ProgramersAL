
from collections import deque
# bfs문제
def solution(maps):
    # 방문처리는 maps에 0을 표시해서 처리
    max_col = len(maps)
    max_row = len(maps[0])
    answer = -1
    col_move = [1,0,-1,0]
    row_move = [0,1,0,-1]
    position_queue = deque()
    position_queue.append([0,0,1])
    while position_queue:
        [col_now,row_now,now_moves] = position_queue.popleft()
        if col_now == max_col-1 and row_now == max_row-1:
            answer = now_moves
            break
        for i in range(4):
            next_col = col_now+col_move[i]
            next_row = row_now+row_move[i]
            if -1<next_col<max_col and -1< next_row < max_row and maps[next_col][next_row]:
                maps[next_col][next_row]=0
                position_queue.append([next_col,next_row,now_moves+1])
    return answer

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))