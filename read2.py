a = []
with open ('C:/Users/DOS/Desktop/coding/reviews.py/reviews.txt','r') as f:
	for line in f:
		a.append(line.strip())

good = []
for d in a:
	if 'good' in d:
		good.append(d)

print('It has',len(good),'message')