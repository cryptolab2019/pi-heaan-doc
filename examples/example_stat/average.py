''' 
This is a sample that shows how to calculate average of ciphertext. 
First we will generate message, and encrypt it to ciphertext.
In this sample, homomorphic operation is performed in defined function.  

'''

import heaan 
import math

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

 
def ctxt_average(ciphertext, N) :

    for i in range(int(math.log(N, 2))) :
        ciphertext_tmp = heaan.Ciphertext()
        evaluator.left_rotate(ciphertext, 1 << i, public_key_pack, ciphertext_tmp)
        evaluator.add(ciphertext, ciphertext_tmp, ciphertext)
        pass

    ciphertext_avg = heaan.Ciphertext()
    evaluator.mult(ciphertext, 1.0 / N, ciphertext_avg)

    return ciphertext_avg


avg = ctxt_average(ciphertext_a, 128)

# Step 5. Decrypt Ciphertext to Message
decryptor = heaan.Decryptor(context)
message_result = heaan.Message()
decryptor.decrypt(avg, secret_key, message_result)

print(message_result)

