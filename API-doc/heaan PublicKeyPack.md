# heaan.PublicKeyPack

*class* heaan.**PublicKeyPack**(context, secret_key, key_dir_path)

PublicKeyPack 클래스는 암호화키와 연산키(곱셈키)를 생성한다.

### Input

- context : heaan.Context()

    암호화에 필요한 컨텍스트이다.

- secret_key : heaan.SecretKey()

    공개키 생성에 필요한 비밀키이다 

- key_dir_path : string

    공개키를 저장하는 경로이다.

Examples

```python
>>> keypack = heaan.PublicKeyPack(context, secret_key, key_dir_path)
```

### Method

- `get_enc_key`

    암호키를 불러온다.

- `get_mult_key`

    곱셈연산에 사용되는 키를 불러온다.

- `get_conj_key`

    복소수연산에 사용되는 키를 불러온다.

- `set_key_dir_path`

    지정한 공개키 경로를 변경한다.

- `get_key_dir_path`

    공개키가 저장된 경로를 불러온다.

---

# METHODS

### heaan.PublicKeyPack.get_enc_key

PublicKeyPack.**get_enc_key**()

암호화키를 불러온다.

### Return

- enc_key : heaan.PublicKeyPack()

---

### heaan.PublicKeyPack.get_mult_key

PublicKeyPack.**get_mult_key**()

곱셈연산에 사용되는 키를 불러온다.

### Return

- mult_key : heaan.PublicKeyPack()

---

### heaan.PublicKeyPack.get_conj_key

PublicKeyPack.**get_conj_key**()

복소수연산에 사용되는 키를 불러온다. 

### Return

- mult_key : heaan.PublicKey()

---

### heaan.PublicKeyPack.set_key_dir_path

PublicKeyPack.**set_key_dir_path**(new_*path = ' '*)

키가 저장된 기존 경로를 new_path로 바꾼다.

### Parameters

- new_path : string

---

### heaan.PublicKeyPack.get_key_dir_path

PublicKeyPack.**get_key_dir_path**()

키가 저장된 경로를 가져온다. 

### Returns

- path : string

    키가 저장된 경로이다.

Examples

```python
key_dir_path = "사용자 지정 경로"
new_path = "사용자 지정 경로"
params = heaan.Parameters()
context = heaan.Context(params)
secret_key = heaan.SecretKey(context)

keypack = heaan.PublicKeyPack(context, secret_key, key_dir_path)

enc_key = keypack.get_enc_key()
mult_key = keypack.get_mult_key()
keypack.set_dir_path(new_path)
get_path = keypack.get_key_dir_path()
```