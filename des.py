# initial_perm table
initial_perm_table = [58, 50, 42, 34, 26, 18, 10, 2,
                60, 52, 44, 36, 28, 20, 12, 4,
                62, 54, 46, 38, 30, 22, 14, 6,
                64, 56, 48, 40, 32, 24, 16, 8,
                57, 49, 41, 33, 25, 17, 9, 1,
                59, 51, 43, 35, 27, 19, 11, 3,
                61, 53, 45, 37, 29, 21, 13, 5,
                63, 55, 47, 39, 31, 23, 15, 7]



# initial key table
inital_key_table = [57, 49, 41, 33, 25, 17, 9,
                1, 58, 50, 42, 34, 26, 18,
                10, 2, 59, 51, 43, 35, 27,
                19, 11, 3, 60, 52, 44, 36,
                63, 55, 47, 39, 31, 23, 15,
                7, 62, 54, 46, 38, 30, 22,
                14, 6, 61, 53, 45, 37, 29,
                21, 13, 5, 28, 20, 12, 4]



# Expansion D-box Table

exp_d_table = [32, 1, 2, 3, 4, 5, 4, 5,
        6, 7, 8, 9, 8, 9, 10, 11,
        12, 13, 12, 13, 14, 15, 16, 17,
        16, 17, 18, 19, 20, 21, 20, 21,
        22, 23, 24, 25, 24, 25, 26, 27,
        28, 29, 28, 29, 30, 31, 32, 1]



# Straight Permutation Table

per_table = [16, 7, 20, 21,
    29, 12, 28, 17,
    1, 15, 23, 26,
    5, 18, 31, 10,
    2, 8, 24, 14,
    32, 27, 3, 9,
    19, 13, 30, 6,
    22, 11, 4, 25]



# S-box Table

sbox_table = [[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],


        [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],


        [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],


        [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],


        [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],


        [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],


        [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],


        [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]]



# Final Permutation Table

final_perm_table = [40, 8, 48, 16, 56, 24, 64, 32,
            39, 7, 47, 15, 55, 23, 63, 31,
            38, 6, 46, 14, 54, 22, 62, 30,
            37, 5, 45, 13, 53, 21, 61, 29,
            36, 4, 44, 12, 52, 20, 60, 28,
            35, 3, 43, 11, 51, 19, 59, 27,
            34, 2, 42, 10, 50, 18, 58, 26,
            33, 1, 41, 9, 49, 17, 57, 25]



# key compresion P

key_comp = [14, 17, 11, 24, 1, 5,
            3, 28, 15, 6, 21, 10,
            23, 19, 12, 4, 26, 8,
            16, 7, 27, 20, 13, 2,
            41, 52, 31, 37, 47, 55,
            30, 40, 51, 45, 33, 48,
            44, 49, 39, 56, 34, 53,
            46, 42, 50, 36, 29, 32]



# Number of bit shifts
shift_table = [1, 1, 2, 2,
            2, 2, 2, 2,
            1, 2, 2, 2,
            2, 2, 2, 1]




def initial_perm_f(plaintext):
    plaintext = "".join(plaintext)
    x = []
    for i in initial_perm_table:
        x.append(plaintext[i-1])
    return list_x(x, 8)

def inital_key(key):
    x = []
    for i in inital_key_table:
        x.append(key[i - 1])
    return list_x(x, 7)

def decimal_to_binary(num, x):
    binary = ''
    for i in range(x):
        temp = num % 2
        num = num//2
        binary = chr(temp + 48) + binary
    return binary

def padding1(message):
    message_b = []
    for i in message:
        message_b.append(decimal_to_binary(ord(i), 8))
    count = 1
    while(len(message_b) < 8):
        message_b.append('00000020')
        count += 1
    return list_x(message_b, 8)


def padding2(message):
    message_b = []
    for i in message:
        message_b.append(decimal_to_binary(ord(i), 8))
    count = 1
    while(len(message_b) < 7):
        message_b.append('00000000')
        count += 1

    message_b.append(decimal_to_binary(count, 8))
    return list_x(message_b, 8)

def padding3(message):
    message_b = []
    count = 8
    for i in message:
        message_b.append(decimal_to_binary(ord(i), 8))
        count -= 1
    temp = decimal_to_binary(int(count), 8)
    while(len(message_b) < 8):
        message_b.append(temp)
    
    return list_x(message_b, 8)
    



def list_x(text, num):
    text = "".join(text)
    x = []
    for i in range(0, len(text), num):
        x.append(text[i: i+num])
    return x


def shift(key, round):
    key = "".join(key)
    for i in range(shift_table[round-1]):
        key = key[1:28] + key[0]
    return list_x(key, 7)

def expansion_p_f(key):
    key = "".join(key)
    x = []
    for i in exp_d_table:
        x.append(key[i-1])
    return list_x(x, 8)

def compression_p(key):
    key = ''.join(key)
    x = []
    for i in key_comp:
        x.append(key[i-1])
    return x

def xor(text1, text2):
    text1 = ''.join(text1)
    text2 = ''.join(text2)
    x = []
    for i in range(len(text1)):
        if text1[i] == text2[i]:
            x.append('0')
        else:
            x.append('1')
    return list_x(x, 6)

def str2dec(text):
    return int(text, 2)

def s_box_f(text):
    text = list_x(text, 6)
    x = []
    count = 0
    for i in text:
        row = str2dec(i[0] + i[5])
        col = str2dec(i[1:5])
        x.append(decimal_to_binary(sbox_table[count][row][col], 4))
        count += 1
    return x

def p_box_f(text):
    text = ''.join(text)
    x = []
    for i in per_table:
        x.append(text[i-1])
    return list_x(x, 8)

def final_permutaion_f(text):
    text = ''.join(text)
    x = []
    for i in final_perm_table:
        x.append(text[i-1])
    return list_x(x, 8)
        





# message = "ARIAL"  #input

message = input("Enter message: ")
round = 2   #input

print('[1] 00000020 00000020 00000020')
print('[2] 00000000 00000000 00000011')
print('[3] 00000011 00000011 00000011')
padding = int(input('Padding by: '))
if padding == 1:
    plaintext = padding1(message)
elif padding == 2:
    plaintext = padding2(message)
else:
    plaintext = padding3(message)
    

initial_perm = initial_perm_f(plaintext)
key = "1111111111111111111111111111111100000000000000000000000000000000"
inital_key = inital_key(key)
k_L = inital_key[:4]
k_R = inital_key[4:]
plaintext_L = initial_perm[:4]
plaintext_R = initial_perm[4:]


print('plaintext:', plaintext)
print('initial_perm:', initial_perm)
print('inital_key:', inital_key)

for i in range(round):
    print("Rount:", i+1)
    k_L_shift = shift(k_L, i)
    k_R_shift = shift(k_R, i)
    key_compression_p = compression_p(k_L_shift + k_R_shift)
    

    expansion_p = expansion_p_f(plaintext_R)
    exp_xor_key_com_p = xor(expansion_p, key_compression_p)
    s_box = s_box_f(exp_xor_key_com_p)
    p_box = p_box_f(s_box)


    print('k_L:', k_L)
    print('k_R:', k_R)
    print('k_L_shift:', k_L_shift)
    print('k_R_shift:', k_R_shift)
    print('L(' + chr(i+49) +'):', plaintext_L)
    print('R(' + chr(i+49) + '):', plaintext_R)
    print('expansion P:', expansion_p)
    print('exp xor key com p:', exp_xor_key_com_p)
    print('s_box:', s_box)
    print('P_box:', p_box)


    # set variable for new round
    temp = plaintext_R
    plaintext_R = list_x(xor(p_box, plaintext_L), 8)
    plaintext_L = temp
    k_L = k_L_shift
    k_R = k_R_shift
    print('plaintext_L', plaintext_L)
    print('plaintext_R', plaintext_R)

x = plaintext_L + plaintext_R

final_perm = final_permutaion_f(x)
print("Cipertext", final_perm)



