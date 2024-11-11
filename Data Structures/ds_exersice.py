sentence = "This is a common interview question"
sentence_dict = {}

for word in sentence:
    if word in sentence_dict:
        sentence_dict[word] += 1
    else:
        sentence_dict[word] = 1

print(f"All the words count{sentence_dict}")
print(max(sentence_dict))
