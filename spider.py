import requests
import json
import base64
from Crypto.Cipher import AES
import codecs



headers = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'content-length': '484',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': '_iuqxldmzr_=32; _ntes_nnid=d38b06ca69f1f9a7f2c259ff7b83fcca,1575604264131; _ntes_nuid=d38b06ca69f1f9a7f2c259ff7b83fcca; WM_TID=TMvvx61idBRFFBAEEAMp%2FKbGMiIWs5Ks; mail_psc_fingerprint=757cd4b011b125973a9cd44fc24f8551; nts_mail_user=18391726137@163.com:-1:1; UM_distinctid=170b92f4432a5e-0a926f51021c42-4313f6a-1fa400-170b92f4433aa8; hb_MA-BFF5-63705950A31C_source=www.baidu.com; P_INFO=houserchiu@163.com|1584524451|0|mail163|00&99|sic&1569683648&mail163#sic&510100#10#0#0|183137&1|mail163|houserchiu@163.com; WM_NI=FUwqR058aOVDfcvbSaSdNDmcw0JI222mz9%2FvowIDE7HlAJ%2FZ%2BancMK2WtkhZ846ScsjOXYO6S%2F2ATMFM0GH3kBQh%2BAdoCla0fhTMPN2QPj5K4%2B3vxGdei55FzK9B6kMkc20%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeb8c74493ef8285bc73b8eb8ab2d85f968f9aabf45ea6aea4aacc3fad95fe86e62af0fea7c3b92a868bb992d13cf7e8afb0d550a6bdba83d26b91bc82a5f069b5f086aab13af2b3b6daae7eada987a5c83d8cb48fabae52e9bfa284d041f289bc8ceb52fcecfab4e279aa9198bace3e91f1fea2d747869300a8cb39a99e9f89aa4ba8b18d8de43ca6b89caed346f28fa08bb841f8f5fd97fb4da8bba7d6b84eba95f7a3b5618fb5add3b337e2a3; JSESSIONID-WYYY=JqKfwAXsT9F6%2Bv6CVV%2Bf1Gh2wB54OUx3HZKaeddUFdfh0KBdNUoIRUVhwxue%5Csyd8Nu3l%5CFGQCOuzEzsBYeVWd8ajQQomy5AfDhAqg%2BUko5nUh%5CSPuxm58FsxidQsiBPXHKn32Hh9ER%2FgCY5P8kU5aAjqebauikxeqbZ62fedkhIukKb%3A1584848298242',
    'origin': 'https://music.163.com',
    'referer': 'https://music.163.com/user/home?id=50359783',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
}
url = "https://music.163.com/weapi/user/getfolloweds?csrf_token="


params_first = '{"userId":"50359783","offset":"0","total":"true","limit":"20","csrf_token":""}'
params_second = "010001"
params_third = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
params_forth = "0CoJUm6Qyw8W8jud"


# params需要第一个参数和第四个参数
# encSecKey需要第二个和第三个参数，还需要一个随机的16个字符组成的字符串

def aesEncrypt(text, key):
     # 偏移量
     iv = '0102030405060708'
     # 文本
     pad = 16 - len(text) % 16
     text = text + pad * chr(pad)
     encryptor = AES.new(key, 2, iv)
     ciphertext = encryptor.encrypt(text)
     ciphertext = base64.b64encode(ciphertext)
     return ciphertext


def get_params(text):
     # 第一个参数
     params = aesEncrypt(params_first, params_forth).decode('utf-8')
     params = aesEncrypt(params, text)
     return params

def rsaEncrypt(pubKey, text, modulus):
     '''进行rsa加密'''
     text = text[::-1]
     rs = int(codecs.encode(text.encode('utf-8'), 'hex_codec'), 16) ** int(pubKey, 16) % int(modulus, 16)
     return format(rs, 'x').zfill(256)


def get_encSEcKey(text):
    pubKey = params_second
    moudulus = params_third
    encSecKey = rsaEncrypt(pubKey, text, moudulus)
    return encSecKey

text = "A"*16
params = get_params(text)
encSecKey = get_encSEcKey(text)
formdata = {
    "params": params,
    "encSecKey": encSecKey
}


temp_data = json.loads(requests.post(url, data=formdata, headers=headers).content)['followeds']
for eve_data in temp_data:
    print(eve_data['userId'])