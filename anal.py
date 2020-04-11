from get_ans import *
from caculate import caculate,toNum


import math

import sys

import json

nlist = open('test.nlist').readlines()
for i in range(len(nlist)):
	nlist[i] = json.loads(nlist[i])

clist = json.load(open('clist.json'))

cat = {'other', 'probability', 'general', 'gain', 'physics', 'geometry'}

dic = {'correct':0, 'invalid hypo':0, 'invalid ans':0, 'wrong ans':0}

cat_dic = {ct : dic.copy() for ct in cat}

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
	
	hyponum = caculate(hypo,nlist[idx])
	if type(hyponum) == type('asdf'):
		print(idx,'hypo',hyponum)
		error_c += 1
		cat_dic[clist[idx]]['invalid hypo'] += 1
		continue
	try:
		correct, choose = get_ans(problems[idx],hyponum)
		if correct == choose:
			ac += 1
			cat_dic[clist[idx]]['correct'] += 1
		else:
			cat_dic[clist[idx]]['wrong ans'] += 1
	except:
		print(idx)
		cat_dic[clist[idx]]['invalid ans'] += 1
		err_ans += 1
		continue
import pandas as pd

pd.DataFrame(cat_dic).to_csv('cat.csv')
json.dump(cat_dic,open('cat.json','w'))
print(ac/count)
print(error_c)
print(err_ans)