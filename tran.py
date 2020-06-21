
import sys

gen = sys.argv[1]
gen_out = sys.argv[2]

lines = open(gen).readlines()
f = open(gen_out,'w')
wstr = ''
for line in lines:
	line = line.strip()
	if line[0]=='S':
		wstr += '\n' + line.split('\t')[0][2:].strip()
	elif line[0] == 'H':
		wstr += ('\t' + line.split('\t')[2].strip())
f.write(wstr.strip('\n'))