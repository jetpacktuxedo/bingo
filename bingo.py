#!/usr/bin/env python

import sys, random, textwrap, argparse

# enforces that the width argument is above 0
def width_type(w):
	w = int(w)
	if w <= 0:
		raise argparse.ArgumentTypeError("width must be above 0")
	return w

# Reads inFile and converts each line in the file into a list, which is
# then shuffled before being returned
def getList(inFile):
    if inFile != "":
        bingoList = inFile.readlines()
        inFile.close()
        for index, var in enumerate(bingoList):
            bingoList[index] = var.replace("\n", "")
        random.shuffle(bingoList)
        bingoList.insert(12, "FREE SPACE")
        return bingoList[:25]

# Breaks each entry in the input list into chunks. Returns a list 
# of list chunks
def smallWords(bingoList, chunkSize):
    for index, var in enumerate(bingoList):
        temp = textwrap.wrap(var, chunkSize)
        while len(temp) < 3:
            temp.append(" ")
        bingoList[index] = temp
    return bingoList

def boardDump(bingoList, width):
    print("=" * (6 + (width * 5)))
    print("|" + "B".center(width) + "|" + "I".center(width) + "|" + \
            "N".center(width) + "|" + "G".center(width) + "|" + \
            "O".center(width) + "|")
    print("=" * (6 + (width * 5)))
    for i in range(0,5):
        for j in range(0,3):
            print("|" + bingoList[i*5][j].center(width) + "|" + \
            bingoList[(i*5)+1][j].center(width) + "|" + \
            bingoList[(i*5)+2][j].center(width) + "|" + \
            bingoList[(i*5)+3][j].center(width) + "|" + \
            bingoList[(i*5)+4][j].center(width) + "|")
        print("=" * (6 + (width * 5)))

# Main stuff
parser = argparse.ArgumentParser(description='Generate a bingo board!')
parser.add_argument('-f', '--file', default="bingo.list", dest='infile', \
        help='File containing the list of bingo words')
parser.add_argument('-w', '--width', dest='width', default=9, 
		type=width_type, \
		help='The width of each cell on the board (default: 9)')
args = parser.parse_args()

try:
	with open(args.infile, 'r') as inList:
		width = args.width
		boardDump(smallWords(getList(inList), width), width)
except IOError:
	print("Sorry, I can't open file: '{}'".format(args.infile))
