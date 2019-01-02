import collections
strFilePath = 'input/day2/day2-puzzle.txt'
#strFilePath = 'input/day2/day2-test.txt'
#answer is 7470
twos = 0
threes = 0

strIDs = set()

def duplicates(input):
	global twos
	global threes

	oCounter = collections.Counter(input)

	if len({x : oCounter[x] for x in oCounter if oCounter[x] == 2}):
		twos += 1

	if len({x : oCounter[x] for x in oCounter if oCounter[x] == 3}):
		threes += 1

with open(strFilePath) as oFile:
	strFileLine = oFile.readline().strip()

	while strFileLine:
		strIDs.add(strFileLine)
		strFileLine = oFile.readline().strip()


list(map(duplicates,strIDs))
print("answer: {}".format(twos * threes))
