n = int(input())

word_list=[]

for i in range(n) :
    word = input()
    word_count = len(word)
    word_list.append((word_count, word))

word_list = list(set(word_list))

word_list.sort(key=lambda word:(word[0], word[1]))

for i in word_list :
    print(i[1])
