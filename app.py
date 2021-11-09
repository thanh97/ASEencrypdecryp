from flask import Flask, request, render_template
# import webbrowser
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random
import os
import codecs

app= Flask(__name__,static_url_path='/static')

def create_aes(password, iv):
    sha = SHA256.new()
    sha.update(password.encode('utf-8'))
    key = sha.digest()
    return AES.new(key, AES.MODE_CFB, iv)

def encrypt(data, password):
    iv = Random.new().read(AES.block_size)
    return iv + create_aes(password, iv).encrypt(data)

def decrypt(data, password):
    iv, cipher = data[:AES.block_size], data[AES.block_size:]
    return create_aes(password, iv).decrypt(cipher)
    
@app.route('/')
@app.route('/home', methods=['get'])
def home():
    return render_template('home.html')

@app.route('/encryp', methods=['POST', 'GET'])
def encrypFunctions():
    if request.method == 'POST':
        try:
            data = request.form['plaintext']
            password  = request.form['password']
            passwordConfirm = request.form['confirm']
            if password != passwordConfirm:
                templte_data = 'Confirmation password is incorrect!'
            else:
                with open('./datatmp/plaintext.txt', "w+", encoding="UTF-8") as f:
                        f.write(data)
                f.close()

                with open('./datatmp/plaintext.txt', 'r', encoding="UTF-8") as reader:
                    string_data = reader.read().encode("UTF-8")
                    encrypted_data = encrypt(string_data, password)
                    hex_data = codecs.encode(encrypted_data,'hex_codec')
                    with open('./datatmp/encrypt.txt', "wb+") as f:
                        f.write(hex_data)
                    f.close()
                reader.close()
                with open('./datatmp/encrypt.txt', 'r') as reader:
                    templte_data = reader.read()
                reader.close()
        except:
            print("An exception occurred")
    return render_template('home.html', encode_data=templte_data)

@app.route('/decryp', methods=['POST', 'GET'])
def decrypFunctions():
    if request.method == 'POST':
        try:
            data_request = request.form['plaintext2']
            password2  = request.form['password2']
            hex_data = codecs.decode(data_request, 'hex_codec')
            decrypted_data = decrypt(hex_data, password2)
            with open('./data/encrypt_out.txt', "wb+") as f:
                    f.write(decrypted_data)
            f.close()

            with open('.\data\encrypt_out.txt','r') as reader:
                decrypted_data_out = reader.read()
            reader.close()
        except:
            print('An error occurred during decryption execution, please try again')
    os.remove('./data/plaintext.txt')
    os.remove('./data/encrypt.txt')                
    os.remove('./data/encrypt_out.txt')
    return render_template('home.html', data2=decrypted_data_out)

if __name__ == "__main__":
  app.run(threaded=True, port=5000)