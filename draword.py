words = open('word.txt', 'r')
max_len = 0;
lines=[];
while 1:
	line = words.readline().strip('\n')
	if not line:
		break
	else:
		lines.insert(len(line), line)
		print "line:", line
		if len(line) > max_len:
			max_len = len(line)

index = range(1, max_len)
print "index-->", index
for i in index:
	if len(lines[i]) > 0:
		print "list:", lines[i]

