"""
# 1

words = ["This", "is", "An", "Example", "Of", "PYTHON", "syntax"]

word_lowered = [] 
for word in words: 
    word_lowered.append(word.lower())
print(word_lowered)

# 2
words = ["This", "is", "An", "Example", "Of", "PYTHON", "syntax"]
word_lower = [word.lower() for word in words if len(word) > 3  ] # list comprehension
print(word_lower)

words = ["NLP", "is", "fun"] 
for index, value in enumerate(words):
    print (index, value) 

# 3
for index, value in enumerate(words, start=1):
    print (index, value) 

# 4
words = ["deep", "learning", "rocks"]
lengths = [4, 8, 5]

for item1,item2 in zip(words, lengths):
    print (item1, item2)

# 5
words = ["deep", "learning", "rocks", "AI"]
lengths = [4, 8, 5, 2]

for item1,item2 in zip(words,lengths):
     if len(item1) > 4:
        print(item1, item2)

words = ["deep", "learning", "rocks", "AI"]
lengths = [4, 8, 5, 2]
words_list = [f"{item1} {item2}"  for item1,item2 in zip(words,lengths) if len(item1) > 4 ]
print(words_list)

tokens = ["nlp", "is", "fun", "and", "useful"]
freqs  = [5, 1, 4, 2, 3]

words_list = [f"{item1}:{item2}" for item1,item2 in zip(tokens,freqs) if item2 > 2]
print(words_list)
"""




