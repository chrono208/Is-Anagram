def is_anagram(word1, word2):
    wordList = []
    for letter in word2:
        wordList.append(letter)
    print(wordList)
    for letter in word1:
        try:
            wordList.remove(letter)
        except:
            print("caught exception")
            return False
    print(len(wordList))
    if len(wordList) == 0:
        return True
    else:
        return False