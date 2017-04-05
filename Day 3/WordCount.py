def words(sentence):#Sentence is an argument
    my_string = sentence.lower().split()
    dic = {} #Declare a dictionary
    for word in my_string:
        dic[word] = my_string.count(word) #Counting words in a dictionary
    print(dic)#Output a dictionary
