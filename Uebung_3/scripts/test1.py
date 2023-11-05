from PIL import Image
from pathlib import Path

FILES_DIRECTORY = Path(__file__).parent.parent / "files"
ENCRYPTED_FILE = FILES_DIRECTORY / "encrypted.png"
DEENCRYPTED_FILE = FILES_DIRECTORY / "decrypted.png"

BLOCK_SIZE = 8

def extract_key_blocks(image_path):
    with open(image_path, "rb") as f:
        image_data = f.read()
    
    key_blocks = []
    for i in range(0, len(image_data), BLOCK_SIZE):
        key_block = image_data[i:i + BLOCK_SIZE]
        key_blocks.append(key_block)
    
    return key_blocks

def extract_key(image_path):
    key_blocks = extract_key_blocks(image_path)
    
    if len(key_blocks) < 2:
        raise ValueError("Not enough key blocks")
    
    key = key_blocks[0] + key_blocks[1]
    return key

def decrypt_file(filename, key):
    with open(filename, "rb") as f:
        file_contents = f.read()

    key_as_hex = key.hex()  # Wandele den Schlüssel in einen Hexadezimal-String um
    key_as_byte_array = bytes.fromhex(key_as_hex)
    file_contents_as_byte_array = bytearray(file_contents)

    decrypted_file_contents = bytearray()
    for i in range(len(file_contents_as_byte_array)):
        decrypted_byte = file_contents_as_byte_array[i] ^ key_as_byte_array[i % len(key_as_byte_array)]
        decrypted_file_contents.append(decrypted_byte)

    return bytes(decrypted_file_contents)

def main():
    try:
        key = extract_key(ENCRYPTED_FILE)
    except ValueError as e:
        print(f"Error extracting key: {e}")
        return
    
    decrypted_file_contents = decrypt_file(ENCRYPTED_FILE, key)
    
    with open(DEENCRYPTED_FILE, "wb") as f:
        f.write(decrypted_file_contents)
        
    
    # Laden und Anzeigen des entschlüsselten Bilds in RGB
    decrypted_image = Image.open(DEENCRYPTED_FILE)
    decrypted_image.save("decrypted.png", format="PNG")
    decrypted_image.show()

if __name__ == "__main__":
    main()
