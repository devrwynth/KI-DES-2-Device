import socket
import DES

HOST = '139.228.87.9'  
PORT = 26800         

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    plaintext = input("Masukkan plaintext (panjang berapapun): ")
    encrypt_key = input("Masukan key untuk enkripsi: ")
    encrypt_rkb = DES.generate_rkb(encrypt_key)
    message_to_send = DES.des_encrypt_dynamic(plaintext, encrypt_rkb)

    s.sendall(message_to_send.encode('utf-8'))
    print("=== SENT ===")
    print(f"Plaintext: {plaintext}")
    print(f"Ciphertext (hex): {message_to_send}")

    print("Awaiting response from server...")

    data = s.recv(1024)
    reply = data.decode('utf-8')
    
    print("=== RECEIVED ===")
    print(f"Ciphertext (hex): {reply}")

    decrypt_key = input("Masukan key untuk dekripsi: ")
    decrypt_rkb = DES.generate_rkb(decrypt_key)
    decrypt_rkb_rev = decrypt_rkb[::-1]
    reply_deciphered = DES.des_decrypt_dynamic(reply, decrypt_rkb_rev)
    print(f"Deciphered Message: {reply_deciphered}")