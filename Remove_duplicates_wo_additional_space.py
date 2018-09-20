a = list(input('Enter word '))
a.sort()
i = 0
while i < (len(a) - 1):
    if a[i] == a[i+1]:
        a.pop(i)
    else:
        i += 1
print(''.join(a))

#for i in range(len(a) - 1):
#    if i == len(a) - 1:
#        if a[i] == a[i-1]:
#            a.pop(i)
#        break
#    print(i,a[i],a[i+1])
#    if a[i] == a[i+1]:
#        a.pop(i)
#    #if i == len(a) - 2:
#    #    break
#    print(a)
#print(a)
