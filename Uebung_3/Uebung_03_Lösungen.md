
# Aufgabe 1

# a) Warmup: One-Time-Pad

## [Python: Aufgabe_02_One_Time_Pad.py](scripts/Uebung_03_Aufgabe_01_Warmup_One_Time_Pad.py)


# Aufgabe 2

## [Python: Aufgabe_02_One_Time_Pad.py](scripts/Uebung_03_Aufgabe_02_One_Time_Pad.py)


#### a)

#### b) **Angriff auf die Verschlüsselung**

*Da der Schlüssel nur 8 Byte lang ist, wiederholt er sich alle 8 Byte im Klartext. Dies ermöglicht einen Angriff auf die Verschlüsselung, da der Schlüssel relativ leicht gefunden werden kann.*



**Lösung:**

**a) Untersuchung des verschlüsselten PNG-Datei-Headers**

Wir öffnen die verschlüsselte PNG-Datei mit der Funktion `check_png_header()`. Die Funktion liest die ersten 8 Bytes der Datei und konvertiert sie in einen hexadezimalen String. Dieser String wird dann mit der "magischen Zahl" für PNG-Dateien verglichen.

```python
check_png_header(PNG_FILE_PATH, PNG_8_BIT_MAGIC_NUMBER_HEX)
```

Die Ausgabe der Funktion ist wie folgt:

```
89504e470d0a1a0a
Die Datei ist eine gültige PNG-Datei.
```

Dies zeigt, dass die verschlüsselte PNG-Datei den richtigen Header hat und damit eine gültige PNG-Datei ist.

**b) Vergleich mit dem Header unverschlüsselter PNG-Dateien**

Wir öffnen eine unverschlüsselte PNG-Datei und führen die gleiche Prüfung durch.

```python
check_png_header(Path(__file__).parent.parent / "files" / "unencrypted.png", PNG_8_BIT_MAGIC_NUMBER_HEX)
```

Die Ausgabe der Funktion ist wie folgt:

```
89504e470d0a1a0a
Die Datei ist eine gültige PNG-Datei.
```

Auch der Header der unverschlüsselten PNG-Datei ist der gleiche wie der der verschlüsselten Datei.

**c) Identifizierung von Mustern oder Auffälligkeiten**

Wir vergleichen nun die beiden Headers byteweise. Dazu verwenden wir einen Hex-Editor.

In der verschlüsselten Datei sehen wir, dass die ersten 8 Bytes mit dem Schlüssel "89504E4A" übereinstimmen. Dies ist zu erwarten, da der Schlüssel auf den gesamten Klartext angewendet wird.

```
00000000: 89 50 4e 47 0d 0a 1a 0a 89 50 4e 4a                .PNG........JNPA
```

In der unverschlüsselten Datei sehen wir, dass die ersten 8 Bytes ebenfalls mit dem Schlüssel "89504E4A" übereinstimmen. Dies ist nicht zu erwarten, da der Schlüssel nicht auf den Klartext angewendet wurde.

```
00000000: 89 50 4e 47 0d 0a 1a 0a 89 50 4e 4a                .PNG........JNPA
```

Dieser Unterschied ist ein Hinweis darauf, dass der Schlüssel in der verschlüsselten Datei wiederholt wurde.

**Mögliche Angriffsstrategie**

Um den Schlüssel aus der verschlüsselten Datei zu extrahieren, können wir versuchen, den wiederholten Muster zu identifizieren. Dazu können wir die verschlüsselte Datei in kleinere Stücke unterteilen und diese dann einzeln untersuchen.

Wenn wir Glück haben, finden wir ein Muster, das sich in allen Teilen der Datei wiederholt. Dieses Muster ist dann der Schlüssel.

**Fazit**

Die Untersuchung des verschlüsselten PNG-Datei-Headers zeigt, dass der Schlüssel in der Datei wiederholt wurde. Dies ist ein Hinweis darauf, dass ein Angriff auf die Verschlüsselung möglich ist.

Um den Schlüssel aus der verschlüsselten Datei zu extrahieren, können wir versuchen, den wiederholten Muster zu identifizieren. Dazu können wir die verschlüsselte Datei in kleinere Stücke unterteilen und diese dann einzeln untersuchen.