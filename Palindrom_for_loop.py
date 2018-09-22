x=input('Enter a word to test for Palindrome ')
y=len(x)//2
z=len(x)
for i in range(y):
    n=i+1
    m=z-i-1
    o=z-i
    #print(x[i:n])
    #print(x[m:o])
    if x[i:n] != x[m:o]:
        print('Not a Palindrome')
        break
if n == y:
    print('You got a Palindrome')
