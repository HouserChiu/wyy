import execjs
from Crypto.Cipher import AES
import base64,codecs

#a函数

get_i=execjs.compile(r"""
    function a(a) {
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1)
            e = Math.random() * b.length,
            e = Math.floor(e),
            c += b.charAt(e);
        return c
    }
""")

#b函数
i=get_i.call('a',16)

def to_16(key):
    while len(key) % 16 != 0:
        key += '\0'
    return str.encode(key)
def AES_encrypt(text, key, iv):#text为密文，key为公钥，iv为偏移量
    bs = AES.block_size
    pad2 = lambda s: s + (bs - len(s) % bs) * chr(bs - len(s) % bs)
    encryptor = AES.new(to_16(key), AES.MODE_CBC,to_16(iv))
    encrypt_aes = encryptor.encrypt(str.encode(pad2(text)))
    encrypt_text = str(base64.encodebytes(encrypt_aes), encoding='utf-8')
    return encrypt_text

#params

g='0CoJUm6Qyw8W8jud'
def get_params(id,g):
    
    iv="0102030405060708"
    i=get_i.call('a',16)
    encText=str({'ids': "[" + str(id) + "]", 'br': 128000, 'csrf_token': ""})#i8a
    return AES_encrypt(AES_encrypt(encText,g, iv), i, iv)
#c函数
def RSA_encrypt(text, pubKey, modulus):
    text=text[::-1]
    rs=int(codecs.encode(text.encode('utf-8'), 'hex_codec'), 16) ** int(pubKey, 16) % int(modulus, 16)
    return format(rs, 'x').zfill(256)

#encseckey值
i=get_i.call('a',16)
b="010001"
c='00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
def get_encSecKey(i, b, c):
     return RSA_encrypt(i, b, c)


if __name__ == '__main__':
    print(c)
    print(RSA_encrypt(i, b, c))