from collections import defaultdict

def solution(phone_book):
    answer = True
    numbers = set(phone_book)
    for number in phone_book:
        for idx in range(1,len(number)):
            if number[0:idx] in numbers:
                answer = False
    return answer