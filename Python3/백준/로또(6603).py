from itertools import combinations

while True :

    s = list(map(int, input().split()))

    if s[0] == 0 :
        break

    k = s.pop(0)
    
    combi = list(combinations(s, 6))

    for item in combi :
        item = list(item)

        for i in range(len(item)) :
            item[i] = str(item[i])

        answer = ' '.join(item)
        print(answer)

    print()
