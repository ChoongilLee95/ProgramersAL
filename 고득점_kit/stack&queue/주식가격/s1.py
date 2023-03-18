def solution(prices):
    len_prices = len(prices)
    answer = [0]*len_prices
    price_stack = []
    # [시간, 가격]
    price_stack.append([0,prices[0]])
    for idx in range(1, len_prices):
        while price_stack and prices[idx] < price_stack[-1][1]:
            poped_price = price_stack.pop()
            answer[poped_price[0]] = idx - poped_price[0]
        price_stack.append([idx, prices[idx]])
    while price_stack:
        poped_price = price_stack.pop()
        answer[poped_price[0]] = len_prices-1 - poped_price[0]
    return answer