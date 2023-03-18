
from collections import defaultdict, deque

def check_difference(word1, word2):
    difference = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            difference+=1
            if difference > 1:
                return False
    return True

def solution(begin, target, words):
    # 경로비용 일정 최단거리니까 bfs
    num_words = len(words)
    # 방문처리
    visited = [False]*num_words
    answer = 0
    words_queue = deque()
    words_queue.append((begin,0))
    while words_queue:
        (now_word,now_move) = words_queue.popleft()
        for i in range(num_words):
            if not visited[i] and check_difference(now_word,words[i]):
                if words[i] == target:
                    answer = now_move+1
                    return answer
                visited[i] = True
                words_queue.append((words[i],now_move+1))
    return answer
