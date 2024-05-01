import random

def encode(word):
    if len(word) >= 3:
        new_word = word[1:] + word[0]
        random_chars = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=3))
        return random_chars + new_word + random_chars
    else:
        return word[::-1]

def decode(word):
    if len(word) < 3:
        return word[::-1]
    else:
        random_chars = word[:3]
        new_word = word[3:-3] + word[-4]
        return new_word

def main():
    choice = input("Enter 'code' to encode a message or 'decode' to decode a message: ").lower()

    if choice == 'code':
        message = input("Enter the message you want to encode: ")
        encoded_message = ' '.join(encode(word) for word in message.split())
        print("Encoded message:", encoded_message)
    elif choice == 'decode':
        message = input("Enter the message you want to decode: ")
        decoded_message = ' '.join(decode(word) for word in message.split())
        print("Decoded message:", decoded_message)
    else:
        print("Invalid choice. Please enter either 'code' or 'decode'.")

if __name__ == "__main__":
    main()
