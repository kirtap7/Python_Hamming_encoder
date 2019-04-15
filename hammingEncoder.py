def hammingEncoder(bits):
    
    import math
    
    #check if argument is valid
    if not set(bits).issubset(('0', '1')) or len(bits)==0:
        return ('Error: Input must be binary!') 
    #check if number of bits is > 3 (minimum Humming distance is 3) 
    elif len(bits) < 4:
        return ('Error: Input must be at least 4 bits!') 
    else:
        #find number of extra bits using the formula 2^r ≥ m + r + 1 where, r = extra bit, m = data bit
        n=0
        while n < len(bits):
            if 2**n >= len(bits) + n + 1:
                extra_bits = n
                break
            else:
                n+=1
                
        #create new array that will store all the bits 
        encoded = ['*'] * (len(bits) + extra_bits)
        
        #insert empty spaces to corresponding parity bits position
        i = 0
        while i < extra_bits:
            #empty space every power of 2
            encoded[2**i - 1] = '_'
            i += 1
            
        #show current encoded list    
#         print (encoded, end="")
        
        #insert original bits in the new array
        # enc_index is the index of the encoded list and the first available position is at index 2
        enc_index = 2
        # orig_index is the index of the original code 
        orig_index = 0
        
        #use the number of extra_bits to find the powers of 2  
        for power in range (1,extra_bits):
            #set boundaries where to insert original bits
            lower = 2**power
            upper = 2**(power + 1) - 1

            # fill the other empty positions with the original bits    
            while enc_index >= lower and enc_index < upper and orig_index < len(bits):
                encoded[enc_index] = bits[orig_index]
                enc_index += 1
                orig_index += 1  
                
            enc_index += 1
            
        #show current encoded list 
#         print()
#         print (encoded, end="")                            
        
        
        ''' 
        Calculate and insert the parity bits in their position
        Following the algorithm https://en.wikipedia.org/wiki/Hamming_code
        Example:
        - Parity bit 1 covers all bit positions which have the least significant bit set:
        bit 1 (the parity bit itself), 3, 5, 7, 9, etc.
        - Parity bit 2 covers all bit positions which have the second least significant bit set: 
        bit 2 (the parity bit itself), 3, 6, 7, 10, 11, etc.
        ''' 
        
        #we use p to check the position which have the p least significant bit set
        for p in range (1,extra_bits+1):
            
            i = 0
            #initialize sum 
            sum = 0
            while i < len(encoded):
                #convert the index value in binary
                binary_index = bin(i+1)
                # check the binary index p least significant position and add its value to the sum
                if p < len(binary_index) and binary_index[-p] == '1' and encoded[i] != '_':
                    #cast the binary value to an int to obtain the sum in base 10
                    sum += int((encoded[i]))
                i += 1
            # the parity value is 0 if sum is even, 1 if sum is odd
            parity_value = sum % 2
            #add the parity value to its position
            encoded[2**(p-1)-1] = parity_value
            
        #show current encoded list 
#         print()
#         print (encoded, end="")
        
        #pass the list to a string to display the result
        result = ""
        for elem in encoded:
            result += str(elem)
        return result