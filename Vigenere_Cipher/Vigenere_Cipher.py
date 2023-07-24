# Vigenere Cipher is a method of encrypting alphabetic text. It uses a simple form of
# polyalphabetic substitution. A polyalphabetic cipher is any cipher based on substitution,
# using multiple substitution alphabets. The encryption of the original text is done using the
# Vigenère square or Vigenère table.
# The table consists of the alphabets written out 26 times in different rows, each alphabet
# shifted cyclically to the left compared to the previous alphabet, corresponding to the 26
# possible Caesar Ciphers.
# At different points in the encryption process, the cipher uses a different alphabet from
# one of the rows.
# The alphabet used at each point depends on a repeating keyword.
# Input: Plaintext: MICHIGAN TECHNOLOGICAL UNIVERSITY
# Keyword: HOUGHTON
# Output: Ciphertext : TWWNPZOA ASWNUHZBNWWGS NBVCSLYPMM
# For generating key, the given keyword is repeated in a circular manner until it matches the
# length of the plain text.
# The keyword "HOUGHTON" generates the key "HOUGHTON HOUGHTONHOUGH
# TONHOUGNTO". The plain text is then encrypted using the process explained below.

# Encryption
# To encrypt, pick a letter in the plaintext and its corresponding letter in the keyword, use the
# keyword letter and the plaintext letter as the row index and column index, respectively, and
# the entry at the row-column intersection is the letter in the ciphertext. For example, the first
# letter in the plaintext is M and its corresponding keyword letter is H. This means that the
# row of H and the column of M are used, and the entry T at the intersection is the encrypted
# result. Similarly, since the letter N in MICHIGAN corresponds to the letter N in the keyword,
# the entry at the intersection of row N and column N is A which is the encrypted letter in the
# ciphertext.
# Decryption
# To decrypt, pick a letter in the ciphertext and its corresponding letter in the keyword, use
# the keyword letter to find the corresponding row, and the letter heading of the column that
# contains the ciphertext letter is the needed plaintext letter. For example, to decrypt the first
# letter T in the ciphertext, we find the corresponding letter H in the keyword. Then, the row
# of H is used to find the corresponding letter T and the column that contains T provides the
# plaintext letter M (see the above figures). Consider the fifth letter P in the ciphertext. This
# letter corresponds to the keyword letter H and row H is used to find P. Since P is on column
# I, the corresponding plaintext letter is I.
def Gen_key(string, key): # defining gen function for generating keyword
    key = list(key) # converting key to lists
    if len(string) == len(key): # checking whether the key matches to the length of input string
        return (key)
    else:
        for i in range(len(string) - len(key)): #if not matches it increases the lenght by it self
            key.append(key[i % len(key)])
    return ("".join(key))
def ciphertext(string, key): #defining ciphertext for conversion
    cipher_text = []
    for i in range(len(string)):
        A = (ord(string[i]) + ord(key[i])) % 26 #Ei=(Pi + Ki)mod 26 Encryption
        A += ord('A') # for replacing the alphabet in original place
        cipher_text.append(chr(A))# adding original converted text to the original text
    return ("".join(cipher_text))
def decryptedtext(cipher_text, key): # defining decryptedtext
    orig_text = []
    for i in range(len(cipher_text)):
        A = (ord(cipher_text[i]) - ord(key[i]) + 26) % 26 #Di = (Ei - Ki + 26) mod 26 Decryption
        A += ord('A') # for replacing the alphabet in original place
        orig_text.append(chr(A))# adding original converted text to the original text
    return ("".join(orig_text))
if __name__ == "__main__":
    plaintext = input("Enter Plain Text: ") #input of plaintext
    s=plaintext.replace(" ","") # it is used to replace space
    keyword= input("Enter key: ") #input of key word
    key = Gen_key(s, keyword) # calling gen function for generating keyword
    cipher_text = ciphertext(s, key) # calling ciphertext function for encryption
    print("Cipher Text is :", cipher_text)
    if decryptedtext(cipher_text,key)==s:
        print("Original text :",plaintext) #printing the original text or decrypted text