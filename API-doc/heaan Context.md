# heaan.Context

*class* heaan.**Context**(params)

클래스 Context(컨텍스트)를 통해 생성되는 컨텍스트 객체는 파라미터 저장, 알고리즘의 시간복잡도 계산?을 수행한다. 암호문의 부트스트랩을 가능하도록 하는 메소드를 가지고 있다.

### Input

- params : heaan.Parameters()

    컨텍스트 생성에 필요한 파라미터 객체이다. 

Examples

```python
>>> context = heaan.Context(params)
```

### Method

- `make_bootstrappable`

    암호문을 부트스트랩 할 수 있도록 한다.

---

# METHODS

### heaan.Context.make_bootstrappable

Context.make_bootstrappable(log_slots)

부트스트랩이 가능하도록 한다.

### Input

- log_slots : 16, 고정값

    암호문이 사용할 수 있는 최대 슬롯의 수로 65536에 대해 2를 밑으로 하는 로그값이다. 

Examples

```python
params = heaan.Parameters()
log_slots = 16
context = heaan.Context(params)
context.make_bootstrappable(log_slots)
```