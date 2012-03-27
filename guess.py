import re, sys

if len(sys.argv) < 3:
	print 'python guess.py [letters] [length]'
	sys.exit()

allletter = 'abcdefghijklmnopqrstuvwxyz';
match_pattern = sys.argv[1]
word_len = int(sys.argv[2]) 

print 'letters:', match_pattern
print 'word length:', word_len

for ch in match_pattern:
	allletter = allletter.replace(ch, '')	

not_match_pattern = allletter
match_re = re.compile('[' + match_pattern + ']+')
not_match_re = re.compile('[' + not_match_pattern + ']+')
words = open('word.txt', 'r')

while 1:
	line = words.readline().strip('\n')
	if not line:
		break
	else:
		if not len(line) == word_len:
			continue

		n = not_match_re.search(line)
		if n:
			continue

		m = match_re.search(line)
		if m:
			print "Possible Words =>", line

