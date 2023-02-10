import string
import time

def vigenere_cipher(text, key, mode):
    key_len = len(key)
    key_index = 0
    result = ""
    for char in text:
        char = char.upper()
        if char.isalpha():
            key_char = key[key_index % key_len].upper()
            key_index += 1
            if mode == 'encrypt':
                result += chr((ord(char) + ord(key_char) - 2 * ord('A')) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord(key_char) + 26) % 26 + ord('A'))
    return result

def brute_force_cracker(ciphertext, key_length, first_word_length, dict_file):
    with open(dict_file, 'r') as f:
        words = set(word.strip().upper() for word in f)
    result = []
    for i in range(26**key_length):
        key = ""
        for j in range(key_length):
            key += chr(i // (26**j) % 26 + ord('A'))
        plaintext = vigenere_cipher(ciphertext, key, 'decrypt')
        first_word = plaintext[:first_word_length].upper()
        if all(char in string.ascii_letters for char in first_word) and first_word in words:
            result.append(plaintext)
    return result

print("-------------------------------------------------------")
print("Audrey's Vigenere Cipher & Brute Force Password Cracker")
print("-------------------------------------------------------")
print("\t1. Encrypt")
print("\t2. Decrypt")
print("\t3. Brute Force")

choice = int(input("\n\tEnter your choice (1/2/3): "))

if choice == 1:
    text = input("\nEnter the message: ")
    key = input("Enter the key: ")
    result = vigenere_cipher(text, key, 'encrypt')
    print("\nEncrypted message:", result)
elif choice == 2:
    text = input("\nEnter the ciphertext: ")
    key = input("Enter the key: ")
    result = vigenere_cipher(text, key, 'decrypt')
    print("\nDecrypted message:", result)
else:
    ciphertext = input("\nEnter the ciphertext: ")
    key_length = int(input("Enter the key length: "))
    first_word_length = int(input("Enter the length of the first word: "))
    dict_file = ("MP1_dict.txt")

    start_time = time.time()
    result = brute_force_cracker(ciphertext, key_length, first_word_length, dict_file)
    end_time = time.time()

    print("\nTime taken to Brute Force Crack the Password:", end_time - start_time, "seconds")
    for plaintext in result:
        print("Decrypted message:", plaintext)
