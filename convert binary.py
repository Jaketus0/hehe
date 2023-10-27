def text_to_binary(text):
    binary = ' '.join(format(ord(char), '08b') for char in text)
    return binary

def binary_to_text(binary):
    text = ''.join(chr(int(char, 2)) for char in binary.split())
    return text

# Meminta input dari pengguna
input_choice = input("Pilih opsi (1: Text ke Binary\n 2: Binary ke Text): ")

if input_choice == "1":
    text_input = input("Masukkan teks yang ingin diubah menjadi biner: ")
    binary_output = text_to_binary(text_input)
    print("Hasil konversi ke biner: ", binary_output)
elif input_choice == "2":
    binary_input = input("Masukkan biner yang ingin diubah menjadi teks: ")
    text_output = binary_to_text(binary_input)
    print("Hasil konversi ke teks: ", text_output)
else:
    print("Pilihan tidak valid. Silakan pilih opsi 1 atau 2.")
