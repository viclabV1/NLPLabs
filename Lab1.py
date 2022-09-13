import re

#Input string initially empty, updated via user input (unsurprisingly)
inputString = ""
outputString = "> Hi. Please talk to me"
print(outputString)
#Loop will continue until user types exit, and only exit
while True:
    outputString = "> "
    inputString=input("< ")
    #make input string only count first sentence.
    inputString="".join(re.split(r"\.",inputString)[0])
    wordList = list(re.split(r" ", inputString))
    #exit breaks while loop, exits program, input string must be exactly equal to "exit"
    if inputString == "exit":
        break
    #For each of these, I just decided to go with a manual substitution method since it was more efficient effort-wise.
    #If a pattern is detected, I split the input into a list of words and then just use certain indices, since this program only has
    #to respond to very specific prompts. Not very robust, but it works for this purpose.
    #if pattern matches form "I ___ my ____"
    elif re.search(r"I [A-Za-z]+ my [A-Za-z]+", inputString):
        outputString += "Why do you say you " + wordList[1] + " your " + " ".join(wordList[3:]) + "?"
    #if pattern matches form "You ___ your ___"
    elif re.search(r"You [A-Za-z]+ your [A-Za-z]+", inputString):
        outputString += "Why do you say I " + wordList[1] + " my " + " ".join(wordList[3:]) + "?"
    #if pattern matches form "We ___ our ___"
    elif re.search(r"We [A-Za-z]+ our [A-Za-z]+", inputString):
        outputString += "Why do you say we " + wordList[1] + " our " + " ".join(wordList[3:]) + "?"
    #extra case
    elif re.search(r"I really wish [A-Za-z]+", inputString):
        outputString += "Why do you say you wish " + " ".join(wordList[3:]) + "?"
    #If no other patterns are matched
    else:
        outputString += "Tell me more."
    print(outputString)
    