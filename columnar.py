import math

def encryption(columns, plaintext):
    ciphertext = ''
    rows = math.ceil(len(plaintext) / columns)
    fill = (rows * columns) - len(plaintext)

    columnar = list(plaintext)
    columnar.extend('X' * fill)

    for i in range(1, len(columnar) + 1):
        print(columnar[i - 1], end = ' ')
        if i % columns == 0:
            print()

    col = 0
    while (col < columns):
        ciphertext += columnar[col]

        i = col + columns
        for j in range(0, rows - 1): 
            ciphertext += columnar[i]
            i += columns
        
        col += 1
    
    return ciphertext

def decryption(columns, ciphertext):
    plaintext = ''
    rows = math.floor(len(ciphertext) / columns)

    columnar = []
    for i in range(columns):
        columnar += [[None] * rows]

    l = 0
    for i in range(0, columns):
        for j in range(0, rows):
            columnar[i][j] = ciphertext[l]
            l += 1

    print(columnar)

    for i in range(0, rows):
        for j in range(0, columns):
            print(columnar[j][i], end = ' ')
            plaintext += columnar[j][i]
        print()

    return plaintext

pt = input('Enter Plain Text: ')
c = int(input('Enter Columns: '))

print()

print('<--- ENCRYPTION --->')
ct = encryption(c, pt)
print('Cipher Text:', ct)

print()

print('<--- DECRYPTION --->')
pt = decryption(c, ct)
print('Plain Text:', pt)