# from Crypto.Cipher import AES
# from Crypto.Hash import SHA256
# from Crypto import Random
# import os,sys


# def encrypt(data, password):
#     iv = Random.new().read(AES.block_size)
#     return iv + create_aes(password, iv).encrypt(data)

# def decrypt(data, password):
#     iv, cipher = data[:AES.block_size], data[AES.block_size:]
#     return create_aes(password, iv).decrypt(cipher)

# def create_aes(password, iv):
#     sha = SHA256.new()
#     sha.update(password.encode('UTF-8'))
#     key = sha.digest()
#     return AES.new(key, AES.MODE_CFB, iv)


# import base64
# import codecs
# text = 'The live Monster Grand Prix Token price today is 0034275 USD with a 24-hour trading volume of not available. We update our MGPX to USD price in real-time. Monster Grand Prix Token is down ,19 in the last 24 hours. The current CoinMarketCap ranking is, with a live market cap of not available. The circulating supply is not available and a max. supply of 500.000 MGPX coins.'
# pw = '123'


# # s1 = text.encode('utf-8', 'ignore')
# # encrypt_text = encrypt(s1, pw)

# # encrypt_text_new = encrypt_text.decode()
# # # encrypt_text_new = encrypt_text.decode('utf-8')
# # print(type(encrypt_text_new))


# # # # # # # encrypt_text_end = bytes(encrypt_text_new, 'ascii')

# # # # # # # de = encrypt_text_end.decode('ascii')
# # # # # # # print(type(de))
# # # # # # # print (type(encrypt_text_end))


# # decrypt_text = decrypt(encrypt_text_new.encode(), pw)
# # # print (decrypt_text)
# # # print (type(decrypt_text))

# # decrypt_text = decrypt_text.decode('utf-8')
# # print(decrypt_text);
# # file_text = 'vanban.txt'
# pathFile = 'vanban.txt'
# with open(pathFile, "w+", encoding="UTF-8") as f:
#     for i in text:
#         f.write(i)
# f.close()

# with open(pathFile, 'r', encoding="UTF-8") as reader:
#     string_data = reader.read().encode("UTF-8")
#     encrypted_data = encrypt(string_data, pw)

#     print(encrypted_data)

#     print ('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')

#     # for bytes in encrypted_data:
#     hex_data = codecs.encode(encrypted_data, 'hex')
#     # print(codecs.encode(encrypted_data, 'hex'))
#         # print(codecs.encode(bytes, 'hex'))
#     # print(hex_data)
#     with open('encrypt.txt', "wb+") as f:
#         f.write(hex_data)
#     f.close()
# reader.close()

# with open('encrypt.txt','rb') as reader:
#     try:
#         bytes_date = codecs.decode(reader.read(), 'hex_codec')
#         decrypted_data = decrypt(bytes_date, pw)
#         with open('decrypt.txt', "wb+") as f:
#             f.write(decrypted_data)
#         f.close()
#     except:
#             print(erro)
# reader.close()
