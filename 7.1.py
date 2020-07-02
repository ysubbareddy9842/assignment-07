import itertools      
d ={'1':['j','m'], '2':['n','o']}
for combo in itertools.product(*[d[k] for k in sorted(d.keys())]):
    print(''.join(combo))
	