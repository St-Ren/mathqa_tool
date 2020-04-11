import math
def toNum(word,ns,hashtag):
	if word[0] == 'n':
		idx = int(word[1:])
		if idx < len(ns):
			return ns[idx]
		else:
			return None
	if word[0] == '#':
		idx = int(word[1:])
		if idx < len(hashtag):
			return hashtag[idx]
		else:
			return None
	if 'const' in word:
		n = word.split('_')[1]
		if n == 'pi':
			return math.pi
		return float(n)
	else:
		print('invalid number '+word)
		return None

def caculate(op,ns):
	hashtag = []
	i = 0
	ops = op.split()
	while i < len(ops):
		if i + 1 >= len(ops):
				return ops[i]+' invalid len'
		num1 = toNum(ops[i + 1],ns,hashtag)
		if num1 == None:
				return 'number invalid'
		if ops[i] == 'inverse':
			hashtag.append(1/num1)
		elif ops[i] == 'negate':
			hashtag.append(-num1)
		elif ops[i] == 'sqrt':
			if num1 < 0:
				return 'neg sqrt'
			hashtag.append(math.sqrt(num1))
		elif ops[i] == 'circumface':
			hashtag.append(math.pi * num1)
		elif ops[i] == 'square_area':
			hashtag.append(num1 * num1)
		elif ops[i] == 'log':
			hashtag.append(math.log(num1))
		elif ops[i] == 'negate_prob':
			hashtag.append(1 - num1)
		elif ops[i] == 'factorial':
			hashtag.append(math.factorial(num1))
		elif ops[i] == 'floor':
			hashtag.append(math.floor(num1))
		elif ops[i] == 'circle_area':
			hashtag.append(num1 ** 2 * math.pi)
		elif ops[i] == 'surface_cube':
			hashtag.append(6 * num1 ** 2)
		elif ops[i] == 'volume_cube':
			hashtag.append(num1 ** 3)
		elif ops[i] == 'cube_edge_by_volume':
			hashtag.append(math.pow(num1,1/3))
		elif ops[i] == 'volume_sphere':
			hashtag.append(math.pi * num1 ** 3 * 4 /3)
		else:
			if i + 2 >= len(ops):
				return ops[i]+' invalid len'
			num1 = toNum(ops[i + 1],ns,hashtag)
			num2 = toNum(ops[i + 2],ns,hashtag)
			if num1 == None or num2 == None:
				return 'number invalid'
		
			if ops[i] == 'add':
				hashtag.append(num1 + num2)
			elif ops[i] == 'subtract':	
				hashtag.append(num1 - num2)
			elif ops[i] == 'multiply':
				hashtag.append(num1 * num2)
			elif ops[i] == 'divide':
				if num2 == 0:
					return 'divde 0'
				hashtag.append(num1 / num2)
			elif ops[i] == 'power':
				try:
					hashtag.append(math.pow(num1,num2))
				except:
					return '{} {} math range'.format(num1,num2)
			elif ops[i] == 'reminder':
				hashtag.append(num1%num2)
			elif ops[i] == 'rhombus_area':
				hashtag.append(num1 * num2 / 2)
			elif ops[i] == 'volume_cone':
				hashtag.append(num1*num1*num2*math.pi/3)
			elif ops[i] == 'gcd':
				hashtag.append(math.gcd(int(num1),int(num2)))
			elif ops[i] == 'lcm':
				hashtag.append(num1 * num2 / math.gcd(int(num1),int(num2)))
			elif ops[i] == 'triangle_area':
				hashtag.append(num1 * num2 / 2)
			elif ops[i] == 'rectangle_area':
				hashtag.append(num1 * num2)
			elif ops[i] == 'choose':
				hashtag.append(math.factorial(num1) / math.factorial(num2) / math.factorial(num1-num2))
			elif ops[i] == 'volume_cylinder':
				hashtag.append(math.pi * num1 * 2 * num2)
			else:
				if i + 3 >= len(ops):
					return ops[i]+' invalid len'
				num3 = toNum(ops[i + 3],ns,hashtag)
				if ops[i] == 'surface_rectangular_prism':
					hashtag.append((num1*num2 + num1 * num3 + num2 * num3) * 2 )
				elif ops[i] == 'volume_rectangular_prism':
					hashtag.append(num1 * num2 * num3)

				else:
					return ops[i]
				i += 1
			i += 1
		i += 2
	return hashtag[-1]

import json

nlist = open('test.nlist').readlines()
for i in range(len(nlist)):
	nlist[i] = json.loads(nlist[i])

ac = 0.0
count = 0.0
gen = open('gen.out').readlines()

for l in gen:
	idx,tgt,hypo = l.split('\t')
	idx = int(idx)
	tgtnum = caculate(tgt,nlist[idx])
	hyponum = caculate(hypo,nlist[idx])
	if type(tgtnum) == type('asdf'):
		print(idx,'tgt',tgtnum)
	if type(hyponum) == type('asdf'):
		print(idx,'hypo',hyponum)

	if tgtnum == hyponum:
		ac += 1.0

print(ac/len(gen))
