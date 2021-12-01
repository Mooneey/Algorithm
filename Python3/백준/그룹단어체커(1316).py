n = int(input())

answer = n

for i in range(n) :
    word = input()
    for index in range(len(word)-1) :
        if word[index] != word[index+1] :
            if word[index+1] in word[:index] :
                answer -= 1
                break

print(answer)
