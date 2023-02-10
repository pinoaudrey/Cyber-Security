import string

def vigenere_cipher(text, key, mode):
    key_len = len(key)
    key_index = 0
    result = ""
    for char in text:
        char = char.upper()
        if char.isalpha():
            key_char = key[key_index % key_len].upper()
            key_index += 1
            if mode == '1':
                result += chr((ord(char) + ord(key_char) - 2 * ord('A')) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord(key_char) + 26) % 26 + ord('A'))
    return result

print("------------------------")
print("Audrey's Vigenere Cipher")
print("------------------------")
print("\t1. Encrypt")
print("\t2. Decrypt")

mode = int(input("\n\tEnter your choice (1/2): "))
text = input("Enter the text to encrypt/decrypt: ")
key = input("Enter the key: ")

result = vigenere_cipher(text, key, mode)

print("Result:", result)
