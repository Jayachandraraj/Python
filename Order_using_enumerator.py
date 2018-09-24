sentence = input('Enter the sentence ')
sort_sentence = sorted(sentence)
dedup = ''
sentence_ind_dedup = []
ordered = ''


for i in range(len(sort_sentence)):
    j = i+1
    if j > (len(sort_sentence)-1):
        dedup = dedup + str(sort_sentence[i])
        break
    else:
        if sort_sentence[i] != sort_sentence[j]:
            dedup = dedup + str(sort_sentence[i])


print("'Sentence after removing duplicates '",dedup)
enumerate_dedup = list(enumerate(dedup))
enumerate_sentence = list(enumerate(sentence))
print('enumerated input', enumerate_sentence)
print('enumerated dedup',enumerate_dedup)


def order_match(val):
    for i in range(len(enumerate_sentence)):
        if val[1] == enumerate_sentence[i][1]:
            tup = (i,val[1])
            sentence_ind_dedup.append(tup)
            break
    return


for n in range(len(enumerate_dedup)):
    order_match(enumerate_dedup[n])

ordered_sentence = sorted(sentence_ind_dedup, key=lambda tup: tup[0])
print('dedup ordered using enumerator match', ordered_sentence)

for i in ordered_sentence:
    ordered = ordered + i[1]

    
print("'Unique values reverted to input order '", ordered)
