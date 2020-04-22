from unicodedata import numeric
from caculate import caculate,toNum
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

def try_get_num(num_str):
	if ' ) ' in num_str:
		return get_num(num_str.split(' ) ')[1])
	if 'rs .' in num_str:
		return get_num(num_str.split('rs .')[1])
	
	num_str = num_str.replace('. ','.')
	num_str = num_str.replace('. ','.')
	num_str = num_str.replace(',','')
	if '/' in num_str:
		n1,n2 = num_str.split('/')
		return try_get_num(n1)/try_get_num(n2)
	if ':' in num_str:
		n1,n2 = num_str.split(':')
		return try_get_num(n1)/ try_get_num(n2) 
	for i,num in enumerate(['one','two','three','four','five','six']):
		if num in num_str.lower():
			return i + 1
	num_str = num_str.replace(' ','')
	for i in range(len(num_str),0,-1):
		for j in range(len(num_str) - i + 1):
			try:
				rt = float(num_str[j : j + i])
				return rt
			except ValueError:
				continue
	if 'none' in num_str.lower():
		return None

	return 'error_ans {}'.format(num_str)



def get_ans(problem,hypo):
	try:
		json.loads
		##json type ans
	try:
		ops = [get_num(op[4:]) for op in problem['options'].split(' , ')]
	except:
		print('get_ans err')
		return 'err_ans:','err'
	correct = ord(problem['correct']) - ord('a')
	choose = 0
	have_none = -1
	for i in range(5):
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


def main():
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
		print(idx)
		hyponum = caculate(hypo,nlist[idx])
		if type(hyponum) == type('asdf'):
			print(idx,'hypo',hyponum)
			error_c += 1
			continue
		
		correct, choose = get_ans(problems[idx],hyponum)
		if type(correct) != type('asdf'):
			if correct == choose:
				ac += 1
			else:
				print('wrong ans',idx)
		else:
			
			print(idx,'err_ans',err_ans)
			err_ans += 1
			continue
	print(ac/count)
	print(error_c)
	print(err_ans)
if __name__ == '__main__':
	main()