bingo
=====

An ASCII bingo board generator in Python

Originally written to build boards for buzzword bingo, but I figured it had other uses as well.

## Usage 

``` bash
./bingo.py [-h/--help] [-f/--file <File with list of words>] [-w/--width <Cell Width>]
```

The **-f** flag is to specify list of words. The default tries to use bingo.list in the current directory

The **-w** flag is to specify the width of each cell. The deafault is 9

The **-h** flag displays the help message
