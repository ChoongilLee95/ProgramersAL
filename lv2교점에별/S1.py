def solution(line):
    answer_1 = []
    answer =[]
    x_axis = []
    y_axis = []
    for i in range(len(line)):
        for j in range(i+1,len(line)):
            cross_point = find_xy(line[i],line[j])
            if cross_point!='no':
                x_axis.append(cross_point[0])
                y_axis.append(cross_point[1])
    x_max = max(x_axis)
    x_min = min(x_axis)
    y_max = max(y_axis)
    y_min = min(y_axis)
    for i in range(y_max-y_min+1):
        answer_1 += [['.']*(x_max-x_min+1)]
    for i in range(len(x_axis)):
        answer_1[y_max-y_axis[i]][x_axis[i]-x_min] = '*'
    for i in range(y_max-y_min+1):
        answer.append("".join(answer_1[i]))
    print(answer)
    return answer

def find_xy(a,b):
    ans = 'no'
    if a[0]*b[1]-b[0]*a[1]:
        x = -(a[2]*b[1]-b[2]*a[1])/(a[0]*b[1]-b[0]*a[1])
        if int(x)==x:
            y = -(a[2]+a[0]*x)/a[1]
            if int(y)==y:
                ans = [int(x),int(y)]
    return ans

input = [[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]
input2 = [[1, -1, 0], [2, -1, 0], [4, -1, 0]]
solution(input)