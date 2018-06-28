data = []
count = 0
k_total = 0
with open ('C:/Users/Also_T410/Desktop/reviews.txt','r') as f:
	for line in f:
		#data.append(line.strip())
		count += 1
		data.append(line)
		#if count % 1000 == 0:
		#	print(count)
		k = (len(line))
		k_total += k
print(data[1])
print (len(data))
k_means = k_total/len(data)
print(k_means)
print(k_total)