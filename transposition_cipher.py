#in a transposition algorithm, the key is how many spaces you'll "shift" the next letter in the column
#you're not changing the letters, you're repositioning them!

import pyperclip

def main():
    myMessage = 'There once was a man from Peru, who dreamed he was eating his shoe...'

    myKey = 8 #this is going to be the shift in position

    ciphertext = encryptMessage(myKey, myMessage)

    #print the encrypted string in ciphertext to the screen, with
    #a | after it in case there are spaces at the end of the encrypted message:
    print(ciphertext + '|')

    #copy the encrypted string in ciphertext to the clipboard:
    pyperclip.copy(ciphertext)


def encryptMessage(key, message):
    #each string will represent a column in the grid
    ciphertext = [''] * key

    #loop through each column in  ciphertext
    for column in range(key):
        currentIndex = column
        #keep looping until currentIndex goes past the message length
        while currentIndex < len(message):
            #place the character at currentIndex in the message at the end of the current column in the ciphertext list
            ciphertext[column] += message[currentIndex]

            #move currentIndex over:
            currentIndex += key

    #convert the ciphertext list into a single string value and return
    print(ciphertext)
    return ''.join(ciphertext)

#if transpositionencrypt.py is run, call the main() function
if __name__ == '__main__':
    main()