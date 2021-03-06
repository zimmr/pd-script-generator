import sys
import regex

def assign_to_fc(d, k, x, y):
    key = k
    d[key] = [x, [y]]
    return d[key]

def build_string(head, multi, inner, tail):
    if multi != '' and multi != None and inner != '' and inner != None:
        prod = int(multi) * (inner + ' ')
        if prod != None and prod != '':
            return head + prod + tail + ' '
    elif head != None and tail != None:
        return head + tail + ' '
    else:
        return head 

def convert_bpm_to_ms(x):
    return (15000 / x) * 16

def convert_list_to_str(x):
    p = ''
    for item in x:
        rs = regex.match('(\w*)[^\n]', str(item))
        if rs != None:
            p += rs[0] + ' '
    return p

def print_gap(gap, x, w, y, z):
    if x == y and w == z:
        return '\n' + str(gap)
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
with open(sys.argv[2]) as f:
    read_data = f.read()
    bpm = int(regex.search('bpm ?= ?(\d*)', read_data).group(1))
    gap = convert_bpm_to_ms(bpm)
    regExp = regex.findall('(n?seq):(\w*)\n\t?(r|v|s|n|o)? ?=? ?(.*)\n?\t?(r|v|s|n|o)? ?=? ?(.*)\n?\t?(r|v|s|n|o)? ?=? ?(.*)\n?', read_data) # this regex can be shortened
    instruments = {}
    arrangement = {}
    for i in range(len(regExp)):
        x = regExp[i]
        instruments[x[1]] = x[0]
        arrangement[x[1]] = {}
        for j in range(2, 6, 2):
            arrangement[x[1]][x[j]] = x[j+1]


# preparing stored patterns
tsil = []
sizes = []

for i in arrangement.keys():
    teste = arrangement[i]
    for j in arrangement[i]:
        ev = arrangement[i][j]
        test = 1
        while test:
            exp = regex.search("(?<head>(\w*\s*)*(?!\*))((?<multi>\d*)\*\[(?<inner>(\w*\s*)*(?:[^[]]|(?R))*)\](?<tail>(\w*\s*)*(?!\*)))*", ev) 
            ev = build_string(exp.group('head'), exp.group('multi'), exp.group('inner'), exp.group('tail'))
            brackets = regex.search('(\[|\])', ev)
            if brackets == None:
                test = 0
                break
        result = regex.findall('(\S*[^\s])', ev)
        for k in range(len(result)):
            tsil.append(result[k])
        arrangement[i][j] = tsil
        sizes.append(len(tsil))
        tsil = []


# writing patterns to output file
with open(sys.argv[3], "w") as output:
    for m in range(max(sizes)):
        for i in arrangement: 
            first = list(arrangement.keys())[0]
            firstParam = list(arrangement[i].keys())[0]
            instrName = i
            iv = arrangement[i]
            for j in iv:
                parameter = j
                pv = iv[j]
                if m < len(pv):
                    call = pv[m]
                    if call == 'x':
                       break
                    else:
                       gapToPrint = print_gap(gap, i, parameter, first, firstParam) 
                       if instruments[i] == 'seq':
                           if parameter == 'r':
                               parameter = 'pattern'
                               if call == '0':
                                   patternToPrint = '0 ' * 16
                               else:
                                   patternToPrint = convert_list_to_str(patterns[call])
                           elif parameter == 'v':
                               parameter = 'vpattern'
                               if call == '0':
                                   patternToPrint = '100 ' * 16
                               else:
                                   patternToPrint = convert_list_to_str(patterns[call])
                           elif parameter == 's':
                               parameter = 'rpattern'
                               if call == '0':
                                   patternToPrint = '0 ' * 16
                               else:
                                   patternToPrint = convert_list_to_str(patterns[call])
                       elif instruments[i] == 'nseq':
                           if parameter == 'n':
                               parameter = 'note-pattern'
                               if call == '0':
                                   patternToPrint = '0 ' * 16
                               else:
                                   patternToPrint = convert_list_to_str(patterns[call])
                           elif parameter == 'o':
                               parameter = 'oct-pattern'
                               if call == '0':
                                   patternToPrint = '4 ' * 16
                               else:
                                   patternToPrint = convert_list_to_str(patterns[call])
                           elif parameter == 'v':
                               parameter = 'vel-pattern'
                               if call == '0':
                                   patternToPrint = '100 ' * 16
                               else:
                                   patternToPrint = convert_list_to_str(patterns[call])
                       output.write("{0} {1}-{2} {3};\n".format(gapToPrint, parameter, instrName, patternToPrint))   


