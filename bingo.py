#!/usr/bin/python
import sys, random, textwrap, argparse

parser = argparse.ArgumentParser(description='Generate a bingo board!')
parser.add_argument('-f', '--file', nargs='?', const="bingo.list",\
        dest='infile', type=str, required=True, \
        help='File containing list of bingo words')
parser.add_argument('-w', '--width', nargs=1, default="9",\
        dest='width', type=int, help='The width of each cell on the board')
args = parser.parse_args()

print args.infile

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

# Returns a filehandler for the file at the path passed in as "name"
def getFile(name):
    inlist = ""
    try:
        inList = open(name, "r")
        return inList
    except IOError:
        print "sorry, that file doesn't exist"
        sys.exit()

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
    print "=" * (6 + (width * 5))
    print "|" + "B".center(width) + "|" + "I".center(width) + "|" + \
            "N".center(width) + "|" + "G".center(width) + "|" + \
            "O".center(width) + "|"
    print "=" * (6 + (width * 5))
    for i in range(0,5):
        for j in range(0,3):
            print "|" + bingoList[i*5][j].center(width) + "|" + \
            bingoList[(i*5)+1][j].center(width) + "|" + \
            bingoList[(i*5)+2][j].center(width) + "|" + \
            bingoList[(i*5)+3][j].center(width) + "|" + \
            bingoList[(i*5)+4][j].center(width) + "|"
        print "=" * (6 + (width * 5))

# Main stuff
inList = getFile(args.infile)
width = args.width

boardDump(smallWords(getList(inList), width), width)
