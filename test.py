def main():
    # hap filet per te lexuar
    temat = open("sqi_lexemes_V.txt", "r")
    fjaletRaw = open("unanalyzed_wordlist.txt", "r")
    fjaletAnal =  open("analyzed_wordlist.txt", "r")

    allAnal = []
    for line in fjaletAnal:
        allAnal.append(line.strip())

    sep1 = allAnal[0]
    list1 = processLine(sep1)
    print(list1)
    print(len(list1))

    # mbyll filet per te lexuar
    temat.close()
    fjaletRaw.close()
    fjaletAnal.close()
    return


# proceson nje linje te nje fjale te analizuar dhe kthen nje liste stringesh me cdo info brenda tageve
# input: line- str
# output: analList - 2D list of str
def processLine(line):
    redundantList = ["/ana", "/w", "w"]
    analList = []

    # parse through the string and fill the information inside the tags in a list, do not include '/ana', '/w', or 'w'
    # as they don't contain any relevant information
    i = 0
    while i < len(line):
        myStr = ""
        if line[i] == "<":
            i += 1
            while line[i] != ">":
                myStr += line[i]
                i += 1
            i += 1
        else:
            while i < len(line) and line[i] != "<":
                myStr += line[i]
                i += 1
        if not (myStr in redundantList):
            analList.append(myStr)
    return analList


# input: wordList - lista qe kthehet nga processLine(line)
# output: newList - liste qe permban veten infot e perpunuara te foljeve
def formatVerbs(wordList):
    newList = []

    for analysis in wordList:
        if 'gr="V, "':
            # process
            analysis.split()



    return newList


if __name__ == "__main__":
    main()
