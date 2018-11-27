import sys
import regex

def assign_to_fc(d, k, x, y):
    key = k
    d[key] = [x, [y]]
    return d[key]

def build_string(head, multi, inner, tail):
    if multi != '' and multi != None and inner != '' and inner != None:
        prod = int(multi) * inner
        if prod != None and prod != '':
            return head + prod + tail
    elif head != None and tail != None:
        return head + tail
    else:
        return head 

def convert_bpm_to_ms(x):
    return x / 15000

def print_gap(gap, x, y):
    if x == y:
        return gap
    else:
        return 0


# create patterns dict and add patterns to keys
patterns = {}
with open(sys.argv[1], "r") as input:
    for line in input:
        line = line.split(' ')
        key = line[0]
        patterns[key] = line[2:len(line)]


# instrument tag and paremeters
tsil = []
with open(sys.argv[2]) as f:
    read_data = f.read()
    bpm = int(regex.search('bpm ?= ?(\d*)', read_data).group(1))
    first = list(patterns.keys())[0]
    gap = convert_bpm_to_ms(bpm)
    regExp = regex.findall('(n?seq):(\w*)\n\t?(r|v|s|n|o)? ?=? ?(.*)\n?\t?(r|v|s|n|o)? ?=? ?(.*)\n?\t?(r|v|s|n|o)? ?=? ?(.*)\n?', read_data) # this regex can be shortened
    arrangement = {}
    for i in range(len(regExp)):
        x = regExp[i]
        for j in range(2, 6, 2):
            # verify if the strings are not null
            tsil.append((x[j], [x[j+1]]))
        assign_to_fc(arrangement, x[1], x[0], tsil)
        tsil = []


<<<<<<< HEAD
bpm = int(regex.search('bpm ?= ?(\d*)', arrangeInput).group('1'))
first = list(patterns.keys())[0]
gap = convert_bpm_to_ms(bpm)
=======
# preparing stored patterns
sizes = []
for i in arrangement:
    ev = arrangement[i]
    paramList = ev[1]
    for iterParam in range(len(paramList)):
        it = paramList[iterParam]
        for j in range(len(it)):
            bt = it[j]
            at = bt[1]
            test = 1
            lineEv = at[0]
            while test:
                exp = regex.search("(?<head>(\w*\s*)*(?!\*))((?<multi>\d*)\*\[(?<inner>(\w*\s*)*(?:[^[]]|(?R))*)\](?<tail>(\w*\s*)*(?!\*)))*", lineEv) 
                #print[lineEv, exp]
                at = build_string(exp.group('head'), exp.group('multi'), exp.group('inner'), exp.group('tail'))
                brackets = regex.search('(\[|\])', at)
                if brackets == None:
                    test = 0
                    break
            result = regex.findall('(\S*[^\s])', at)
            for i in range(len(result)):
                tsil.append(result[i])
            at = tsil
            sizes.append(len(tsil))
            tsil = []
>>>>>>> dev

# writing patterns to output file
with open(sys.argv[3], "w") as output:
    for m in range(max(sizes)):
        for i in arrangement: 
            ev = arrangement[i]
            it = ev[1]
        for j in range(len(it)):
            bt = it[j]
            at = bt[1]
            qt = at[1]
            pt = qt[0]
            print(qt,'////',pt)
            result = regex.findall('(\w*)\s?', pt)
            for iterP in range(len(result)):
                call = result[iterP]
                if m < len(result) and call != '':
                    if call == 'x':
                       break
                    else:
                       if ev[0] == 'seq':
                           if at[0] == 'r':
                               parameter = 'pattern'
                               if call == '0':
                                   patternToPrint = '0 ' * 16
                               else:
                                   patternToPrint = patterns[call]
                           elif at[0] == 'v':
                               parameter = 'vpattern'
                               if call == '0':
                                   patternToPrint = '100 ' * 16
                               else:
                                   patternToPrint = patterns[call]
                           elif at[0] == 's':
                               parameter = 'rpattern'
                               if call == '0':
                                   patternToPrint = '0 ' * 16
                               else:
                                   patternToPrint = patterns[call]
                       elif ev[0] == 'nseq':
                           if at[0] == 'n':
                               parameter = 'note-pattern'
                               if call == '0':
                                   patternToPrint = '0 ' * 16
                               else:
                                   patternToPrint = patterns[call]
                           elif at[0] == 'o':
                               parameter = 'oct-pattern'
                               if call == '0':
                                   patternToPrint = '4 ' * 16
                               else:
                                   patternToPrint = patterns[call]
                           elif at[0] == 'v':
                               parameter = 'vel-pattern'
                               if call == '0':
                                   patternToPrint = '100 ' * 16
                               else:
                                   patternToPrint = patterns[call]
                       instrName = i
                       gapToPrint = print_gap(gap, m, first) 
                       output.write("{0} {1}-{2} {3};\n".format(gapToPrint, parameter, instrName, patternToPrint))   

<<<<<<< HEAD
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
            tl.append((x[j],x[j+1])
        assign_to_fc(instr, x[1], x[0], tl)
        tl.clear()

                      
# print ordered patterns
for i in range(16):
    for x, y in patterns.items():
        pgap = print_gap(gap, x, first)
        print(pgap, inst, x, y[i], ';')
    print('\n')
=======
>>>>>>> dev
