# heaan.Ciphertext

*class* heaan.**Ciphertext**()

Ciphertext 클래스는 암호 객체를 생성 및 저장하고 불러오기 위해 만들어졌다. 메시지를 암호화하여 변수로 사용하기 위해서는 암호화 이전에 암호문으로 사용할 변수의 자료형을 반드시 heaan.Ciphertext로 설정해야 한다. 

Examples

```python
>>> ctxt = heaan.Ciphertext()
```

### Method

- `save`

    암호문을 사용자가 지정하는 경로에 저장한다.

- `load`

    암호문을 사용자가 지정한 경로로부터 불러온다. 

- `check_parameters`

    부트스트랩 실행의무 여부를 확인한다.

---

METHODS

### heaan.Ciphertext.save

Ciphertext.**save**(*path = ' '*) 

암호문을 경로에 저장한다.

### Input

- path : string

    암호문을 저장할 경로이다.

---

### heaan.Ciphertext.load

Ciphertext.**load**(*path = ' '*) 

암호문을 경로로부터 불러온다.

### Input

- path : string

    암호문을 불러오는 경로이다. 

---

### heaan.Ciphertext.check_parameters

Ciphertext.**check_parameters**() 

부트스트랩 실행의무 여부를 확인할 수 있다.

Examples

```python
PATH = "사용자 지정 경로"
ctxt = heaan.Ciphertext()
ctxt.save(PATH)
ctxt.load(PATH)
ctxt.check_parameters()
```