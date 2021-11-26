def solution (people, limit) :
    answer = 0
    people.sort()
    
    start, end = 0, len(people) - 1
    
    while start <= end : # 앞 뒤로 한명씩
        # 앞 뒤 한명씩 추가하고 제한보다 작으면 출발
        if people[start] + people[end] <= limit : 
            start += 1
        # 아니면 뒤에 한명만 출발
        end -= 1

        answer += 1

    return answer
