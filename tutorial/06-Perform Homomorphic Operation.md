# Perform Homomorphic Operation

## Add and Multiply on ciphertexts

We need HomEvaluator while performing homomorphic operation on ciphertexts. For example, to add ciphertexts `ctxt1` and `ctxt2` as `ctxt_add`, run:

```python
>>> evaluator = heaan.HomEvaluator(context)
>>> ctxt_add = heaan.Ciphertext()
>>>
>>> evaluator.add(ctxt1, ctxt2, ctxt_add)
```

In case of specific operations, public key such as multiplication key is required. The following is to multiply ciphertexts `ctxt1` and `ctxt2` as `ctxt_mult`, which needs multiplication key.

```python
>>> mult_key = public_key.get_mult_key()
>>> ctxt_mult = heaan.Ciphertext()
>>>
>>> evaluator.mult(ctxt1, ctxt2, mult_key, ctxt_mult)
```

You may read API documentation for more information about homomorphic operations that require multiplication key.

## Compute ciphertext with message or constant

We can perform homomophic operations on ciphertext with message or constant. In this case, multiplication key is dispensable.

To add ciphertext `ctxt` and message `msg` as `ctxt_msg_add`, run:

```python
>>> ctxt_msg_add = heaan.Ciphertext()
>>> evaluator.add(ctxt, msg, ctxt_msg_add)
```

To multiply `ctxt` by 3 as `ctxt_const_mult`, run:

```python
>>> mult_const = 3
>>> ctxt_const_mult = heaan.Ciphertext()
>>> evaluator.mult(ctxt, mult_const, ctxt_const_mult)
```

## Rotate ciphertext

If we want to move the value within the ciphertext, we can use left_rotate or right_rotate

Rotating ciphertext means 

What does *"rotating ciphertext"* mean? 

To explain briefly, set a ciphertext `ctxt` with 8 slots as Figure 1.

![Message%20Create%20Block%20c13a936dc8604cb18ca3e2551832eb39/Untitled.png](Message%20Create%20Block%20c13a936dc8604cb18ca3e2551832eb39/Untitled.png)

Figure 1: ciphertext `ctxt` with 8 slots

While rotating `ctxt` to the left by 2, the values in `ctxt` move to the left, and the remaining values(

![Perform%20Homomorphic%20Operation%2089edc546e56848c786659262dca49bb8/Untitled.png](Perform%20Homomorphic%20Operation%2089edc546e56848c786659262dca49bb8/Untitled.png)

Figure 2: left-rotated `ctxt`

Also, the values in `ctxt` move to the right as follows while rotating `ctxt` to the right by 2.

![Perform%20Homomorphic%20Operation%2089edc546e56848c786659262dca49bb8/Untitled%201.png](Perform%20Homomorphic%20Operation%2089edc546e56848c786659262dca49bb8/Untitled%201.png)

Figure 3: right-rotated `ctxt`

```python
>>> rot_idx = 2
>>> ctxt_left_rot, ctxt_right_rot = heaan.Ciphertext(), heaa.Ciphertext()
>>> eval.left_rotate(ctxt, rot_idx, public_key, ctxt_rot)
>>> eval.right_rotate(ctxt1, rot_idx, public_key, ctxt_rot)
```

## Bootstrap ciphertext

```python
>>> eval.bootstrap(ctxt1, keypack, ctxt1)
```