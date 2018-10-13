import binascii
from Crypto.Cipher import AES


key1= binascii.unhexlify('140b41b22a29beb4061bda66b6747e14')
c1= binascii.unhexlify('4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81')
c1new=c1[16:]
iv1=c1[:16]
m1=AES.new(key1,AES.MODE_CBC,iv1)
print('m1:',m1.decrypt(c1new))


c2= binascii.unhexlify('5b68629feb8606f9a6667670b75b38a5b4832d0f26e1ab7da33249de7d4afc48e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253')
c2new=c2[16:]
iv2=c2[:16]
m2=AES.new(key1,AES.MODE_CBC,iv2)
print('m2:',m2.decrypt(c2new))

key2=binascii.unhexlify('36f18357be4dbd77f050515c73fcf9f2')
c3=binascii.unhexlify('69dda8455c7dd4254bf353b773304eec0ec7702330098ce7f7520d1cbbb20fc388d1b0adb5054dbd7370849dbf0b88d393f252e764f1f5f7ad97ef79d59ce29f5f51eeca32eabedd9afa9329')
iv3=c3[:16]
m3=b''
for item in range(16,len(c3),16):
        c3new=c3[item:item+16]
        m=AES.new(key2,AES.MODE_CTR,counter=lambda:iv3)
        x=m.decrypt(c3new)
        m3+=x
        
        iv3=binascii.unhexlify(hex((int.from_bytes(iv3, byteorder='big', signed=True)+1))[2:])
print('m3:',m3)

c4=binascii.unhexlify('770b80259ec33beb2561358a9f2dc617e46218c0a53cbeca695ae45faa8952aa0e311bde9d4e01726d3184c34451')
iv4=c4[:16]
m4=b''
for item in range(16,len(c4),16):
        c4new=c4[item:item+16]
        m=AES.new(key2,AES.MODE_CTR,counter=lambda:iv4)
        x=m.decrypt(c4new)
        m4+=x
        
        iv4=binascii.unhexlify(hex((int.from_bytes(iv4, byteorder='big', signed=True)+1))[2:])
print('m4:',m4)
