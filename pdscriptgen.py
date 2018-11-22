import sys
import re

def assign_to_fc(d,k,x,y):
    key = w
    d[key] = [x, (y, z)]
    return d[key]

def convert_bpm_to_ms(x):
    return x / 15000

def print_gap(gap, x, y):
    if x == y:
        return gap
    else:
        return 0

# create patterns dict and add patterns to keys
patterns = {}
with open(sys.argv[1]) as input:
    for line in input:
        line = line.split()
        key = line[0]
        patterns[key] = line[2:len(line)]


arrangeInput = open(sys.argv[2], "r")
arrange = arrangeInput.readline()



bpm = int(re.search('bpm ?= ?(\d*)', arrangeInput).group('1'))
first = list(patterns.keys())[0]
gap = convert_bpm_to_ms(bpm)


# instrument tag and paremeters
with open(sys.argv[1]) as f:
    read_data = f.read()
    regExp = re.findall('(n?seq):(\w*)\n\t?(r|v|s|n|o)? ?=? ?(.*)\n?\t?(r|v|s|n|o)? ?=? ?(.*)\n?\t?(r|v|s|n|o)? ?=? ?(.*)\n?', read_data)
    instr = {}
    for i in regExp:
        x = regExp[i]
        for j in range(2,6,2):
            # faltou testar se as strings são válidas
            tl = []
            tl.append((x[j],x[j+1])
        assign_to_fc(instr, x[1], x[0], tl)
        tl.clear()

                      
# print ordered patterns
for i in range(16):
    for x, y in patterns.items():
        pgap = print_gap(gap, x, first)
        print(pgap, inst, x, y[i], ';')
    print('\n')