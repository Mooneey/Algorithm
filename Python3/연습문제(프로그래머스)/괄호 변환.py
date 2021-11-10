def check(p) :
    stack = []

    for i in p : 
        # 스택 안에 값이 있을 때
        stack.append(i)

        # 2개 이상 있고
        if len(stack) >= 2 : 
            # 괄호가 맞으면 스택에서 pop
            if stack[-2] == '(' and i == ')' :
                stack.pop()
                stack.pop()

    if stack :
        return False

    return True




def separate(p) :
    count = [0, 0] # '(', ' )' 의 개수 카운트
    for i in p :
        if i == '(' : 
            count[0] += 1
        else : 
            count[1] += 1
        
        if count[0] == count[1] :
            # return u, v
            return p[:(count[0]*2)], p[count[0]*2:]
        


def solution(p) :
    answer = ''
    # 입력이 빈 문자열인 경우
    if p == '' :
        return p # 그대로 반환
    
    elif check(p) :
        return p
    
    else :
        u, v = separate(p)

        if check(u) :
            answer = u
            answer = answer + solution(v)
        
        else :
            answer = '('
            answer = answer + solution(v) + ')'
            reverse = ''

            for i in u[1:-1] :
                if i == '(' :
                    reverse = reverse + ')'
                else :
                    reverse = reverse + '('

            answer = answer + reverse
                
    return answer
