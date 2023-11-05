"""One-Time-Pad, verschlüsselte Datei, PNG-Datei, Schlüssel, Datei-Header, PNG-Dateiformat, Hex-Editor

Aufgabe: Untersuchen des verschlüsselten PNG-Datei-Headers im Zusammenhang mit einem One-Time-Pad.


Plan:

Verstehen Sie, wie ein One-Time-Pad funktioniert.
Erklären Sie, wie sich der wiederholte 8-Byte-Schlüssel auf die Verschlüsselung auswirkt.
Betonen Sie die Bedeutung des Datei-Headers in einem Dateiformat.
Die PNG-Datei beginnt normalerweise mit einem 8-Byte-Header. Da der Schlüssel in diesem Fall auf den gesamten Klartext angewendet wird,
könnten Sie feststellen,
dass der Datei-Header aufgrund der Wiederholung des Schlüssels Muster aufweist,
die in einer normalen PNG-Datei nicht vorhanden sind.
Dies könnte ein Hinweis darauf sein, wie Sie die Verschlüsselung brechen können.

Mögliche Vorgehensweise:

Untersuchen Sie den Datei-Header der verschlüsselten PNG-Datei.
Vergleichen Sie ihn mit dem Header unverschlüsselter PNG-Dateien.
Identifizieren Sie Muster oder Auffälligkeiten, die auf die Wiederholung des 8-Byte-Schlüssels hinweisen.
"""
from pathlib import Path

import binascii
# PNG-Dateiformat Header
# Erkennung von Dateiübertragungsproblemen ermöglicht: \211 P N G \r \n \032 \n ( 0x89504e470d0a1a0a )
# Eine PNG-Datei beginnt immer mit der folgenden, acht Byte langen Signatur (Magische Zahl):

#CONSTANTS
PNG_8_BIT_MAGIC_NUMBER_HEX = "89504e470d0a1a0a"
PNG_FILE_PATH = Path(__file__).parent / "files" / "encrypted.png"


def check_png_header(png: str, magic_number_hex: str):
    """
    Diese Funktion nimmt den Dateipfad als Eingabe und öffnet die Datei im Binärmodus.
    Sie liest die ersten 8 Bytes (den Header) der Datei und konvertiert sie in einen hexadezimalen String.
    Anschließend vergleicht sie diesen hexadezimalen Header mit der "magischen Zahl"
    Wenn der Header übereinstimmt, gibt die Funktion True zurück, andernfalls False.
    """
    #Öffnen der PNG  in Binär Modus
    with open(file=png, mode="rb") as png_file:
        # Lesen der ersten 8 bytes (header)
        header = png_file.read(8) 
        
    # Umwandeln des gelesen Bytes in Hexadezimalen String
    header_hex = binascii.hexlify(header).decode("UTF-8")
    print(header_hex)
    if header_hex == magic_number_hex:
        return True
    else:
        return False


if check_png_header(png=PNG_FILE_PATH, magic_number_hex=PNG_8_BIT_MAGIC_NUMBER_HEX):
    print("Die Datei ist eine gültige PNG-Datei.")
else:
    print("Die Datei ist keine gültige PNG-Datei oder der Header stimmt nicht überein.")



