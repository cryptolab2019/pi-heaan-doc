''' 
This is a sample that shows how to rotate_sum ciphertext. 
First we will generate message, and encrypt it to ciphertext.
In this sample, homomorphic operation is performed in defined function.  

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


class RotateCopy :

    def __init__(self, num_slots) : 
        
        self.num_slots = num_slots

    def _pad_x(self, num_slots_per_vec, idx) :
        # pad that the (idx_per_vec)-th slot in each vector is filled wtih 1, the other slots are 0
    
        pad = [0] * self.num_slots
        
        for i in range(self.num_slots) :
            if (idx % num_slots_per_vec) == idx :
                pad[idx] = 1

        return pad 
   
   
    def rotate_partial_sum(self, ciphertext, num_slots_per_vec):
        # sum all the slots per row and place it on the first slot
        
        ctxt_out = deepcopy(ciphertext)
        
        mask = heaan.Message(self._pad_x(num_slots_per_vec, 0))
        log_num_slots_per_vec = math.ceil(math.log2(num_slots_per_vec))
        ctxt_tmp = heaan.Ciphertext()
        
        for idx in range(int(log_num_slots_per_vec)):
            rot_idx = 2**idx
            evaluator.left_rotate(ctxt_out, rot_idx, public_key_pack, ctxt_tmp)
            evaluator.add(ctxt_out, ctxt_tmp, ctxt_out)

        evaluator.mult(ctxt_out, mask, mult_key, ctxt_out)

        return ctxt_out
