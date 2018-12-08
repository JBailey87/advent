import collections
#filepath = 'input/day1/day1-test.txt'
filepath = 'input/day1/day1-puzzle1.txt'
intTotalFrequency = 0
intFrequencyList = []

def duplicate(frequency):
	if frequency in list:
		raise ValueError("Duplicate frequency found {}".format(frequency))

with open(filepath) as fp:
	line = fp.readline()
	while line:
		intTotalFrequency += int(line)
		line = fp.readline()
	print("Total Frequency {}".format(intTotalFrequency))

intTotalFrequency = 0

while True:
	with open(filepath) as oFile:
		strFileLine = oFile.readline()
		while line:
			intTotalFrequency += int(strFileLine)
			duplicate(intTotalFrequency)
			intFrequencyList.append(intTotalFrequency)
			strFileLine = oFile.readline()
