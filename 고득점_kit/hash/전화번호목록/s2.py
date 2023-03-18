from collections import defaultdict

def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if len(phone_book[i]) < len(phone_book[i+1]) and phone_book[i] == phone_book[i+1][0:len(phone_book[i])]:
            answer = False
    return answer