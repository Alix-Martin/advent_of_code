from random import randint

A, B, C = 117440,0,0

program = "0,3,5,4,3,0".split(',')

LARGE = True

if LARGE:
    A, B, C = 3, 0, 0
    program = "2,4,1,5,7,5,1,6,4,2,5,5,0,3,3,0"
    print(program)
    print()
    program = program.split(',')

output = list()
pointer = 0

def combo_operand(x):
    if x < 4:
        return x
    if x == 4:
        return 'A'
    if x == 5:
        return 'B'
    if x == 6:
        return 'C'
    assert False  # reserved value

def disassemble(program):
    ops = {0: 'adv',
           1: 'bxl',
           2: 'bst',
           3: 'jnz',
           4: 'bxc',
           5: 'out',
           6: 'bdv',
           7: 'cdv'}
    pointer = 0
    while pointer < len(program):
        opcode = int(program[pointer])
        operand = int(program[pointer + 1])
        if opcode in [0, 2, 5, 6, 7]:
            operand = combo_operand(operand)
        print(ops[opcode], operand)
        pointer += 2

disassemble(program)
print()

def combo(x, A, B, C):
    if x < 4:
        return x
    if x == 4:
        return A
    if x == 5:
        return B
    if x == 6:
        return C
    assert False

def run(program, A, B, C):
    pointer = 0
    output = list()
    while pointer < len(program):
        instruction = program[pointer]
        operand = int(program[pointer + 1])
        if instruction == '0':
            A = int(A  / (2 ** combo(operand, A, B, C)))
        if instruction == '1':
            B ^= operand
        if instruction == '2':
            B = combo(operand, A, B, C) % 8
        if instruction == '3':
            if A != 0:
                pointer = operand
                continue
        if instruction == '4':
            B = B ^ C
        if instruction == '5':
            output.append(combo(operand, A, B, C) % 8)
        if instruction == '6':
            B = int(A  / (2 ** combo(operand, A, B, C)))
        if instruction == '7':
            C = int(A  / (2 ** combo(operand, A, B, C)))
        pointer += 2
    return output

# A = randint(8 ** 15, 8 ** 16 - 1)
target = "2,4,1,5,7,5,1,6,4,2,5,5,0,3,3,0"

# print(target.replace(',', '')[::-1])
# 0330552461575142

A = 0o3033001642550333
AA = A

print(oct(A))
output = run(program, A, B, C)
print(','.join(list(map(str,output))))
print()

for digit in range(16):
    print(f'{digit=}')
    for d in range(8):
        A = AA
        A = str(oct(A))[2:]

        A = int(A[:digit] + str(d) + A[(digit + 1):], 8)

        # print(oct(A))
        output = run(program, A, 0, 0)
        print(d, oct(A)[2:], ''.join(list(map(str, output[::-1]))))
    print()