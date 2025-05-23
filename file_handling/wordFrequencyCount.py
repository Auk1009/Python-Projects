# wordFrequencyCount
word_count = {}
with open('wordFrequencyCount.txt','r') as file:
    fileStr = file.read()
    print(fileStr)
    fileTokens = fileStr.split()
    print(fileTokens)

    for token in fileTokens:
       
        word_count[token] = fileStr.count(token)
       


    # for line in file:
    #     words_line = line.split()
        
    #     for word in words_line:
            # if word_count.get((word)) != None:
            #     temp_word_counter = word_count[word]
            #     temp_word_counter = int(temp_word_counter)+1
            #     word_count[word] = temp_word_counter
            #     print("Incrementing",word, word_count[word])
            # else:
            #     word_count[word] = 1
            #     print("Adding",word, word_count[word])

print(word_count)
                    
  