import sys
import os
def wc(filename):               # counts words,lines,characters in a file and print it
    """Counts lines, words, characters in a file and print them to console, or a error
    message if the file is not found.

    Args:
        filename (str): The name of the file to check
    """
    try:
        f = open(filename, "r") # opens the file for reading
    except:                     # if the file does not exist
        print("File not found: {}".format(filename)) 
        return
    words=0
    lines=0
    characters=0
    l = f.readline()                    # reads the first line
    while l:                            # loop for each line in the file
        o = " "                         # o is used to to not count repeated spaces as new words
        for c in l:                     # loop for each character in the file
            if (c == " " and o != " "): # if it reads a space and the previous read character was not a space
                words += 1              # increase word count
            o = c                       # set o as the current character
            characters += 1             # increase character count
        lines += 1                      # finished with one line, increase line count
        words += 1                      # new line means new word aswell
        l = f.readline()                # read next line
    print("{} {} {} {}".format(lines,words,characters,filename))    # prints the data to console


if (os.name == "nt"): # for windows
    try:
        command = sys.argv[1]
    except:     # if sys.argv[1] is empty print a error message and exit
        sys.exit("Not enough arguments")
    
    starIndex = command.find("*")
    if (starIndex != -1):   # if a * was used in the argument
        extToCheck = command[starIndex+1 : len(command) - starIndex] # get the text after the *, for example *.py = .py
        files = os.listdir()                    # all files and directories in the folder where the python script is located
        for f in files:                         # loop through each file/directory
            if os.path.isfile(f):               # check if its a file and not a directory
                ext = os.path.splitext(f)[1]    # get the file extension
                if (ext == extToCheck):         # check if file extension is the same as the one specified in the argument
                    wc(f)
                elif(extToCheck == ""):         # if the argument was only a * do it for all the files
                    wc(f)
    else:                   # if the argument does not contain a *, its a specific file
        wc(command)
else: # on linux * changes the arguments to the filetype specified
    for x in range(len(sys.argv) - 1, 0, -1):
        wc(sys.argv[x])
	
