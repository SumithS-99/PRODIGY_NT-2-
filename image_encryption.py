from PIL import Image
import numpy as np
import os


def encrypt_image(input_path, output_path, key):
    """Encrypt an image by applying a mathematical operation on pixel values."""
    try:
        # Open the image
        img = Image.open(input_path)
        img_array = np.array(img)

        # Apply encryption: Add the key to each pixel value
        encrypted_array = (img_array + key) % 256

        # Save the encrypted image
        encrypted_img = Image.fromarray(encrypted_array.astype('uint8'))
        encrypted_img.save(output_path)
        print(f"Image encrypted successfully and saved to: {output_path}")
    except Exception as e:
        print(f"Error during encryption: {e}")


def decrypt_image(input_path, output_path, key):
    """Decrypt an image by reversing the mathematical operation."""
    try:
        # Open the encrypted image
        img = Image.open(input_path)
        img_array = np.array(img)

        # Apply decryption: Subtract the key from each pixel value
        decrypted_array = (img_array - key) % 256

        # Save the decrypted image
        decrypted_img = Image.fromarray(decrypted_array.astype('uint8'))
        decrypted_img.save(output_path)
        print(f"Image decrypted successfully and saved to: {output_path}")
    except Exception as e:
        print(f"Error during decryption: {e}")


def main():
    print("Welcome to the Image Encryption Tool!")
    while True:
        print("\nOptions:")
        print("1. Encrypt an image")
        print("2. Decrypt an image")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")
        if choice == "1":
            input_path = input("Enter the path of the image to encrypt: ")
            output_path = input("Enter the path to save the encrypted image: ")
            key = int(input("Enter the encryption key (integer): "))
            encrypt_image(input_path, output_path, key)
        elif choice == "2":
            input_path = input("Enter the path of the encrypted image: ")
            output_path = input("Enter the path to save the decrypted image: ")
            key = int(input("Enter the decryption key (integer): "))
            decrypt_image(input_path, output_path, key)
        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
