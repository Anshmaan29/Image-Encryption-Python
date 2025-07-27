from PIL import Image

def encrypt_image(image_path, key):
    img = Image.open(image_path)
    img = img.convert('RGB')
    pixels = img.load()

    width, height = img.size

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            r = (r + key) % 256
            g = (g + key) % 256
            b = (b + key) % 256
            pixels[i, j] = (r, g, b)

    img.save("encrypted_image.png")
    print("Encryption complete. Saved as encrypted_image.png")

# Example usage
encrypt_image("sample.jpg", key=50)
