# Image Encryption using Pixel Manipulation - Cyber Security Internship Task

## Description
This Python project uses the Pillow (PIL) library to encrypt and decrypt an image by modifying its RGB values using a simple key.

## How it works
- **Encryption**: Adds a numeric key to every RGB value of each pixel.
- **Decryption**: Subtracts the same key to recover the original image.

## Files
- `encrypt_image.py`: Encrypts the image
- `decrypt_image.py`: Decrypts the image
- `sample.jpg`: The image used for testing

## Usage
1. Run `encrypt_image.py` to create `encrypted_image.png`
2. Run `decrypt_image.py` to restore the original image

```bash
python3 encrypt_image.py
python3 decrypt_image.py
