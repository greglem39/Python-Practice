#we gonna hack some affine son

import pyperclip, affineCipher, detectEnglish, cryptomath

SILENT_MODE = False

def main():
    #I've just copied and pasted this from source code.
    myMessage = """5QG9ol3La6QI93!xQxaia6faQL9QdaQG1!!axQARLa!!AuaRLQADQALQG93!xQxaGaAfaQ1QX3o1RQARL9Qda!AafARuQLX1LQALQI1iQX3o1RNQ-5!1RQP36ARu"""

    hackedMessage = hackAffine(myMessage)

    if hackedMessage != None:
        #plaintext is displayed and we copy it for the user because they're lazier than me! :p
        print('Copying hacked message to clipboard.')
        print(hackedMessage)
        pyperclip.copy(hackedMessage)
    else:
        print('Failed to hack encryption.')

def hackAffine(message):
    print('Hacking...')

    #can be stopped at any time by pressing ctrl-c (windows) or ctrl-d (mac/linux)
    print('(Press Ctrl-C or Ctrl-D to quit at any time.)')

    #brute force is best force
    for key in range(len(affineCipher.SYMBOLS) ** 2):
        keyA = affineCipher.getKeyParts(key)[0]
        if cryptomath.gcd(keyA, len(affineCipher.SYMBOLS)) != 1:
            continue
        decryptedText = affineCipher.decryptMessage(key, message)
        if not SILENT_MODE:
            print('Tried key %s... (%s)' % (key, decryptedText[:40]))

        if detectEnglish.isEnglish(decryptedText):
            #check with user to see if the key has been found
            print()
            print('Possible encryption hack:')
            print('Key: %s' % (key))
            print('Decrypted message: ' + decryptedText[:200])
            print()
            print('Enter D for done or just press Enter to continue hacking:')
            response = input('> ')

            if response.strip().upper().startswith('D'):
                return decryptedText
    return None

if __name__ == '__main__':
    main()