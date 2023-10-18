# SHA-256 Encryption/Decryption Tool
## Overview:

The SHA-256 Encryption/Decryption Tool is a Python-based command-line utility designed to perform encryption and decryption operations using the SHA-256 hashing algorithm. This tool allows users to either encrypt a given text or attempt to decrypt a SHA-256 hash through a brute-force approach for input strings up to 5 characters in length.

## Features:

### 1. Encryption (Option: E):
Users can input a text string (up to 5 characters) and the tool will generate the corresponding SHA-256 hash. This feature is useful for securely hashing sensitive information.

### 2. Decryption (Option: D):
Users can input a SHA-256 hash, and the tool will attempt to find a matching input string using a brute-force approach. It systematically generates all possible combinations of up to 5-character strings, hashes them, and compares the result with the provided hash. If a match is found, the original input string is displayed.

## Usage Instructions:

### Encryption (Option: E):
Run the script and choose option "E" when prompted.
Enter the text to be encrypted (up to 5 characters).
The tool will output the corresponding SHA-256 hash.

### Decryption (Option: D):
Run the script and choose option "D" when prompted.
Enter the SHA-256 hash to be decrypted.
The tool will perform a brute-force search for a matching input string and display the result if found.

## Dependencies:
The tool uses the hashlib library for SHA-256 hashing.

## How to Run:
 - Clone the repository.
 - Ensure Python is installed on your system.
 - Open a terminal and navigate to the project directory.
 - Run the script using the command: python sha256_tool.py

## Contribution:
Contributions to the project are welcome. Users can contribute by improving the efficiency of the brute-force algorithm, enhancing the user interface, or addressing any identified issues.

## License:
This project is open-source and available under the MIT License.

Feel free to explore, use, and contribute to this SHA-256 Encryption/Decryption Tool!
