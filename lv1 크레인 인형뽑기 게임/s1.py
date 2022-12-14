board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
def solution(board, moves):
    answer=0
    new_board =[]
    width = len(board[0])
    for k in range(width):
        list_b=[]
        for j in board:
            b=j.pop(0)
            if b!=0:
                list_b.append(b)
        new_board+=[list_b]
    stack = [0]
    for i in moves:
        if new_board[i-1] != []:
            a = new_board[i-1].pop(0)
            b = stack.pop()
            if a == b:
                answer +=2
            else:
                stack.append(b)
                stack.append(a)
    return answer
print(solution(board, moves))

