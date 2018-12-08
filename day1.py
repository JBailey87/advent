import collections
#filepath = 'input/day1/day1-test.txt'
filepath = 'input/day1/day1-puzzle1.txt'
total=0
list = []





def duplicate(frequency):
	if frequency in list:
		raise ValueError("duplicate {}".format(frequency))



with open(filepath) as fp:
	line = fp.readline()
	while line:
		total += int(line)
		line = fp.readline()
	print("Total frequency {}".format(total))

total = 0

while True:
	with open(filepath) as fp:
		line = fp.readline()
		while line:
			total += int(line)
			duplicate(total)
			list.append(total)
			line = fp.readline()
