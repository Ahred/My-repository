def solution(number):
    new_list = []
    for a in range(number):
        if a % 3 == 0 or a % 5 == 0:
            if a not in new_list:
                new_list.append(a)
    return sum(new_list)
