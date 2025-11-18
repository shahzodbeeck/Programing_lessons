#task 13
i =1
n = int(input("Enter a number: "))
while i<=10:
    print(i*n)
    i = i + 1


#task 14
given_list =['toyota', 'toyota 1', 'toyota 2', 'toyota 3 d f']
max_len = len(given_list[0])
i = 0
index=0
while i < len(given_list):
    if len(given_list[i])>max_len:
        max_len = len(given_list[i])
        index = i
    i+=1
print(given_list[index])

#task 15
given_list =['toyota', 'toyota 1', 'toyota 2', 'toyota 3 d f','bmw','olma']
i = 0
index=0
while i < len(given_list):
    if given_list[i][-1] == 'a':
        print(given_list[i])
    i+=1


#home task
all_words =[]
seen_words = set()
while True:
    ask_word = input("Enter a word: ")
    if ask_word == "quit":
        break
    elif ask_word not in seen_words:
        all_words.append(ask_word)
        seen_words.add(ask_word)
    else:
        print("Word already in use,Not added")

summary={
    "total_words": len(all_words),
    "status": "No words added" if not all_words else "All words added" ,
}
print(summary)
print(all_words)
print(seen_words)