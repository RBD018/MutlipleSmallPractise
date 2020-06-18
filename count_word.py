def count_word(sntce,word):
    cnt = 0
    l1 = word.split()
    for i in range(0,len(sntce)-1):
        for j in range(0,len(word)-1):
   #         cnt += 1
            if sntce[i] == word[j] and sntce[i+1] == word[j+1]:  
                cnt+=1
    return cnt

sentence = input("Enter the string: ")
word = input("Enter the word you want to check : ")
print(count_word(sentence,word))

