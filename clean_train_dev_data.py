import json


from get_ans import get_ans
from sent2num import sen2numre as s2n
from caculate import caculate
def linear2op(line):
    op = line.replace(')',' ').replace('|','').replace('(',' ').replace(',',' ')
    return op

for split in ['train','dev']:
    ct = 0
    err_ct = 0
    problems = json.load(open(split + '.json'))
    new_problems = []
    for problem in  problems:
        ct += 1
        #print(problem)
        _,nlist = s2n(problem['Problem'])
        op = linear2op(problem['linear_formula'])
        tgt = caculate(op,nlist)
        if type(tgt) == type('asdf'):
            err_ct += 1
            print(ct,err_ct)
            print(problem['Problem'],tgt)
            continue
        correct, choose = get_ans(problem,tgt)
        if correct == choose:
            new_problems.append(problem)
    json.dump(new_problems,open('right_data/'+split+'.json','w'))



