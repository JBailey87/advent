import collections
#filepath = 'input/day1/day1-test.txt'
strFilepath = 'input/day1/day1-puzzle1.txt'
intTotalFrequency = 0
intFrequencyList = []

def duplicate(intFrequency):
	if intFrequency in intFrequencyList:
		raise ValueError("Duplicate frequency found {}".format(intFrequency))

with open(strFilepath) as oFile:
	strFileLine = oFile.readline()
	while strFileLine:
		intTotalFrequency += int(strFileLine)
		strFileLine = oFile.readline()
	print("Total Frequency {}".format(intTotalFrequency))

intTotalFrequency = 0

while True:
	with open(strFilepath) as oFile:
		strFileLine = oFile.readline()
		while strFileLine:
			intTotalFrequency += int(strFileLine)
			duplicate(intTotalFrequency)
			intFrequencyList.append(intTotalFrequency)
			strFileLine = oFile.readline()
