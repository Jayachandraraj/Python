sentence=input('Enter the sentence to test for Palindrome ')
parse_sentence=sentence.split(" ")
#print(parse_sentence)
reconstruct_sentence="".join(parse_sentence)
#print(reconstruct_sentence)
reverse_sentence=reconstruct_sentence[::-1]
if reconstruct_sentence == reverse_sentence:
    print('You got a Palindrome sentence')
else:
    print('Not a Palindrome sentence')
