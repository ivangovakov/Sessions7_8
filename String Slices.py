s="0123456789"
print(s)
print(s[1:2]) #first index is included, last index is excluded
print(s[4:7])
print(s[:7]) #from the beginning
s1="i go to IE"
print(s1[:4])
print(s1[:]) #the whole thing
print(s1[::2]) #every second character
print(s1[::-1]) #reverse
s2=s1.replace(" ", "").lower()
print(s2)