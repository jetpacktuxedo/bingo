#!/usr/bin/env python

import sys, os, random, textwrap, argparse

# enforces that the width argument is above 0
def width_type(w):
  w = int(w)
  if w <= 0:
    raise argparse.ArgumentTypeError("width must be above 0")
  return w

# Reads inFile and converts each line in the file into a list, which is
# then shuffled before being returned
def getList(inFile):
  if inFile == None:
    try:
      inFile = open('bingo.list', 'r');
    except IOError:
      print("There doesn't seem to be an accessible bingo.list file\
          in this directory: '{}'".format(os.getcwd()))
      sys.exit()
  try:
    bingoList = inFile.readlines()
  except KeyboardInterrupt:
    print("KeyboardInterrupt")
    sys.exit()
  finally:
    inFile.close()
  if len(bingoList) < 24:
    print("Must provide at leaste 24 words/phrases")
    sys.exit()
  for index, var in enumerate(bingoList):
    bingoList[index] = var.replace("\n", "")
  bingoList = filter(None, bingoList)
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
def main():
  parser = argparse.ArgumentParser(description='Generate a bingo board!')
  parser.add_argument('-f', '--file', default=sys.stdin, nargs='?', \
      dest='infile', type=argparse.FileType('r'),\
      help='File containing the list of bingo words')
  parser.add_argument('-w', '--width', type=width_type, dest='width', \
      default=9, help='The width of each cell on the board (default: 9)')
  args = parser.parse_args()

  boardDump(smallWords(getList(args.infile), args.width), args.width)

if __name__ == '__main__':
  main()
