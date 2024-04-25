# Decrypt

## Description

This Python script offers a decryption utility for files encrypted using the AES encryption algorithm in Cipher Block Chaining (CBC) mode with PKCS7 padding.

## Usage

1. **Prompting for File Location**: Upon execution, the script prompts the user to enter the location of the file they want to decrypt.

2. **Prompting for Decryption Key**: After specifying the file location, the user is prompted to enter the decryption key.

3. **Decryption Process**: The script reads the input file, extracts the IV (Initialization Vector) from the file, initializes the decryptor with the provided key and IV, decrypts the ciphertext, removes the padding from the decrypted data, and writes the decrypted data to the output file.

4. **Completion Message**: Once the decryption process is completed, a message indicating successful decryption is displayed.

## How to Use

1. Ensure that Python and the `cryptography` library are installed on your system.

2. Copy the provided script into a Python file (e.g., `decrypt.py`).

3. Run the script using Python by executing `python decrypt.py`.

4. Follow the prompts to enter the location of the file to decrypt and the decryption key.

5. After decryption, the decrypted file will be saved in the same directory with the same filename but without the `.h4g` extension.

## Note

- This is only used for this event.
H4G{A-D3cryt0r}


