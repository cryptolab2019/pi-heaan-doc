''' 
This is a sample that shows how to rotate_sum ciphertext. 
First we will generate message, and encrypt it to ciphertext.
In this sample, homomorphic operation is performed in defined function.  

'''

class Pad :
    
    def __init__(self, num_slots) :
        
        self.num_slots = num_slots

    
    def _pad_x(self, num_slots_per_vec, idx) :
        # pad that the (idx_per_vec)-th slot in each vector is filled with 1, the other slots are 0
        
        pad = [0] * self.num_slots
        
        for i in range(self.num_slots) :
            if (idx % num_slots_per_vec) == idx :
                pad[idx] = 1

        return pad 

    def _pad_z(self, num_slots_per_vec, num_vectors, vector_idx) :
        # pad that the vector_idx-th vector is filled with 1, the other vectors are 0

        pad = [0] * self.num_slots

        for i in range(self.num_slots) :
            if((i // num_slots_per_vec) % num_vectors) == vector_idx :
                pad[i] = 1

        return pad 

    def _pad_y(self, n, d, vector_idx) :

        stripwidth = 2 ** vector_idx
        pad = [0] * self.num_slots

        for i in range(self.num_slots) :
            if (i < n*d) :
                if (i // (stripwidth * d)) % 2 == vector_idx :
                    pad[i] = 1

        return pad 



