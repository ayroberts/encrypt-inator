from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
import os

def encrypt_image(input_image_path, output_image_path, key):
    with open(input_image_path, 'rb') as f:
        image_data = f.read()

    iv = get_random_bytes(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted_data = cipher.encrypt(pad(image_data, AES.block_size))

    os.makedirs(os.path.dirname(output_image_path), exist_ok=True)
    with open(output_image_path, 'wb') as f:
        f.write(iv + encrypted_data)

def get_or_generate_key(key_folder):
    key_file_path = os.path.join(key_folder, "key.txt")
    if not os.path.exists(key_file_path):
        key = get_random_bytes(16)
        with open(key_file_path, "wb") as f:
            f.write(key)
    else:
        with open(key_file_path, "rb") as f:
            key = f.read()
    return key

if __name__ == "__main__":
    input_folder, output_folder, key_folder = "input", "secret", "key"
    os.makedirs(output_folder, exist_ok=True)
    key = get_or_generate_key(key_folder)

    for root, _, files in os.walk(input_folder):
        for file in files:
            encrypt_image(os.path.join(root, file), os.path.join(output_folder, os.path.relpath(os.path.join(root, file), input_folder)), key)

    print("Encryption complete.")
