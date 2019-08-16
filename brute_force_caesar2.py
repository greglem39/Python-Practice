#a brute forcing script that'll let the user input the script they want to brute force

encryptedMessage = input('Please enter the message you\'d like to decrypt: ')

POSSIBLE_SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

for key in range(len(POSSIBLE_SYMBOLS)):
    decrypted = ''

    for symbol in encryptedMessage:
        if symbol in POSSIBLE_SYMBOLS:
            symbolIndex = POSSIBLE_SYMBOLS.find(symbol)
            translatedIndex = symbolIndex - key

            if translatedIndex < 0:
                translatedIndex = translatedIndex + len(POSSIBLE_SYMBOLS) #this will help handle wraparound

            decrypted += POSSIBLE_SYMBOLS[translatedIndex]

        else:
            decrypted = decrypted + symbol #appending to decrypted if it's not in the symbol list

    #now let's see every attempt
    print('Key #%s: %s' % (key, decrypted))

"""questions for a future variant:
how can I make this work with web scraping?
is there a place where I can go to test this with web scraping, post requests, and running through this key
or should I build myself a simple site"""