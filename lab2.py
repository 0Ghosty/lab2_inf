syndrome = {'000': True,
            '001': 3,
            '010': 1,
            '011': 5,
            '100': 0,
            '101': 4,
            '110': 2,
            '111': 6}
syndrome_bit = {'000': True,
                '001': 'r3',
                '010': 'r2',
                '011': 'i3',
                '100': 'r1',
                '101': 'i2',
                '110': 'i1',
                '111': 'i4'}
Check = False
while Check == False:
    code_in = input()
    if code_in.isdigit() and len(code_in) == 7:
        for i in code_in:
            if i  in '01':
                Check = True
            else:
                Check = False
                break
s1 = int(code_in[0]) ^ int(code_in[2]) ^ int(code_in[4]) ^ int(code_in[6])
s2 = int(code_in[1]) ^ int(code_in[2]) ^ int(code_in[5]) ^ int(code_in[6])
s3 = int(code_in[3]) ^ int(code_in[4]) ^ int(code_in[5]) ^ int(code_in[6])
s = str(s1) + str(s2) + str(s3)
error_id = syndrome[s]
error_bit = syndrome_bit[s]
if error_id == True:
    print(code_in[2] + code_in[4] + code_in[5] + code_in[6])
else:
    if code_in[error_id] == '1':
        code_out = code_in[0:error_id] + '0' + code_in[error_id + 1:7]
        print(code_out[2] + code_out[4] + code_out[5] + code_out[6],
              'Ошибочный бит ' + str(error_bit), sep='\n')
    else:
        code_out = code_in[0:error_id] + '1' + code_in[error_id + 1:7]
        print(code_out[2] + code_out[4] + code_out[5] + code_out[6],
              'Ошибочный бит ' + str(error_bit), sep='\n')
