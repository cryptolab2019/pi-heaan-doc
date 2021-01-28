# heaan.Message

*class* heaan.**Message**(data)

Message 클래스는 list 형태의 데이터를 인코딩하여 평문을 생성한다. 

### Input

- data : list

    암호화하고자는 데이터이다.

Examples

```python
>>> data = [1,2,3,4,5,6,7,8]
>>> msg = heaan.Message(data)
```