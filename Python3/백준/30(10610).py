n = list(input())

n.sort(reverse=True)
answer = 0

if '0' not in n :
    print(-1)

else :
    for i in n:
        answer += int(i)
    if answer % 3 != 0 :
        print(-1)
    else :
        print(''.join(n))
