import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

def decrypt_file(input_file, output_file, key):
    key = key.encode('utf-8')

    with open(input_file, 'rb') as f:
        # Read the IV from the input file
        iv = f.read(16)

        # Initialize the decryptor with the provided key and IV
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
        decryptor = cipher.decryptor()

        # Decrypt the ciphertext
        ciphertext = f.read()
        decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()

        # Remove the padding from the decrypted data
        unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
        decrypted_data = unpadder.update(decrypted_data) + unpadder.finalize()

    # Write the decrypted data to the output file
    with open(output_file, 'wb') as f:
        f.write(decrypted_data)

# Prompt the user to enter the file location
while True:
    file_location = input("Enter the file path you want to decrypt: ")
    
    # Remove double quotes from the file location if present
    file_location = file_location.strip('"')
    
    # Check if the specified file exists
    if os.path.isfile(file_location):
        break
    else:
        print("File not found. Please enter a valid file location.")

# Prompt the user to enter the decryption key
key = input("Enter the decryption key: ")

# Decrypt the file
output_file = os.path.splitext(file_location)[0]  # Remove the extension from the input file
decrypt_file(file_location, output_file, key)
print("Decryption completed.")
