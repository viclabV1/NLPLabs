import re

#Input string initially empty, updated via user input (unsurprisingly)
inputString = ""
outputString = "> Hi. Please talk to me"
print(outputString)
#Loop will continue until user types exit, and only exit
while True:
    outputString = "> "
    inputString=input("< ")
    #exit breaks while loop, exits program, input string must be exactly equal to "exit"
    if inputString == "exit":
        break
    #if pattern matches form "I ___ my ____"
    elif re.search(r"I [A-Za-z]+ my [A-za-z]+", inputString):
        outputString += "Why do you say you " + " your " + "?"
    #if pattern matches form "You ___ your ___"
    elif re.search(r"You [A-Za-z]+ your [A-Za-z]+", inputString):
        outputString += "Why do you say I " + " my " + "?"
    #if pattern matches form "We ___ our ___"
    elif re.search(r"We [A-Za-z]+ our [A-Za-z]", inputString):
        outputString += "Why do you say we " + " our " + "?"
    #If no other patterns are matched
    else:
        outputString += "Tell me more."
    print(outputString)
    