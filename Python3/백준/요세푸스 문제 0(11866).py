n, k = map(int, input().split())

yose = []
result = []
answer = '<'

for i in range(1, n+1) :
    yose.append(i)

for i in range(n) :
    for j in range(k-1) :
        yose.append(yose.pop(0))
    result.append(yose.pop(0))

answer += (', '.join(str(_) for _ in result))
answer += '>'

print(answer)
