from PIL import Image

def decrypt_image(image_path, key):
    img = Image.open(image_path)
    img = img.convert('RGB')
    pixels = img.load()

    width, height = img.size

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            r = (r - key) % 256
            g = (g - key) % 256
            b = (b - key) % 256
            pixels[i, j] = (r, g, b)

    img.save("decrypted_image.png")
    print("Decryption complete. Saved as decrypted_image.png")

# Example usage
decrypt_image("encrypted_image.png", key=50)
