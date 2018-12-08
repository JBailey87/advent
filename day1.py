filepath = 'input/day1/day1-puzzle1.txt'
total = 0

with open(filepath) as fp:
	line = fp.readline()
	while line:
		total += int(line)
		line = fp.readline()
print("Frequency {}".format(total))
