A, B, C = 117440,0,0

program = "0,3,5,4,3,0".split(',')

LARGE = False

if True:
    A, B, C = 33940147, 0, 0
    program = "2,4,1,5,7,5,1,6,4,2,5,5,0,3,3,0".split(',')

output = list()
pointer = 0

def combo(x):
    if x < 4:
        return x
    if x == 4:
        return A
    if x == 5:
        return B
    if x == 6:
        return C
    assert False

while pointer < len(program):
    instruction = program[pointer]
    operand = int(program[pointer + 1])
    if instruction == '0':
        A = int(A  / (2 ** combo(operand)))
    if instruction == '1':
        B ^= operand
    if instruction == '2':
        B = combo(operand) % 8
    if instruction == '3':
        if A != 0:
            pointer = operand
            continue
    if instruction == '4':
        B = B ^ C
    if instruction == '5':
        output.append(combo(operand) % 8)
    if instruction == '6':
        B = int(A  / (2 ** combo(operand)))
    if instruction == '7':
        C = int(A  / (2 ** combo(operand)))
    pointer += 2

print(','.join(list(map(str,output))))