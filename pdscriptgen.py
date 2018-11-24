import sys
import regex

def assign_to_fc(d,k,x,y):
    key = w
    d[key] = [x, (y, z)]
    return d[key]


def assign_to_item(d,k,x):
    key = k
    d[key] = x
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

bpm = int(regex.search('bpm ?= ?(\d*)', arrangeInput).group('1'))
first = list(patterns.keys())[0]
gap = convert_bpm_to_ms(bpm)

# instrument tag and paremeters
with open(sys.argv[1]) as f:
    read_data = f.read()
    regExp = regex.findall('(n?seq):(\w*)\n\t?(r|v|s|n|o)? ?=? ?(.*)\n?\t?(r|v|s|n|o)? ?=? ?(.*)\n?\t?(r|v|s|n|o)? ?=? ?(.*)\n?', read_data)
    instr = {}
    for i in regExp:
        x = regExp[i]
        for j in range(2,6,2):
            # faltou testar se as strings são válidas
            tl = []
            tl.append((x[j],x[j+1]))
        assign_to_fc(instr, x[1], x[0], tl)
        tl.clear()


# preparing stored patterns
for i in instr:
    ev = instr[i]
    it = ev(1)
    for j in it:
        at = it[j]
        pattern = at[1]
        test = 1
        while test:
            exp = regex.findall("(?'head'(\w*\d*\s*)*(?!\*))(?'multi'\d*)\*\[(?'inner'(\w*\d*\s*)*(?:[^[]]|(?R))*)\](?'tail'(\w*\d*\s*)*(?!\*))", pattern)
            for k in exp:
                at[1] = exp.group('head') + (exp.group('multi') * exp.group('inner')) + exp.group('tail')
                brackets = regex.search('(\[|\])', pattern)
                if brackets == None:
                    test = 0
                    break
        tsil = []
        result = regex.findall('(\S*[^\s])',at[i])
        for i in range(len(result)):
            tulip = result[i]
            tsil.append(tulip[0])
            assign_to_item(instr[i],at[0],tsil))


# print ordered patterns
for i in range(16):
    for x, y in patterns.items():
        pgap = print_gap(gap, x, first)
        print(pgap, inst, x, y[i], ';')
    print('\n')
