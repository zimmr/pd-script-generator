import sys
import regex

def assign_to_fc(d,k,x,y):
    key = k
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


#arrangeInput = open(sys.argv[2], "r")
#arrange = arrangeInput.readline()


# instrument tag and paremeters
with open(sys.argv[2]) as f:
    read_data = f.read()
    bpm = int(regex.search('bpm ?= ?(\d*)', read_data).group('1'))
    first = list(patterns.keys())[0]
    gap = convert_bpm_to_ms(bpm)
    regExp = regex.findall('(n?seq):(\w*)\n\t?(r|v|s|n|o)? ?=? ?(.*)\n?\t?(r|v|s|n|o)? ?=? ?(.*)\n?\t?(r|v|s|n|o)? ?=? ?(.*)\n?', read_data)
    arrangement = {}
    for i in regExp:
        x = regExp[i]
        for j in range(2,6,2):
            # faltou testar se as strings são válidas
            tsil = []
            tsil.append((x[j],[x[j+1]]))
        assign_to_fc(arrangement, x[1], x[0], tsil)
        tsil.clear()


#instruments = arrangement.keys()
#arrangement = {}
sizes = []
tsil = []

# preparing stored patterns
for i in arrangement:
    ev = arrangement[i]
    it = ev(1)
    for j in it:
        at = it[j]
        test = 1
        while test:
            exp = regex.findall("(?'head'(\w*\d*\s*)*(?!\*))(?'multi'\d*)\*\[(?'inner'(\w*\d*\s*)*(?:[^[]]|(?R))*)\](?'tail'(\w*\d*\s*)*(?!\*))",at[1]) 
            for k in exp:
                at[1] = exp.group('head') + (exp.group('multi') * exp.group('inner')) + exp.group('tail')
                brackets = regex.search('(\[|\])', pattern)
                if brackets == None:
                    test = 0
                    break
        result = regex.findall('(\S*[^\s])',at[i])
        for i in range(len(result)):
            tsil.append(result[i])
        at[1] = tsil
        sizes.append(tsil)
        tsil.clear()


with open(sys.argv(2),w) as output:
    for m in range(max(sizes)):
        for i in arrangement: 
            ev = arrangement[i]
            it = ev(1)
        for j in it:
            at = it[j]
            patternCall = at[1]
            if m > len(patternCall):
                if patternCall[m] == 'x':
                   break
                 else:
                   if ev[0] == seq:
                       if at[0l == 'r':
                           paramTag = 'pattern'
                           if patternCall[m] == 'ø':
                               patternToPrint = '0'*16
                           else:
                               patternToPrint = patterns[i]
                       elif at[0] == '\v':
                           paramTag = 'vpattern'
                           if patternCall[m] == 'ø':
                               patternToPrint = '100'*16
                           else:
                               patternToPrint = patterns[i]
                       elif at[0] == 's':
                           paramTag = 'rpattern'
                           if patternCall[m] == 'ø':
                               patternToPrint = '0'*16
                           else:
                               patternToPrint = patterns[i]
                   elif ev[0] == nseq:
                       if at[0l == '\n':
                           paramTag = 'note-pattern'
                           if patternCall[m] == 'ø':
                               patternToPrint = '0'*16
                           else:
                               patternToPrint = patterns[i]
                       elif at[0] == '\o':
                           paramTag = 'oct-pattern'
                           if patternCall[m] == 'ø':
                               patternToPrint = '4'*16
                           else:
                               patternToPrint = patterns[i]
                       elif at[0] == '\v':
                           paramTag = 'vel-pattern'
                           if patternCall[m] == 'ø':
                               patternToPrint = '100'*16
                           else:
                               patternToPrint = patterns[i]
                   output.write("{0} {1}-{2} {3};".format(gapToPrint,paramTag,instrName,patternToPrint))   

