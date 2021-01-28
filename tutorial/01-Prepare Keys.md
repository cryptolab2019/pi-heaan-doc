# Prepare Keys

## Create new keys

### Set up parameters

Firstly, we set up parameters and context for homomorphic encryption as below:

```python
>>> import heaan
>>> params = heaan.Parameters()
>>> context = heaan.Context(params)
```

### Generate keys

To generate secret key, run:

```python
>>> secret_key = heaan.SecretKey(context)
```

To generate public keys, run:

```python
>>> public_key_path = "./public_key_path"
>>> public_key_pack = heaan.PublicKeyPack(context, secret_key, public_key_path)
```

After generating a pack of public keys, those are stored in the directory `PK` under `public_key_path`, which consists of public keys such as...

- ConjKey : public key for conjugating ciphertext
- EncKey : public key for encrypting message
- MultKey : public key for multiplication of ciphertexts
- RotKey{rot_idx} : public key for rotating ciphertext by {rot_idx}

```python
./public_key_path
  └─ PK
     ├─ ConjKey.bin
     ├─ EncKey.bin
     ├─ MultKey.bin
     ├─ RotKey1.bin
     ├─ RotKey2.bin
     ├─ ...
     └─ RotKey655365.bin
```

While encrypting message or evaluating homomorphic operations, we get public keys as below:

```python
>>> conj_key = public_key_pack.get_conj_key()
>>> enc_key = public_key_pack.get_enc_key()
>>> mult_key = public_key_pack.get_mult_key()
```

### Save parameters and secret key

Parameters and secret key are able to be saved as binary files.

```python
>>> param_path = "./params.bin"
>>> params.save(param_path)
>>>
>>> secret_key_path = "./secretkey.bin"
>>> secret_key.save(secret_key_path)
```

## Load existing parameters and keys

To load existing parameters, run:

```python
>>> param_path = "./params.bin"
>>> params_new = heaan.Parameters()
>>> params_new.load(param_path)
>>> context_new = heaan.Context(params_new)
```

To load existing secret key, run:

```python
>>> secret_key_path = "./secretkey.bin"
>>> secret_key_new = heaan.SecretKey()
>>> secret_key_new.load(secret_key_path)
```

To load existing public keys, run:

```python
>>> public_key_path = "./public_key_path"
>>> public_key_pack_new = heaan.PublicKeyPack(context_new)
>>> public_key_pack_new.load(public_key_path)
```