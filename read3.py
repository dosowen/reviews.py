data = []
with open ('C:/Users/DOS/Desktop/coding/reviews/reviews.txt','r') as f:
	for line in f:
		data.append(line.strip())

WC = {}

for words in data:
	words = words.split()
	for word in words:
		if word in WC:
			WC[word] += 1
			
			
		else:
			WC[word] = 1
for word in WC:
	if WC[word] > 1000000:
		print(word,':',WC[word])

while True:
	check = input('please type the word you want to check:')
	if check == 'q':
		break
	if check in WC:
		print(check,':',WC[check])
	if check not in WC:
		print('cannot find it')




































# good = []
# for d in a:
# 	if 'good' in d:
# 		good.append(d)

# print('It has',len(good),'message about good')

# bad = [d for d in a if 'bad' in d]
# print('It has',len(bad),'message about bad')