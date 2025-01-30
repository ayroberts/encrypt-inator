from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
import os

def encrypt_image(input_image_path, output_image_path, key):
    with open(input_image_path, 'rb') as f:
        image_data = f.read()
    
    inv = get_random_bytes(AES.block_size)  # Generate random initialization vector

    cipher = AES.new(key, AES.MODE_CBC, inv)
    padded_data = pad(image_data, AES.block_size)
    encrypted_data = cipher.encrypt(padded_data)

    with open(output_image_path, 'wb') as f:
        f.write(inv)  # Need this for decryption
        f.write(encrypted_data)

    print(f"Image encrypted and saved to {output_image_path}")


def generate_key():
    return get_random_bytes(16)  # AES requires a 16-byte key for AES-128, that's why it was padded earlier


if __name__ == "__main__":
    input_image = "input_image.jpg" # Need to do a batch folder
    output_image = "encrypted_image.enc"  

    key = generate_key()

    with open("key.txt", "wb") as key_file: 
        key_file.write(key)
    
    encrypt_image(input_image, output_image, key)
    print("Encryption complete, stored in /", output_image)
