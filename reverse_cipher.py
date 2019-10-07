#reverse cipher
#https://www.nostarch.com/crackingcodes/

message = input("Please input your message: ")

#print(message)

encrypted = ''

i = len(message) - 1 #get length
print(i)

"""while i >= 0:
    encrypted += message[i] #since i is the length, it's the last character, thus reversing it
    i = i - 1

print(encrypted) 

This is what I got from the cracking codes book"""

encrypted2 = ''.join(reversed(message))

print(encrypted2)