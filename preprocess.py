import json

for split in ['dev','test','train']:
	pro = []
	ope = []
	f = json.load(open(split+'.json'))
	for ques in f:
		pro.append(ques['Problem'])
		op = ques['linear_formula']
		op = op.replace(')','').replace('|',' ').replace('(',' ').replace(',',' ')
		ope.append(op)
	open('data/'+split+'.pro','w',encoding ='utf-8').write('\n'.join(pro))
	open('data/'+split+'.ope','w',encoding = 'utf-8').write('\n'.join(ope))