def Anagrams(word1,word2):
    word1=word1.lower()
    word2=word2.lower()
    return sorted(word1)==sorted(word2)
print( Anagrams("suresh","resush"))
print( Anagrams("times","minus"))
print( Anagrams("explore","perolex"))
print( Anagrams("python","typhon"))

