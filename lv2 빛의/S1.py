def solution(grid):
    answer = []
    dict_node = {}
    dict_node_turn ={}
    list_node = []
    width_node = len(grid[0])
    height_node = len(grid)
    for i in range(height_node):
        colume = []
        for j in range(width_node):
            node_axis = [j,i]
            if grid[i][j]=='R':
                turn_v = [[0,-1],[1,0]]
            elif grid[i][j] =='L':
                turn_v = [[0,1],[-1,0]]
            else:
                turn_v = [[1,0],[0,1]]
            dict_node[str(node_axis)] = [[0,1],[1,0],[0,-1],[-1,0]]
            dict_node_turn[str(node_axis)] = turn_v
            colume.append(node_axis)
        list_node.append(colume)
    print(list_node,dict_node)
    print(width_node,height_node)
    for i in list_node:
        for j in i:
            if len(dict_node[str(j)])==0:
                pass
            else:
                k=0
                while k < len(dict_node[str(j)]):
                    start_position = j
                    start_direction = dict_node[str(j)][k]
                    position=[]
                    direction =[]
                    for n in [0,1]:
                        position.append(j[n])
                        direction.append(start_direction[n])
                    print(position,direction)
                    moves = 0
                    dict_node[str(position)].remove(direction)
                    position[0] = (position[0]+direction[0]+width_node)%width_node
                    position[1] = (position[1]+direction[1]+height_node)%height_node
                    new_direction = []
                    for dx in range(2):
                        new_direction += [direction[0]*dict_node_turn[str(position)][dx][0] + direction[1]*dict_node_turn[str(position)][dx][1]]
                    direction[0] = new_direction[0]
                    direction[1] = new_direction[1]
                    print(position,direction)
                    moves+=1
                    while (position!=start_position or direction!=start_direction):
                        dict_node[str(position)].remove(direction)
                        position[0] = (position[0]+direction[0]+width_node)%width_node
                        position[1] = (position[1]+direction[1]+height_node)%height_node
                        new_direction = []
                        for dx in range(2):
                            new_direction += [direction[0]*dict_node_turn[str(position)][dx][0] + direction[1]*dict_node_turn[str(position)][dx][1]]
                        direction[0] = new_direction[0]
                        direction[1] = new_direction[1]
                        moves+=1
                        print(position,direction)
                    k=0
                    answer.append(moves)
    answer.sort()
    return answer
solution(["SL","LR"])
solution(["S"])
print(solution(['R','R']))