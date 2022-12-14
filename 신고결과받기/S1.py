
from multiprocessing.connection import answer_challenge
from re import A


id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k=2
def solution(id_list, report, k):
    id_add = dict()
    len_id = len(id_list)
    answer = [0]*len_id
    table = [len_id*[0] for i in range(len_id)]
    set_rep = set(report)
    for i,j in zip(id_list, range(len_id)):
        id_add[i] = j
    for x in set_rep:
        table[id_add[x.split()[1]]][id_add[x.split()[0]]] +=1
    for i in range(len_id):
        if sum(table[i])>=k:
            for j in range(len_id):
                answer[j] += table[i][j]
    return answer
print(solution(id_list, report, k))