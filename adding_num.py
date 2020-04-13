from unicodedata import numeric

import json
def sen2numre(sen):
	rep_list = []
	sen = sen.replace(' , ',',').replace(',',' , ').replace(': ',':').replace(' :',':').replace(':',' : ')
	l = sen.split()
	n_old = []
	n_new = []
	for i in range(len(l)):
		if l[i].isdecimal():
			n_old.append(float(l[i]))
			n_new.append(float(l[i]))
			rep_list.append(('n{}'.format(len(n_old) - 1),'n{}'.format(len(n_new) - 1)))
			l[i] = 'n{}'.format(len(n_new) - 1)

		elif l[i].isnumeric():
			n_new.append(numeric(l[i]))
			l[i] = 'n{}'.format(len(n_new) - 1)


	return ' '.join(l),rep_list


for split in ['dev','test','train']:
	pro = []
	ope = []
	f = json.load(open(split+'.json'))
	list_file = open(split+'.unilist','w')
	for ques in f:
		nl,repl = sen2numre(ques['Problem'])

		list_file.write(json.dumps(nl) + '\n')
		pro.append(ques['Problem'])
		op = ques['linear_formula']
		op = op.replace(')','').replace('|',' ').replace('(',' ').replace(',',' ')
		for oldn,newn in repl:
			op = op.replace(oldn,newn)


		ope.append(op)
	open('unidata/'+split+'.pro','w',encoding ='utf-8').write('\n'.join(pro))
	open('unidata/'+split+'.ope','w',encoding = 'utf-8').write('\n'.join(ope))