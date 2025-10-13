#Word Analysis Tool

sentence = input("Please enter a sentence: ")

character_count = len(sentence.replace(" ", ""))
print("Number of characters:", character_count)

word_count = sentence.split()
print("Number of words:", len(word_count))

unique_words = set(word_count)
print ("Unique_words:", unique_words)

longest_word = max(word_count , key = len)
print("Longest word:", longest_word)






