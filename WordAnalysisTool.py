#Word Analysis Tool

sentence = input("Please enter a sentence: ")

character_count = len(sentence)
print("Number of characters:", character_count)

word_count = len(sentence.split())
print("Number of words:", word_count)

unique_words = set(sentence.split())
print (unique_words)

longest_word = max(sentence.split(), key=len)
print("Longest word:", longest_word)






