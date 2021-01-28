# Ciphertext: Encrypt, Save and Load

## Encrypt ciphertext

First of all, prepare a message to be encrypted.

```python
>>> message = heaan.Message([0.5, 2.3, 4.9, 10.2, 9.0, 5.2, 3.4, 8.6])
```

To encrypt the message as a Ciphertext instance by Encryptor, run:

```python
>>> encryptor = heaan.Encryptor(context)
>>> ciphertext = heaan.Ciphertext()
>>> enc_key = public_key.get_enc_key()
>>>
>>> encryptor.encrypt(message, enc_key, ciphertext)
```

Unlike message, the contents of ciphertext cannot be printed.

```python
>>> message      # can print the contents
[0.5, 2.3, 4.9, 10.2, 9.0, 5.2, 3.4, 8.6]
>>> ciphertext   # cannot print the contents
Traceback (most recent call last):
  ...
TypeError: ~~~~
```

To figure out the length of ciphertext (i.e. number of slots in the ciphertext), run:

```python
>>> ciphertext.get_number_of_slots()
8
>>> len(message)
8
```

## Save & Load ciphertext

To save ciphertext, run:

```python
>>> ciphertext_path = "./ciphertext.bin"
>>> ciphertext.save(ciphertext_path)
```

To load ciphertext, run :

```python
>>> ciphertext_path = "./ciphertext.bin"
>>> ciphertext_new = heaan.Ciphertext()
>>> ciphertext_new.load(ciphertext_path)
```