#vigenere goes terribly on sandwiches

import pyperclip

POSSIBLE_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    anotherMessage = True

    while anotherMessage:  # let's have fun and give the user a chance to encrypt more messages
        message = input('Please input your message: ')
        myKey = 'CYBERSECURITY' #you can make this whatever. Just remember, for each letter you add, you multiply the
        # number of possible combinations by 26!

        mode = input('Would you like to encrypt or decrypt this message? (Enter encrypt or decrypt) ')#'decrypt' #set to 'encrypt' or 'decrypt'

        if mode.lower() == 'encrypt':
            translated = encryptMessage(myKey, message)
        elif mode.lower() == 'decrypt':
            translated = decryptMessage(myKey, message)

        print('%sed message:' % (mode.title()))
        print(translated)
        pyperclip.copy(translated)
        print()
        print('The message has been copied to the clipboard.')
        promptUser = input('Would you like to run the program again? (y/n) ')

        if promptUser == 'n':
            anotherMessage = False

def encryptMessage(key, message):
    return translateMessage(key, message, 'encrypt')

def decryptMessage(key, message):
    return translateMessage(key, message, 'decrypt')

def translateMessage(key, message, mode):
    translated = [] #stores the message string

    index = 0
    key = key.upper()

    for symbol in message: #loop through each symbol
        number = POSSIBLE_LETTERS.find(symbol.upper())
        if number != -1: #means  symbol.upper  was  not found in LETTERS
            if mode  ==  'encrypt':
                number += POSSIBLE_LETTERS.find(key[index])  #add if encrypting
            elif mode == 'decrypt':
                number -= POSSIBLE_LETTERS.find(key[index]) #subtract if decrypting

            number %= len(POSSIBLE_LETTERS) #deals with wraparound

            #add to end of translated
            if symbol.isupper():
                translated.append(POSSIBLE_LETTERS[number])
            elif symbol.islower():
                translated.append(POSSIBLE_LETTERS[number].lower())

            index += 1 #move to the next letter in the key
            if index == len(key):
                index = 0

        else:
            #append without encrypting/decrypting otherwise
            translated.append(symbol)
    return ''.join(translated)

if __name__ == '__main__':
    main()