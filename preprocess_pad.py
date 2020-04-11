import json

for split in ['dev','test','train']:
	pro = []
	ope = []
	f = json.load(open(split+'.json'))
	for ques in f:
		pro.append(ques['Problem'])
		ops = ques['linear_formula']
		ops = ops.replace(')','').strip('|').split('|')
		for i in range(len(ops)):
			#print(ops[i])
			#print(ops[i].split('('))
			op,nums = ops[i].split('(')
			nums = nums.split(',')
			while len(nums) < 3:
				nums.append('PAD')
			nums = ' '.join(nums)
			ops[i] = '{} {}'.format(op,nums)
		op = ' '.join(ops)
		ope.append(op)
	open('data/pad/'+split+'.pro','w',encoding ='utf-8').write('\n'.join(pro))
	open('data/pad/'+split+'.ope','w',encoding = 'utf-8').write('\n'.join(ope))