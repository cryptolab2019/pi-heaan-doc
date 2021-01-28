# heaan.Parameters

*class* heaan.**Parameters**()

클래스 Parameters는 동형암호 연산에 필요한 파라미터 객체를 생성한다.

Examples

```jsx
>>> params = heaan.Parameters()
```

### Method

- `save`

    파라미터를 사용자가 지정하는 경로에 저장한다.

- `load`

    저장되어 있는 파라미터를 해당 경로로부터 불러온다.

---

# METHODS

### heaan.Parameters.save

Parameters.**save**(*path = ' '*)

파라미터를 path에 저장한다.

### Input

- path : string

    파라미터를 저장할 경로이다.

---

### heaan.Parameters.load

Parameters.**load**(*path = ' '*)

저장되어 있는 파라미터를 해당 경로로부터 불러온다.

### Input

- path : string

    불러올 파라미터가 저장되어 있는 경로이다.

Examples

```python
PATH = "사용자 지정 경로"
params = heaan.Parameters()
params.save(PATH)
params.load(PATH)
```