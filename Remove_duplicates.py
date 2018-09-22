sentence = input('Enter the sentence ')
sort_sentence = sorted(sentence)
dedup = ''
length_sentence = len(sort_sentence)
for i in range(length_sentence):
    j = i+1
    if j > length_sentence-1:
        dedup = dedup + str(sort_sentence[i])
        break
    else:
        if sort_sentence[i] != sort_sentence[j]:
            dedup = dedup + str(sort_sentence[i])
print("'Sentence after removing duplicates '",dedup)
order = [0] * len(dedup)
for i in range(len(dedup)):
    if sentence.index(dedup[i]) < len(dedup):
        order.pop(sentence.index(dedup[i]))
    order.insert(sentence.index(dedup[i]),dedup[i])
for i in range(order.count(0)):
    order.remove(0)
print("'Unique values reverted to input order '",''.join(order))
