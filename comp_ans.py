from unicodedata import numeric
from caculate import mul_caculate,toNum,caculate
from word2number import w2n
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
		if len(num_str.split('/')) > 2:
			return None
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
		return try_get_num(num_str.split(' ) ')[1])
	if 'rs .' in num_str:
		return try_get_num(num_str.split('rs .')[1])
	
	num_str = num_str.replace('. ','.')
	num_str = num_str.replace('. ','.')
	num_str = num_str.replace(',','')
	if '/' in num_str:
		if len(num_str.split('/')) > 2:
			return None
		n1,n2 = num_str.split('/')
		n1 = try_get_num(n1)
		n2 = try_get_num(n2)
		if n1 == None:
			return 0
		elif n2 == 0 or n2 == None:
			return None
		return n1/n2
	if ':' in num_str:
		n1,n2,*l = num_str.split(':')
		n1 = try_get_num(n1)
		n2 = try_get_num(n2)
		if n1 == None:
			return 0
		if n2 == 0 or n2 == None:
			return None
		return n1/n2 
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
	if 'none' in num_str.lower() or 'no ' in num_str.lower():
		return None
	try:
		w2n.word_to_num(num_str)
	except ValueError:
		print('error_ans {}'.format(num_str))
		return None


def get_ans(problem):
	ops = problem['options']
	if len(ops) != 5:
		if problem['options'][1] == "'":
			ops = json.loads(problem['options'].replace("'",'"'))
		else:
			ops = problem['options'].split(' , ')


	#try:
	ops = [try_get_num(op[4:]) for op in ops]
	#except:
	#	print('get_ans err',problem['options'])
	#	return 'err_ans:','err'
	correct = ord(problem['correct']) - ord('A')
	
	return ops[correct]

import math

import sys

import json


def main():
	nlist = open('train.nlist').readlines()
	for i in range(len(nlist)):
		nlist[i] = json.loads(nlist[i])
	cor_f = open('correct_op.txt','w')
	ac = 0.0
	count = 0.0
	matrix = [ [0] * 5 for i in range(5)]
	if len(sys.argv) == 2:
		out = sys.argv[1]
	else:
		out = 'gen.out'
	gen = open(out).readlines()
	problems = [json.loads(s) for s in open('train.tok.json')]
	print('len prob',len(problems))
	
	err_ans = 0
	for l in gen:
		count += 1
		hypos = l.split('\t')
		idx = int(hypos[0])
		hypos = hypos[1:]
		
		#print(hypo)
		ans = get_ans(problems[idx])
		if ans == None:
			err_ans += 1
			continue
		for hp in hypos:
			hyponum = caculate(hp,nlist[idx])
			if hyponum == ans:
				ac +=1
				cor_f.write('{} {} {}\n'.format(idx,hyponum,hp))
				break
		
		
	dic = json.load(open('len_dic.json'))
	if dic == None:
		dic = dict()
	dic[len(hypos)] = [ac,err_ans]
	json.dump(dic, open('len_dic.json','w'))
	print(ac)
	print(err_ans)
if __name__ == '__main__':
	main()