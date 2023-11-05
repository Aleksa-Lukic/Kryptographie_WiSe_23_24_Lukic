"""
**Lösung für das One-Time-Pad und den PNG-Datei-Header**

Dieses Programm untersucht einen verschlüsselten PNG-Datei-Header, der mit einem One-Time-Pad
verschlüsselt wurde. Es erklärt den Aufbau des PNG-Dateiformats und wie die Wiederholung des 8-Byte-Schlüssels
Muster im Header erzeugen kann, die in einer normalen PNG-Datei nicht vorhanden sind.
"""

from pathlib import Path
import binascii
import sys
# Erhöhen Sie die Ausgabebegrenzung, um die gesamte Tabelle anzuzeigen
sys.setrecursionlimit(20**6)



# Konstanten
PNG_8_BIT_MAGIC_NUMBER_HEX = "89504e470d0a1a0a"
PNG_FILE_PATH = Path(__file__).parent.parent / "files" / "encrypted.png"

def main():
    """
    Die Hauptfunktion, die den gesamten Untersuchungsprozess des PNG-Datei-Headers koordiniert.
    """
    # a) Untersuchen des Datei-Headers der verschlüsselten PNG-Datei
    check_png_header(PNG_FILE_PATH, PNG_8_BIT_MAGIC_NUMBER_HEX)

    # b) Beschreibung eines möglichen Angriffs auf die Verschlüsselung
    print("Ein möglicher Angriff könnte darin bestehen, dass der Schlüssel alle 8 Byte wiederholt wird,")
    print("was aufgrund der Wiederholung des Schlüssels Muster im Header erzeugen kann.")

    # c) Extrahieren des Schlüssels in hexadezimaler Form
    
def display_key_table_to_file(key_bytes, output_file):
    """
    Writes the key bytes to a table format in an output file.
    :param key_bytes: The bytes of the key.
    :param output_file: The output file where the table will be written.
    """
    hex_key = key_bytes.hex().upper()
    
    # Write the table header to the file
    output_file.write("Offset    Key Bytes\n")
    output_file.write("-------------------\n")
    
    # Write key bytes to the file in the table format
    for i in range(0, len(hex_key), 16):
        chunk = hex_key[i:i+16]
        offset = f"{i:08X}"
        output_file.write(f"{offset}  | {chunk}\n")

# Specify the output file
output_filename = "key_table.txt"

# Read the key from the encrypted PNG file
with open(PNG_FILE_PATH, 'rb') as file:
    key_bytes = file.read(8)

# Write the key table to the output file
with open(output_filename, 'w') as output_file:
    display_key_table_to_file(key_bytes, output_file)

print(f"The key table has been written to {output_filename}.")


def check_png_header(png: str, magic_number_hex: str):
    """
    Untersucht den Datei-Header der verschlüsselten PNG-Datei.
    :param png: Der Pfad zur verschlüsselten PNG-Datei
    :param magic_number_hex: Die magische Zahl des PNG-Dateiformats in hexadezimaler Form
    """
    with open(file=png, mode="rb") as png_file:
        header = png_file.read(8)
    
    header_hex = binascii.hexlify(header).decode("UTF-8")
    if header_hex == magic_number_hex:
        print("Die Datei ist eine gültige PNG-Datei.")
    else:
        print("Die Datei ist keine gültige PNG-Datei oder der Header stimmt nicht überein.")


def decrypt_file(filename, key):
    """
    Entschlüsselt eine Datei mit einem gegebenen Schlüssel.
    :param filename: Der Dateipfad zur verschlüsselten Datei
    :param key: Der Schlüssel in hexadezimaler Form
    :return: Die entschlüsselten Dateidaten
    """
    with open(filename, "rb") as f:
        file_contents = f.read()

    key_as_byte_array = binascii.unhexlify(key)
    file_contents_as_byte_array = bytearray(file_contents)

    decrypted_file_contents = bytearray()
    for i in range(len(file_contents_as_byte_array)):
        decrypted_byte = file_contents_as_byte_array[i] ^ key_as_byte_array[i % len(key_as_byte_array)]
        decrypted_file_contents.append(decrypted_byte)

    return bytes(decrypted_file_contents)


from PIL import Image

Image.LOAD_TRUNCATED_IMAGES = True  # Stelle sicher, dass abgeschnittene Bilder geladen werden

def load_png_image(filename):
    """
    Lädt ein PNG-Bild in ein 2D-Array von Pixelwerten.

    Args:
        filename: Der Pfad zur PNG-Datei.

    Returns:
        Ein 2D-Array von Pixelwerten.
    """
    with open(filename, "rb") as f:
        image = Image.open(f)

    return image.load()

encrypted_image = load_png_image(PNG_FILE_PATH)

def xor_image_with_key(image, key):
    """
    XORt ein Bild mit einem Schlüssel zusammen.

    Args:
        image: Das Bild.
        key: Der Schlüssel.

    Returns:
        Ein Array von XOR-Werten.
    """

    width, height = image.shape
    xored_image = []

    for i in range(width):
        for j in range(height):
            xored_image.append(image[i][j] ^ key)

    return xored_image

def convert_xor_values_to_rgb(xored_values):
    """
    Konvertiert XOR-Werte in RGB-Werte.

    Args:
        xored_values: Ein Array von XOR-Werten.

    Returns:
        Ein Array von RGB-Werten.
    """

    rgb_values = []

    for xor_value in xored_values:
        r = xor_value >> 0 & 0xFF
        g = xor_value >> 8 & 0xFF
        b = xor_value >> 16 & 0xFF

        rgb_values.append((r, g, b))

    return rgb_values

decrypted_image = load_png_image(Path(__file__).parent.parent / "files" / "de.png")

key = "1BE99071EDB42A3B"

xored_image = xor_image_with_key(encrypted_image, key)

rgb_values = convert_xor_values_to_rgb(xored_image)

for rgb_value in rgb_values:
    print(rgb_value)


if __name__ == "__main__":
    main()
