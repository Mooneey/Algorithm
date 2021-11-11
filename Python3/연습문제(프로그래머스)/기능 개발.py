def solution(progresses, speeds) :
    answer = []
    tmp = 0

    while progresses :

        for i in range(len(progresses)):
            progresses[i] += speeds[i]


        for i in range(len(progresses)):
            if  progresses[0] >= 100 :
                progresses.pop(0)
                speeds.pop(0)
                tmp = tmp + 1
            else : break
        
        if tmp != 0 :
            answer.append(tmp)  
            tmp = 0

    return answer
