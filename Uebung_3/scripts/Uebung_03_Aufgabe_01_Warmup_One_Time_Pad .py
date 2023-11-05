"""
**Lösung für das Warm-up: One-Time-Pad**

Dieses Programm entschlüsselt den gegebenen Ciphertext c mit dem angegebenen Schlüssel k.
Der Ciphertext c ist ein UTF-8-String mit sieben Zeichen, und die Aufgabe besteht darin, 
die Entschlüsselung exemplarisch durchzuführen, Bit für Bit, und den Klartext in hexadezimaler 
und dekodierter Form auszugeben.

Hinweis: UTF-8 ist eine Zeichenkodierung, bei der jedes Zeichen durch 8 Bit kodiert ist. 
Die Dekodierung erfolgt entsprechend, um den Klartext zu erhalten.
"""

# Schritt 1: Konvertieren der Hexadezimalzahlen c und k in Binärzahlen

def main():
    """
    Die Hauptfunktion, die den gesamten Entschlüsselungsprozess koordiniert.
    """
    c = 0x26c5be19df5cdd
    k = 0x63abca6bb02ca4

    # Konvertierung der Hexadezimalzahlen in Binärzahlen
    c_binary = bin(c)[2:]
    k_binary = bin(k)[2:]

    # Schritt 2: Durchführung der XOR-Operation zwischen den beiden Binärzahlen
    xor_result_binary = xor_operation(c_binary, k_binary)

    # Schritt 3: Konvertierung des XOR-Ergebnisses zurück in Hexadezimal und Dekodierung
    result_hex = hex(int(xor_result_binary, 2))
    decoded_text = decode_utf8(result_hex)

    # Ausgabe des Klartexts in hexadezimaler und dekodierter Form
    print("Klartext in hexadezimaler Form:", result_hex)
    print("Dekodierter Klartext:", decoded_text)

def xor_operation(c:str, k:str):
    """
    Führt eine XOR-Operation zwischen den beiden Binärzahlen c und k durch.
    :param c: Der Binärstring des Ciphertexts
    :param k: Der Binärstring des Schlüssels
    :return: Das Ergebnis der XOR-Operation als Binärstring
    """
    max_len = max(len(c), len(k))
    c = c.zfill(max_len)
    k = k.zfill(max_len)
    
    result = ""
    
    for i in range(max_len):
        result += str((int(c[i]) + int(k[i])) % 2)
        
    return result

def decode_utf8(hex_string):
    """
    Dekodiert eine Hexadezimalzeichenfolge in UTF-8 und gibt den Klartext zurück.
    :param hex_string: Die Hexadezimalzeichenfolge
    :return: Der dekodierte Klartext als Zeichenfolge
    """
    decoded_text = bytearray.fromhex(hex_string[2:]).decode('utf-8')
    return decoded_text

if __name__ == "__main__":
    main()
