def solution(s):
    answer = ''
    
    s = list(map(int, s.split()))
    
#     s = s.split()
#     maxnum = max(s)
#     minnum = min(s)
    
#     if int(minnum) > int(maxnum) :
#         minnum, maxnum = maxnum, minnum

    answer = str(min(s)) + ' ' + str(max(s))

    return answer
