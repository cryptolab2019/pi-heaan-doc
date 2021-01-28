''' 
This is a sample that shows how to rotate ciphertext. 
First we will generate message, and encrypt it to ciphertext.
In this sample, homomorphic operation is performed in defined function.  

'''

import heaan 

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


def ctxt_rotate(ciphertext, rot_idx) :

    ciphertext_leftrotate = heaan.Ciphertext()
    ciphertext_rightrotate = heaan.Ciphertext()

    evaluator.left_rotate(ciphertext, rot_idx, public_key_pack, ciphertext_leftrotate) # we left rotated ciphertext by rot_idx and saved the result to the ciphertext_leftrotate. 
    evaluator.right_rotate(ciphertext, rot_idx, public_key_pack, ciphertext_rightrotate)                                                                              # NOTE THAT rot_idx IS RESTRICTED BY POWER OF 2  
    
    return ciphertext_leftrotate, ciphertext_rightrotate



ciphertext_result_leftrotate, ciphertext_result_rightrotate = ctxt_rotate(ciphertext_a, 1) 

# Step 5. Decrypt Ciphertext to Message

decryptor = heaan.Decryptor(context)
message_result_leftrotate = heaan.Message()
message_result_rightrotate = heaan.Message()

decryptor.decrypt(ciphertext_result_leftrotate, secret_key, message_result_leftrotate)
decryptor.decrypt(ciphertext_result_rightrotate, secret_key, message_result_rightrotate)

print(message_result_leftrotate)
print(message_result_rightrotate)
