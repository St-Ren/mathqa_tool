from unicodedata import numeric
import json
def sen2numre(sen):
	l = sen.split()
	n = []
	for i in range(len(l)):
		if l[i].isdecimal():
			n.append(float(l[i]))
			l[i] = 'n{}'.format(len(n) - 1)
	return ' '.join(l),n

for split in ['dev','test','train']:

	lines = open(split + '.pro', encoding='utf-8').readlines()
	new_file = open('new/' + split + '.pro','w', encoding='utf-8')
	list_file = open(split + '.nlist','w', encoding='utf-8')
	for line in lines:
		l,n = sen2numre(line)
		new_file.write(line)
		list_file.write(json.dumps(n) + '\n')