n = input()
lt = map(int, raw_input().split())
lt.sort()
pr,se = [], []
r = []
for i in lt :
	if i not in r :
		r.append(i)
vold = 0
for i in r :
	if i != 0 :
		vold += 1
print vold

