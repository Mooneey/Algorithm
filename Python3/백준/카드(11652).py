n = int(input())

count = {}

for i in range(0, n) :
    key = int(input())

    if key in count.keys() :
        count[key] = count[key] + 1
    else :
        count[key] = 1


sort_count = sorted(count.items(), key = lambda x: (-x[1], x[0]))

print(sort_count[0][0])
