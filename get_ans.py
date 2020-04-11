from unicodedata import numeric
from caculate_pad import caculate,toNum
def get_num(num_str):

	if ' ) ' in num_str:
		return get_num(num_str.split(' ) ')[1])
	if 'rs .' in num_str:
		return get_num(num_str.split('rs .')[1])
	num_str = num_str.replace('. ','.')
	num_str = num_str.replace('. ','.')
	if '-' in num_str:
		return -get_num(num_str.split('-')[1])
	if '–' in num_str:
		return -get_num(num_str.split('–')[1])
	for i,num in enumerate(['one','two','three','four','five','six']):
		if num in num_str:
			return i + 1
	if num_str[0] == '$':
		return int(num_str[1:])
	if '/' in num_str:
		n1,n2 = num_str.split('/')
		return get_num(n1)/get_num(n2)
	if ':' in num_str:
		n1,n2 = num_str.split(':')
		return get_num(n1)/ get_num(n2) 
	if len(num_str.split()) != 1:
		return get_num(num_str.split()[0])
	if '.' in num_str:
		return float(num_str)
	if 'none' in num_str:
		return None
	return int(num_str)
	
	print(num_str)
		
	
		#return numeric(num_str)



def get_ans(problem,hypo):
	ops = [get_num(op[4:]) for op in problem['options'].split(' , ')]
	correct = ord(problem['correct']) - ord('a')
	choose = 0
	have_none = -1
	for i in range(1,5):
		if ops[i] == None:
			have_none = i
			continue
		if abs(hypo - ops[i]) < abs(hypo - ops[choose]):
			choose = i
	if have_none >= 0:
		if abs(hypo - ops[choose]) > 1 or abs((hypo - ops[choose])/ops[choose]) > 0.01:
			choose = have_none
	return correct, choose

import math

import sys

import json

nlist = open('test.nlist').readlines()
for i in range(len(nlist)):
	nlist[i] = json.loads(nlist[i])

ac = 0.0
count = 0.0
if len(sys.argv) == 2:
	out = sys.argv[1]
else:
	out = 'gen.out'
gen = open(out).readlines()
problems = json.load(open('test.json'))
error_c = 0
err_ans = 0
for l in gen:
	count += 1
	idx,tgt,hypo = l.split('\t')
	idx = int(idx)

	hyponum = caculate(tgt,nlist[idx])
	if type(hyponum) == type('asdf'):
		print(idx,'hypo',hyponum)
		error_c += 1
		continue
	try:
		correct, choose = get_ans(problems[idx],hyponum)
		if correct == choose:
			ac += 1
	except:
		print(idx)
		err_ans += 1
		continue
print(ac/count)
print(error_c)
print(err_ans)