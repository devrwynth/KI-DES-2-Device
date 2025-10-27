import socket
import DES

HOST = '192.168.0.101'  #IP local server
PORT = 26800      

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Server listening on {HOST}:{PORT}")
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            message = data.decode('utf-8')
            
            print(f"=== RECEIVED ===")
            print(f"Ciphertext (hex): {message}")
            
            decrypt_key = input("Masukan key untuk dekripsi: ")
            decrypt_rkb = DES.generate_rkb(decrypt_key)
            decrypt_rkb_rev = decrypt_rkb[::-1]

            message_deciphered = DES.des_decrypt_dynamic(message, decrypt_rkb_rev)

            print(f"Deciphered Message: {message_deciphered}")

            reply = input("Masukan reply plaintext: ")
            encrypt_key = input("Masukan key untuk enkripsi: ")
            encrypt_rkb = DES.generate_rkb(encrypt_key)
            reply_cipher = DES.des_encrypt_dynamic(reply, encrypt_rkb)
            print(f"=== SENT ===")
            print(f"Plaintext: {reply}")
            print(f"Ciphertext (hex): {reply_cipher}")
            conn.sendall(reply_cipher.encode('utf-8'))