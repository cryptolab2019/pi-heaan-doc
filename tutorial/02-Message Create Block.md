# Message: Create Block

pi-HEaaN performs encryption, decryption and homomorphic operations in *block units*. A single block consists of a maximum of 65,536(=$2^{16}$) *slots*. For example, the following figure is a block that consists of 8 slots.

![Message%20Create%20Block%20c13a936dc8604cb18ca3e2551832eb39/Untitled.png](Message%20Create%20Block%20c13a936dc8604cb18ca3e2551832eb39/Untitled.png)

We can generate block above as a Message instance.

```python
>>> message = heaan.Message([0.5, 2.3, 4.9, 10.2, 9.0, 5.2, 3.4, 8.6])
```

The message can be checked as below:

```python
>>> message
[0.5, 2.3, 4.9, 10.2, 9.0, 5.2, 3.4, 8.6]
>>> len(message)
8ㅅㅅ
```

Note that *list* is the only type of input for Message object.

```python
>>> message = heaan.Message(1,2,3,4)    # WRONG
Traceback (most recent call last):
  ...
TypeError: ~~~~
>>> message = heaan.Message([1,2,3,4])  # RIGHT
```