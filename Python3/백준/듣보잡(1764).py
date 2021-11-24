n, m = map(int, input().split())
nohear = []
nosee = []
answer = []
for i in range(0, n+m) :
    if i < n :
        nohear.append(input())
    else :
        nosee.append(input())

answer = list(set(nohear) & set(nosee))
answer.sort()

print(len(answer))
for i in range(0, len(answer)) :
    print(answer[i])
