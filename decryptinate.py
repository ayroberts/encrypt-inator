from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import os

def decrypt_image(input_image_path, output_image_path, key):
    with open(input_image_path, 'rb') as f:
        iv = f.read(16)
        encrypted_data = f.read()

    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)

    os.makedirs(os.path.dirname(output_image_path), exist_ok=True)
    with open(output_image_path, 'wb') as f:
        f.write(decrypted_data)

def read_key(key_folder="key"):
    with open(os.path.join(key_folder, "key.txt"), "rb") as key_file:
        return key_file.read()

if __name__ == "__main__":
    secret_folder = "secret"
    output_folder = "vulnerable"
    
    for root, _, files in os.walk(secret_folder):
        for file in files:
            input_image_path = os.path.join(root, file)
            output_image_path = os.path.join(output_folder, os.path.relpath(input_image_path, secret_folder))

            key = read_key()
            decrypt_image(input_image_path, output_image_path, key)

    print("Decryption complete.")
