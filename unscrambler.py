base = input("Please enter a base word: ")
f = open('words.txt')
data = f.readlines()

sorted_base = sorted(base)
results = []

for word in data:
    sorted_dictionary = sorted(word.strip().lower())
    if all(elem in sorted_base for elem in sorted_dictionary):
        results.append(word.strip())
    
sortedList = sorted(results, key = len)

print("Here are the 6 lettered words")
for word2 in sortedList:
    if (len(word2) == 6):
        print(word2)
        
print("Here are the 5 lettered words: ")
for word3 in sortedList:
    if (len(word3) == 5):
        print(word3)
        
print("Here are the 4 lettered words: ")
for word4 in sortedList:
    if (len(word4) == 4):
        print(word4)
        
print("Here are the 3 lettered words: ")
for word5 in sortedList:
    if (len(word5) == 3):
        print(word5)
        
        
            
        
