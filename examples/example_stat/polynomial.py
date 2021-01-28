''' 
This is a sample that shows how to calculate polynomial of ciphertext. 
First we will generate message, and encrypt it to ciphertext.
In this sample, homomorphic operation is performed in defined function.  
This sample's polynomial is 5x^4 + 4x^3 + 3x^2 + 2x + 1. 

'''

import heaan 
import math
from copy import deepcopy

# Step 1. Setting Parameters
params = heaan.Parameters() 
context = heaan.Context(params)

# Step 2. Generating Keys
secret_key = heaan.SecretKey(context) 
public_key_path = "./public_key_path" 
public_key_pack = heaan.PublicKeyPack(context, secret_key, public_key_path) 

conj_key = public_key_pack.get_conj_key() 
enc_key = public_key_pack.get_enc_key() 
mult_key = public_key_pack.get_mult_key() 
encryptor = heaan.Encryptor(context) 
evaluator = heaan.HomEvaluator(context) 

# Step 3. Generating Messages
_list = [i for i in range(128)] 
msg = heaan.Message(_list) 

# Step 4. Encrypt Message to Ciphertext
ciphertext_a = heaan.Ciphertext() 
encryptor.encrypt(msg, enc_key, ciphertext_a) 


def poly(ciphertext) :
    
    coeff = [1, 2, 3, 4, 5]
    result = heaan.Ciphertext()
    
    ciphertext_tmp0 = deepcopy(ciphertext)
    ciphertext_tmp1 = heaan.Ciphertext()
    ciphertext_tmp2 = heaan.Ciphertext()
    ciphertext_result = heaan.Ciphertext()

    for index, value in enumerate(coeff) :
        
        if index == 0 :
            
            coeff_zero = value
            
        elif index == 1 :
            evaluator.mult(ciphertext, value, ciphertext_tmp1)
            
        else : 
            evaluator.mult(ciphertext, ciphertext_tmp0, mult_key, ciphertext_tmp0)
            evaluator.mult(ciphertext_tmp0, value, ciphertext_tmp2)
            
            evaluator.add(ciphertext_tmp1, ciphertext_tmp2, ciphertext_tmp1)
            
    evaluator.add(ciphertext_tmp1, coeff_zero, ciphertext_result)
            
        
    return ciphertext_result


poly_result = poly(ciphertext_a)

# Step 5. Decrypt Ciphertext to Message

# decryptor = heaan.Decryptor(context)
# message_result = heaan.Message()
# decryptor.decrypt(poly_result, secret_key, message_result)

# print(message_result)
print(context)
