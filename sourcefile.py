import hashlib

# The original hash
print("SHA 256 ENCRYPTION/DECRYPTION ")
type = input("Enter Option: Encrypt/Decrypt (E/D): ")


if type == "D":
    import hashlib

    # The original hash
    hash = input("Enter hash: ")

    # Try all possible combinations of upto 5-character input
    for a in range(ord('0'), ord('z')):
        for b in range(ord('0'), ord('z')):
            for c in range(ord('0'), ord('z')):
                for d in range(ord('0'), ord('z')):
                    for d in range(ord('0'), ord('z')):
                        # Generate the input from the characters
                        input = chr(a) + chr(b) + chr(c) + chr(d)

                        # Calculate the SHA-256 hash of the input
                        sha256 = hashlib.sha256(input.encode('utf-8')).hexdigest()

                        # Compare the hash to the original
                        if sha256 == hash:
                            print("Found matching input:", input)
                            break

elif type == "E":

    import hashlib

    # The string to encrypt
    string = input("Enter your text (upto 5 characters only): ")

    # Calculate the SHA-256 hash of the string
    sha256 = hashlib.sha256(string.encode('utf-8')).hexdigest()

    # Print the hash
    print("Encrypted Text SHA-256: ", sha256)



