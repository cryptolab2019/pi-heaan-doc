# heaan.SecretKey

*class* heaan.**SecretKey**(context)

SecretKey 클래스는 암호문을 복호화(Decryption)하는 데 사용하는 비밀키를 생성한다. 

### Input

- context : heaan.Context()

    비밀키 생성에 필요한 파라미터를 저장하고 있는 컨텍스트이다. 

Examples

```python
>>> secret_key = heaan.SecretKey(context)
```

### Method

- `save`

    비밀키를 사용자가 지정한 경로에 저장한다.

- `load`

    저장되어 있는 비밀키를 해당 경로로부터 불러온다.

---

# METHODS

### heaan.SecretKey.save

SecretKey.**save**(context, path = ' ')

비밀키를 사용자가 지정하는 경로에 저장한다. 

### Input

- context : heaan.Context()
- path : string

    비밀키를 저장할 경로이다.

---

### heaan.SecretKey.load

SecretKey.load(context, path = ' *'*)

비밀키를 사용자가 지정하는 경로부터 불러온다. 

### Input

- context : heaan.Context()
- path : string

    비밀키가 저장되어있는 경로이다.

Examples

```python
PATH = "사용자 지정 경로"
params = heaan.Parameters()
context = heaan.Context(params)
secret_key = heaan.SecretKey(context)

secret_key.save(context, path)
secret_key.load(context, path) 
```