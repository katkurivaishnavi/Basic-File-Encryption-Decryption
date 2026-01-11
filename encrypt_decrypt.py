def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result


def decrypt(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) - shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            result += char
    return result


def main():
    print("1. Encrypt File")
    print("2. Decrypt File")
    choice = input("Enter your choice (1/2): ")

    filename = input("Enter file name: ")
    shift = int(input("Enter shift key: "))

    with open(filename, "r") as file:
        content = file.read()

    if choice == "1":
        encrypted_text = encrypt(content, shift)
        with open("encrypted.txt", "w") as file:
            file.write(encrypted_text)
        print(" File encrypted and saved as encrypted.txt")

    elif choice == "2":
        decrypted_text = decrypt(content, shift)
        with open("decrypted.txt", "w") as file:
            file.write(decrypted_text)
        print(" File decrypted and saved as decrypted.txt")

    else:
        print(" Invalid choice")


if __name__ == "__main__":
    main()
