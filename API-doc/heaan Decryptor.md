# heaan.Decryptor

*class* heaan.**Decryptor**(context)

Decryptor 클래스는 복호화(Decryption)를 지원하는 메소드를 가지고 있다.

### Input

- context : heaan.Context()

    복호화에 필요한 파라미터를 저장하고 있는 컨텍스트이다.

Examples

```python
>>> dec = heaan.Decryptor(context)
```

### Method

- `decrypt`

    암호문을 메시지로 복호화한다. 

---

# METHODS

### heaan.Decryptor.decrypt

Decryptor.**decrypt**(ctxt, secret_key, dmsg)

암호문 ctxt를 복호화하여 메시지 dmsg로 저장한다.

### Input

- ctxt : heaan.Ciphertext()
- secret_key : heaan.SecretKey()
- dmsg : heaan.Message()

Examples

```python
### 키 생성
key_dir_path = "사용자 지정 경로"
new_path = "사용자 지정 경로"
params = heaan.Parameters()
context = heaan.Context(params)
secret_key = heaan.SecretKey(context)
keypack = heaan.PublicKeyPack(context, secret_key, key_dir_path)
enc_key = keypack.get_enc_key()

### 메시지 생성 및 암호화
msg = heaan.Message([1,2,3,4,5,6,7,8])
enc = heaan.Encryptor(context)
ctxt = heaan.Ciphertext()
enc.encrypt(msg, secret_key, ctxt)

### 복호화
dmsg = heaan.Message()
dec = heaan.Decryptor(context)
dec.decrypt(ctxt, secret_key, dmsg)
```