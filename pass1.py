#pass one of the assembler
#creates symtab file , an intermiate file with address
line_store = []
locctr = 0
start_add = 0
symtab = {}
optab = {'LDA': 10010, 'LDX': 100000, 'ADD': 101010101, 'SUB': 11001100, 'END': 1010101, 'START': 102020}
def opcode_check(opcode):
    if opcode in optab:
        return opcode
    elif opcode not in symtab:
        return 1
def pass_one(file_name):
    opcode = None
    symbol = None
    temp = 0
    code = open(file_name ,'r')
    line = code.readline().strip().split()
    if 'START' in line:
        start_add = int(line[-1])
        locctr = start_add
        line.insert(0,str(start_add))
        line_store.append(line)
        line = code.readline().strip().split()
    else:
        locctr = 0
    answer = opcode_check(line[0])
    if answer == 1:
        symbol = line[0]
        print(symbol)
    else:
        opcode = answer
        
    while 'END' not in line:
        if symbol:
                symtab.update({symbol:str(locctr)})
        if opcode:
            temp = 3
        elif line[1] == 'WORD':
            temp = 3
        elif line[1] == 'RESW':
            temp = (3* int(line[-1]))
        elif line[1] == 'RESB':
            temp =  int(line[-1])
        elif  line[1] == 'BYTE':
            char_count = line[2].strip().split('\'')
            if c in char_count:
                    locctr = locctr + len(char_count[1])
        else:
            pass
        locctr = locctr + temp
        line_store.append(line)
        line.insert(0,str(locctr-temp))
        line = code.readline().strip().split()
        answer = opcode_check(line[0])
        if answer == 1:
            symbol = line[0]
        else:
            opcode = answer
    line.insert(0,str(locctr))
    line_store.append(line)
    interfile = open('intermidiate.txt', 'a')
    for i in range(len(line_store)):
        str1 = ' '.join(line_store[i])
        interfile.writelines(str1+'\n')
    interfile.close()
    print(symtab)
    symfile = open('symtab.txt','a')
    for i in range(len(symtab)):
        temp = list(symtab.popitem())
        str1 = ' '.join(temp)
        symfile.writelines(str1+'\n')
    symfile.close()

                   
    

            
            
    
        
                
        
                
                     
            
        
