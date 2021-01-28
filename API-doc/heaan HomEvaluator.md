# heaan.HomEvaluator

*class* heaan.**HomEvaluator**(context)

HomEvaluator 클래스는 암호문 연산을 지원하는 메소드들을 가지고 있다.  

### Input

- context : heaan.Context()

    암호문 연산에 필요한 파라미터를 저장하고 있는 컨텍스트이다. 

Examples

```python
>>> eval = HomEvaluator(context)
```

### Method

- `add`

    덧셈연산을 수행한다.

- `sub`

    뺄셈연산을 수행한다.

- `mult`

    곱셈연산을 수행한다.

- `left_rotate`

    암호문 블록의 슬롯을 왼쪽으로 이동한다.

- `right_rotate`

    암호문 블록의 슬롯을 오른쪽으로 이동한다.

- `divide_by_pow_of_two`

    암호문 블록의 모든 슬롯들을 2의 n 제곱으로 나누어준다.

- `square`

    암호문 블록의 모든 슬롯들을 제곱한다.

- `kill_imag`

    암호문 블록의 모든 슬롯들의 허수를 없앤다.

- `negate`

    암호문 블록의 모든 슬롯들에 -1을 곱한다. 

---

# METHODS

### heaan.HomEvaluator.add

HomEvaluator.**add**(ctxt, variable_, ctxt_result)

ctxt와 variable_을 더한 값을 ctxt_result에 저장한다. 

### Input

- ctxt : heaan.Ciphertext()
- variable_ : *optional*

    variable_의 자료형은 다음 중 하나이다.

    - heaan.Ciphertext()
    - heaan.Message()
    - constant - int, float(상수)
- ctxt_result : heaan.Ciphertext()

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
ctxt2 = heaan.Ciphertext()
enc.encrypt(msg, secret_key, ctxt)
enc.encrypt(msg, secret_key, ctxt2)

eval = heaan.HomEvaluator(context)

ctxt_add = heaan.Ciphertext()
msg_add = heaan.Ciphertext()
const_add = heaan.Ciphertext()
eval.add(ctxt, ctxt2, ctxt_add)
eval.add(ctxt, msg, ctxt_msg_add)
eval.add(ctxt, 2, ctxt_const_add)
```

---

### heaan.HomEvaluator.sub

HomEvaluator.**sub**(ctxt, variable_, result)

ctxt로부터 variable_을 뺄셈하여 result에 저장한다.

### Input

- ctxt : heaan.Ciphertext()
- variable_ : *optional*

    variable_의 자료형은 다음 중 하나이다.

    - heaan.Ciphertext()
    - heaan.Message()
    - constant - int, float(상수)
- result : heaan.Ciphertext()

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
ctxt2 = heaan.Ciphertext()
enc.encrypt(msg, secret_key, ctxt)
enc.encrypt(msg, secret_key, ctxt2)

eval = heaan.HomEvaluator(context)

ctxt_sub = heaan.Ciphertext()
msg_sub = heaan.Ciphertext()
const_sub = heaan.Ciphertext()
eval.sub(ctxt, ctxt2, ctxt_sub)
eval.sub(ctxt, msg, ctxt_msg_sub)
eval.sub(ctxt, 2, ctxt_const_sub)

```

---

### heaan.HomEvaluator.mult

HomEvaluator.**mult**(ctxt, variable_, *mult_key*, ctxt_mult)

ctxt와 variable_을 곱하여 result에 저장한다. 이 때, variable_의 자료형이 특별히 heaan.Ciphertext()일 경우 세번째 인수로 mult_key를 입력한다. 이 외의 경우에는 입력하지 않는다.

### Input

- ctxt : heaan.Ciphertext()
- variable_ : *optional*

    variable_의 자료형은 다음 중 하나이다.

    - heaan.Ciphertext()
    - heaan.Message()
    - constant - int, float(상수)
- mult-key : *optional*
- result : heaan.Ciphertext()

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

msg = heaan.Message([1,2,3,4,5,6,7,8])
enc = heaan.Encryptor(context)
ctxt = heaan.Ciphertext()
ctxt2 = heaan.Ciphertext()
enc.encrypt(msg, secret_key, ctxt)
enc.encrypt(msg, secret_key, ctxt2)

eval = heaan.HomEvaluator(context)

ctxt_mult = heaan.Ciphertext()
msg_mult = heaan.Ciphertext()
const_mult = heaan.Ciphertext()
eval.mult(ctxt, ctxt2, mult_key, ctxt_mult)
eval.mult(ctxt, msg, ctxt_msg_mult)
eval.mult(ctxt, 2, ctxt_const_mult)
```

---

### heaan.HomEvaluator.left_rotate

HomEvaluator.**left_rotate**(ctxt, rot_idx, keypack, result)

암호문 ctxt의 slot을 rot_idx만큼 왼쪽으로 이동하여 result에 저장한다. rot_idx는 $2^{n}$으로 제한한다.

### Input

- ctxt : heaan.Ciphertext()
- rot_idx : int, $2^n$
- keypack : heaan.PublicKeyPack()
- result : heaan.Ciphertext()

---

### heaan.HomEvaluator.right_rotate

HomEvaluator.**right_rotate**(ctxt, rot_idx, keypack, result)

암호문 ctxt의 slot을 rot_idx만큼 오른쪽으로 이동하여 result에 저장한다. rot_idx는 $2^{n}$으로 제한한다.

### Input

- ctxt : heaan.Ciphertext()
- rot_idx : int, $2^n$
- keypack : heaan.PublicKeyPack()
- result : heaan.Ciphertext()

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

### 메시지 생성
msg = heaan.Message([1,2,3,4,5,6,7,8])
enc = heaan.Encryptor(context)
ctxt = heaan.Ciphertext()
enc.encrypt(msg, secret_key, ctxt)

### 연산
eval = heaan.HomEvaluator(context)
ctxt_left_rotate = heaan.Ciphertext()
ctxt_right_rotate = heaan.Ciphertext()

eval.left_rotate(ctxt, 1, keypack, ctxt_left_rotate)
eval.right_rotate(ctxt, 1, keypack, ctxt_right_rotate)

```

---

### heaan.HomEvaluator.divide_by_pow_of_two

HomEvaluor.**divide_by_pow_of_two**(ctxt, bitsdiv, result)

암호문 ctxt를 $2^{bitsdiv}$으로 나누어 result로 저장한다. 

### Input

- ctxt : heaan.Ciphertext()
- bitsdiv : int
- result : heaan.Ciphertext()

---

### heaan.HomEvaluator.square

HomEvaluator.**square**(ctxt, mult_key, result)

암호문 ctxt를 제곱하여 result로 저장한다. (heaan.Ciphertext()를 제곱하는 것이므로 두 번째 인수로 mult_key를 입력한다.)

### Input

- ctxt : heaan.Ciphertext()
- mult_key : heaan.PublicKey()
- result : heaan.Ciphertext()

---

### heaan.HomEvaluator.kill_imag

HomEvaluator.**kill_imag**(ctxt, conj_key, result)

암호문 ctxt 의 허수를 없애고 result로 저장한다.

### Input

- ctxt : heaan.Ciphertext()
- conj_key : heaan.PublicKey()
- result : heaan.Ciphertext()

---

### heaan.HomEvaluator.negate

HomEvaluator.**negate**(ctxt, result)

암호문 ctxt에 -1을 곱하여 result로 저장한다.

### Input

- ctxt : heaan.Ciphertext()
- result : heaan.Ciphertext()

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

### 메시지 생성
msg = heaan.Message([1,2,3,4,5,6,7,8])
enc = heaan.Encryptor(context)
ctxt = heaan.Ciphertext()
ctxt2 = heaan.Ciphertext()
enc.encrypt(msg, secret_key, ctxt)

### 연산
eval = heaan.HomEvaluator(context)
ctxt_divide_by_pow_of_two = heaan.Ciphertext()
ctxt_square = heaan.Ciphertext()
ctxt_kill_imag = heaan.Ciphertext()
ctxt_negate = heaan.Ciphertext()

eval.divide_by_pow_of_two(ctxt, 1, ctxt_divide_by_pow_of_two)
eval.square(ctxt, mult_key, ctxt_square)
eval.kill_imag(ctxt, keypack, ctxt_kill_imag)
eval.negate(ctxt, ctxt_negate)

```