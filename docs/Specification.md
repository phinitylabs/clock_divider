# RC5 Documentation of the systemverilog RTL file **rc5_enc_dec_param.sv**

## Overview

Cryptography is the science of securing multimedia objects such as text, images, audio, and video by scrambling the original data. It includes two primary processes: encryption and decryption. Although cryptography is often applied to text, it can secure any type of digital data. Encryption transforms plaintext into ciphertext, while decryption reverses this process. The aim of encryption is to ensure data privacy, making it challenging for unauthorized users or intruders to access the original information. Cryptographic methods are broadly classified into symmetric and asymmetric ciphers. Symmetric ciphers use the same key for both encryption and decryption, whereas asymmetric ciphers use different keys for each process. Depending on whether the encryption processes data in large blocks or bit by bit, it can be categorized as a block cipher or a stream cipher, respectively. The RC5 algorithm is a symmetric block cipher known for its simplicity and effectiveness in converting plaintext to ciphertext and vice versa. It offers flexible options for adjusting block size, key size, and the number of encryption rounds. The RC5 algorithm employs operations such as modulo addition, left rotation, modulo subtraction, right rotation, and XOR in its encryption and decryption processes.

## Interface details

### RC5 encryption/decryption process

### Parameters

&nbsp;&nbsp;&nbsp;&nbsp; **Parameter 'w' for data width**\
&nbsp;&nbsp;&nbsp;&nbsp; **Parameter 'r' for specifying the number of rounds**

### Inputs:
•	**clock (1-bit)** : A single-bit input clock that drives the Finite State Machine executing the encryption algorithm. The clock typically has a 50:50 duty cycle.\
•	**reset (1-bit)**: A control signal that resets the internal states of the encryption system. Asynchronous active LOW reset has been used for both encryption and decryption modules\
•	**enc_start (1-bit)**: This is a 1-bit control signal which initiates the encryption process when it holds a logic HIGH\
•	**p_in (w-bits)[w-1:0]** : This is the plain text input for RC5 encryption, generally available in data widths of 16-bit, 32-bit, 64-bit, or 128-bits. Plaintext is processed in two segments of 'w/2' bits each, aligning with the algorithm’s requirements.\
•	**dec_start (1-bit)**: This is a 1-bit control signal which initiates the decryption process when it holds a logic HIGH\
•	**c_in (w-bits)[w-1:0]** : This is the cipher text input for RC5 decryption, generally available in data widths of 16-bit, 32-bit, 64-bit, or 128-bits. Ciphertext is processed in two segments of 'w/2' bits each, aligning with the algorithm’s requirements.\
•	**lfsr_seed_enc (8-bits)**: This is an 8-bit seed to be applied to LFSR for the generation of 8-bit keys to be used as S-box keys for encryption process\
•	**lfsr_seed_dec (8-bits)**: This is an 8-bit seed to be applied to LFSR for the generation of 8-bit keys to be used as S-box keys for decryption process

### Output:
•	**c_out (w-bits) [w-1:0]**: The output from the RC5 encryption algorithm. Like plaintext, ciphertext typically matches the input data width 'w'. When not in reset mode, the ciphertext is generated from the plaintext after a series of specific logical and arithmetic operations, dependent on the number of rounds 'r'.\
•	**p_out (w-bits) [w-1:0]** : The result of the RC5 decryption process, typically available in data widths matching the ciphertext. When not in reset mode, the plaintext is reconstituted from the ciphertext following a sequence of specified logical and arithmetic operations, contingent upon the number of decryption rounds 'r'.\
•   **enc_done (1-bit)**: This output marks the end of encryption and indicates the presence of stable cipher text output\
•   **dec_done (1-bit)**: This output marks the end of decryption and indicates the presence of stable plain text output


## Functionality

### RC5 Encryption algorithm

In order to understand the RC5 block cipher encryption, the following parameters are needed:
1. Plaintext (P)
2. Plaintext as w/2-bit registers (A & B)
2. Data width (w)
3. S-box key array (S)
4. Rounds of operation (r)
5. Ciphertext (C)

The RC5 encryption algorithm works as follows:

A = A + S[0];\
B = B + S[1];\
for i = 1 to r do\
&nbsp;&nbsp;&nbsp;&nbsp;A = ((A XOR B) <<< B) + S[2&times;i];\
&nbsp;&nbsp;&nbsp;&nbsp;B = ((B XOR A) <<< A) + S[(2&times;i)+1];\
C = {A,B}

Here, <<< : Left rotation; + : Modulo 2<sup>w</sup> addition; A : MSB w-bits of plaintext P;\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;B : LSB w-bits of plaintext P; S[0],S[1],S[2],....... : S-box keys ; {} : Concatenation

At the beginning of encryption, the MSB w-bits of plaintext is assumed as A and LSB w-bits of plaintext as B. Every step of this algorithm has to be carried out sequentially as the subsequent steps utilize the result of previous computations. Even though the encryption can be carried out on any data-width, the recommended plaintext widths are 16,32 or 64. The number of S-box keys for the encryption is 2*(r+1), where 'r' represents the number of rounds. As the number of rounds increases, the algorithm requires more number of S-box keys. In general, S-box keys are assumed by the user during the encryption process which need to be shared for executing the decryption.

### Key generation for encryption

Fibonacci configuration of 8-bit LFSR has to be utilized in this RTL design for generating s-box keys. It has been designed with a characteristic primitive polynomial of x<sup>8</sup>+x<sup>6</sup>+x <sup>5</sup>+x+1.Three XOR gates and 8 D Flip-Flops are required to construct this 8-bit LFSR. When the reset is at active LOW, the LFSR Flip-Flops will be initialized with the bits of the 8-bit initial seed (lfsr_seed_enc). When the reset is at active HIGH and during the positive edge of the clock, the 8-bit random sequence generation begins. The key generation module `lfsr_8bit.sv` has to be instantiated in `rc5_enc_dec_param.sv`.

### FSM-Controlled Process 

When the reset is LOW, state_enc should be initialized to 3'b000 and enc_done has to be maintained at zero. When enc_start is HIGH, the FSM has to begin the encryption process. The FSM orchestrates the encryption process, guiding the data through initial setup, S-box key generation, data transformation, and final output stages.

#### Detailed Analysis of the FSM Stages

1. S-box key generation (3'b000)

&nbsp;&nbsp;&nbsp;&nbsp;This state triggers the S-box key generation based on 8-bit LFSR. According to the number of rounds, the number of keys have to be generated. One clock cycle generates one 8-bit key. The LFSR keys should be based on lfsr_key_enc seed input.

2. Initial Addition (3'b001)

&nbsp;&nbsp;&nbsp;&nbsp;Using the S-box keys, the module performs initial modulo additions on the most significant and least significant halves of p_tmp, demonstrating the use of RC5's key mixing in the early stages.

3. Computation States (3'b010 and 3'b011)

&nbsp;&nbsp;&nbsp;&nbsp; These states handle the core of the RC5 encryption's mixing and data transformation, involving complex operations such as XORing, shifting, and modulo operations. State 3'b001 should handle MSB 8-bits computation wherein state 3'b010 should compute the LSB 8-bits. 

4. Final Assignment (3'b100)

&nbsp;&nbsp;&nbsp;&nbsp; The final encrypted data is assigned to the output c, and enc_done is set HIGH, signaling the completion of the encryption process.

### RC5 Decryption algorithm

In order to understand the RC5 block cipher decryption, the following parameters are needed:
1. Ciphertext (C)
2. Plaintext as w/2-bit registers (A & B)
2. Data width (w)
3. S-box key array (S)
4. Rounds of operation (r)
5. Plaintext (P)

The RC5 decryption algorithm works as follows:

for i = r down to 1 do\
&nbsp;&nbsp;&nbsp;&nbsp;B = ((B - S[(2&times;i)+1] >>> A) XOR A;\
&nbsp;&nbsp;&nbsp;&nbsp;A = ((A - S[(2&times;i)] >>> B) XOR B;\
B = B - S[1];\
A = A - S[0];\
P = {A,B}


Here, >>> : Right rotation; - : Modulo 2<sup>w</sup> subtraction; A : MSB w-bits of ciphertext C;\
B : LSB w-bits of ciphertext C; S[0],S[1],S[2],....... : S-box keys; {} : Concatenation

Decryption follows the reverse order of encryption. At the beginning of decryption, the MSB w-bits of ciphertext are considered as A and the LSB w-bits of ciphertext as B. Every step of this algorithm has to be carried out sequentially as the subsequent steps utilize the result of previous computations. Even though the decryption can be carried out on any data width, the recommended ciphertext widths are 16,32 or 64. The number of S-box keys for the decryption is 2*(r+1), where 'r' represents the number of rounds. As the number of rounds increases, more number of S-box keys are needed. In general, S-box keys will be shared for decryption by the entity that performed encryption due to the symmetric nature of block cipher. 


#### FSM-Controlled Process 

The FSM orchestrates the decryption process, guiding the data through initial setup, S-box key generation, data transformation, and final output stages.

### Key generation for decryption

Fibonacci configuration of 8-bit LFSR has to be utilized in this RTL design for generating s-box keys. It has been designed with a characteristic primitive polynomial of x<sup>8</sup>+x<sup>6</sup>+x <sup>5</sup>+x+1.Three XOR gates and 8 D Flip-Flops are required to construct this 8-bit LFSR. When the reset is at active LOW, the LFSR Flip-Flops will be initialized with the bits of the 8-bit initial seed (lfsr_seed_dec). When the reset is at active HIGH and during the positive edge of the clock, the 8-bit random sequence generation begins. The key generation module `lfsr_8bit.sv` has to be instantiated in `rc5_enc_dec_param.sv`.

### Detailed Analysis of the FSM Stages

1. Key Generation (3'b000)

&nbsp;&nbsp;&nbsp;&nbsp; S-box keys are generated and stored, which is fundamental for the decryption transformations.

2. Computation States (3'b001 to 3'b011)

&nbsp;&nbsp;&nbsp;&nbsp; These states handle the core decryption computations involving modular arithmetic and bitwise operations (XOR, shifts). The operations are reflective of the RC5 decryption methodology, handling data in parts and mixing it with the S-box keys.

3. Final Output and Reset (3'b100 to 3'b110)

&nbsp;&nbsp;&nbsp;&nbsp; The final states manage the loopback for multiple rounds and ultimately move the processed data into the output register once all rounds are complete. The final decrypted data is assigned to the output p, and dec_done is set HIGH, signaling the completion of the decryption process.

