# Decrypt Ciphertext

In the previous section, we find that the contents of ciphertext cannot be seen.

```python
>>> message = heaan.Message([1,2,3,4])
>>> encryptor.encrypt(message, enc_key, ciphertext)
>>> ciphertext   # cannot print the contents
Traceback (most recent call last):
  ...
TypeError: ~~~~
```

To figure out what ciphertext has, we have to decrypt the ciphertext by Decryptor.

```python
>>> decryptor = heaan.Decryptor(context)
>>> message_out = heaan.Message()
>>>
>>> decryptor.decrypt(ciphertext, secret_key, message_out)
```

Note that the result of operation performed on ciphertext is not exactly the same as the result performed on message. This tiny and random error comes from *approximation operation*, which is the essence of HEAAN.

```python
>>> message
[1, 2, 3, 4]
>>> message_out   # i.e. decrypt(encrypt(message))
[1.0, 2.0, 2.9999999990686774, 3.9999999990686774]
```