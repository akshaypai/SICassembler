optab = {'LDA': '10010', 'LDX': '100000', 'ADD': '101010101', 'SUB': '11001100', 'END': '1010101', 'START': '102020', 'RESB':'1010101'}
with open('symtab.txt') as af:
    temp = af.read()
temp1 = temp.strip().split('\n')
symtab = {}
for each in temp1:
    (sym,add)=each.split(' ')
    symtab[sym] = add
print(symtab)
oblist = []
def pass_two(file_name):
    fil = open(file_name, 'r')
    line = fil.readline().strip().split()
    if 'START' in line:
        pname = line[1]
        line = fil.readline().strip().split()
    while 'END' not in line:
        if line[1] in optab:
            opcode = line[1]
        elif line[2] in optab:
            opcode = line[2]
            symbol = line[1]
        if line[2] == 'BYTE' or line[2] == 'WORD':
            oblist.append(bin(int(line[-1])))
        if 'x' not in line:
            try:
                insert = optab[opcode]+'0'+ bin(int(symtab[line[2]]))[2:]
                oblist.append(insert)
            except:
                pass
        else:
            insert = optab[opcode]+'1'+bin((int(symtab[symbol])))[2:]
            oblist.append(insert)
        line = fil.readline().strip().split()
    print(oblist)
            
        
        
