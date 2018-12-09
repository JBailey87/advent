import collections
strFilePath = 'input/day2/day2-puzzle.txt'
#strFilePath = 'input/day2/day2-test.txt'
twos = 0
threes = 0

def duplicates(input):
	global twos
	global threes

	oCounter = collections.Counter(input)

	if len({x : oCounter[x] for x in oCounter if oCounter[x] == 2}):
		twos += 1

	if len({x : oCounter[x] for x in oCounter if oCounter[x] == 3}):
		threes += 1

with open(strFilePath) as oFile:
	strFileLine = oFile.readline()

	while strFileLine:
		duplicates(strFileLine)
		strFileLine = oFile.readline().strip()

	print(twos * threes)


