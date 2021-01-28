# heaan.Encryptor

*class* heaan.**Encryptor**(context)

Encryptor 클래스는 암호화 메소드를 가지고 있다. 

### Input

- context : heaan.Context()

    메시지 암호화에 필요한 파라미터를 저장하고 있는 컨텍스트이다.

Examples

```python
>>> enc = heaan.Encryptor(context)
```

### Method

- `encrypt`

    메시지를 암호화한다. 

---

# METHODS

### heaan.Encryptor.encrypt

Encryptor.encrypt(msg, enc_key, ctxt)

첫번째 인수로 메시지 msg를 받아 두번째 인수인 암호화키를 사용하여 암호화하고 세번째 인수인 암호문으로 암호화한다. 

### Input

- msg : heaan.Message()

    암호화할 메시지이다.

- enc_key : heaan.PublicKey()

    암호화키이다.

- ctxt : heaan.Ciphertext()

    메시지를 암호화한 암호문이다.

Examples

```python
key_dir_path = "사용자 지정 경로"
new_path = "사용자 지정 경로"
params = heaan.Parameters()
context = heaan.Context(params)
secret_key = heaan.SecretKey(context)

keypack = heaan.PublicKeyPack(context, secret_key, key_dir_path)
enc_key = keypack.get_enc_key()

msg = heaan.Message([1,2,3,4,5,6,7,8])
enc = heaan.Encryptor(context)
ctxt = heaan.Ciphertext()
enc.encrypt(msg, secret_key, ctxt)
```