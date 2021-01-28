''' 
This is a sample that shows how to add, sub, and mult two ciphertext. 
First we will generate two messages, and encrypt them to ciphertext.
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
decryptor = heaan.Decryptor(context) 

# Step 3. Generating Messages
list_a = [i for i in range(100)] 
list_b = [i for i in range(0, 200, 2)] 

msg_a = heaan.Message(list_a) 
msg_b = heaan.Message(list_b) 

# Step 4. Encrypt Message to Ciphertext
ciphertext_a = heaan.Ciphertext() 
ciphertext_b = heaan.Ciphertext() 

encryptor.encrypt(msg_a, enc_key, ciphertext_a) 
encryptor.encrypt(msg_b, enc_key, ciphertext_b) 


def ctxt_basic(ciphertext_a, ciphertext_b) :

    ciphertext_add = heaan.Ciphertext() 
    ciphertext_sub = heaan.Ciphertext() 
    ciphertext_mult = heaan.Ciphertext()

    evaluator.add(ciphertext_a, ciphertext_b, ciphertext_add) 
    evaluator.sub(ciphertext_a, ciphertext_b, ciphertext_sub) 
    evaluator.mult(ciphertext_a, ciphertext_b, mult_key, ciphertext_mult)

    return ciphertext_add, ciphertext_sub, ciphertext_mult

def const_basic(ciphertext, const) :

    const_add = heaan.Ciphertext()
    const_sub = heaan.Ciphertext()
    const_mult = heaan.Ciphertext()
    evaluator.add(ciphertext, const, const_add)
    evaluator.sub(ciphertext, const, const_add)
    evaluator.mult(ciphertext, const, const_mult)

    return const_add, const_sub, const_mult

    
ciphertext_add, ciphertext_sub, ciphertext_mult = ctxt_basic(ciphertext_a, ciphertext_b)
const_add, const_sub, const_mult = const_basic(ciphertext_a, 1)

# Step 5. Decrypt Ciphertext to Message
decryptor = heaan.Decryptor(context)
message_ctxt_add = heaan.Message()
message_ctxt_sub = heaan.Message()
message_ctxt_mult = heaan.Message()
message_const_add = heaan.Message()
message_const_sub = heaan.Message()
message_const_mult = heaan.Message()

decryptor.decrypt(ciphertext_add, secret_key, message_ctxt_add)
decryptor.decrypt(ciphertext_sub, secret_key, message_ctxt_sub)
decryptor.decrypt(ciphertext_mult, secret_key, message_ctxt_mult)

decryptor.decrypt(const_add, secret_key, message_const_add)
decryptor.decrypt(const_sub, secret_key, message_const_sub)
decryptor.decrypt(const_mult, secret_key, message_const_mult)

print(message_ctxt_add)
print(message_ctxt_sub)
print(message_ctxt_mult)

print(message_const_add)
print(message_const_sub)
print(message_const_mult)









