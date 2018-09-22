#ascii_list = []
ascii_chr = '' 
ascii_hex = ''
start_range = 21
end_range = 80
#for i in range(10):
#    ascii_list.append(i)

#print(ascii_list)
#ascii_array = " ".join(str(ascii_list))

for i in range(start_range,end_range):
    ascii_hex = ascii_hex + str(i)
    ascii_chr = ascii_chr + chr(i+12)
    if i < end_range-1:
        ascii_hex = ascii_hex + str(' ')
    
#ascii_array = str("'") + ascii_array + str("'")
print(ascii_chr)
print(ascii_hex)
print(bytes.fromhex(ascii_hex))
print(bytes.fromhex(ascii_hex).decode())
