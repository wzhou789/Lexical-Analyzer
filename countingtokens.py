import re
import sys
import string

keyword = ["if", "then", "else", "begin", "end"]
special = ["(", ")", "[", "]", "+", "-", "=", ",", ";"]

symbolList = []
countList = []
tokenList = []

noKeywords = 0
noIdentifiers = 0
noIntegers = 0
noReals = 0
noSpecials = 0


# Returns true when a string is identified as a type of token.

def isKeyword(s):
    return s in keyword

def isIdentifier(s):
    return s.isidentifier()

def isInteger(s):
    return str(s).isdigit()

def isReal(s):
    try:
        float(str(s))
        return True
    except ValueError:
        return False

def isSpecial(s):
    return s in special


# Open and read a file given as an argument in the command line.

with open(sys.argv[1], 'r') as openFile:
    content = openFile.read()
    
# Split the strings by specific delimiters. Keep only the special characters,
# and put the results into a list.

r = re.split('(\()|(\))|(\,)|(\+)|(-)|(=)|(\[)|(\])|(;)|\n|\t|\s', content)
s = list(filter(None, r))


# Records symbols, their types, and count in respective lists.
# For each string read in, checks what token type they are. Increments that
# token type's counter. If it is not a repeat symbol, add it to the symbol list,
# adds its total occurences to count list, and adds its type to the token list.

for n in range(len(s)):
    if (isKeyword(s[n])):
        noKeywords += 1
        if s[n] not in symbolList:
            symbolList.append(s[n])
            countList.append(s.count(s[n]))
            tokenList.append("Keyword")
    
    elif(isSpecial(s[n])):
        noSpecials += 1
        if s[n] not in symbolList:
            symbolList.append(s[n])
            countList.append(s.count(s[n]))
            tokenList.append("Special")

    elif(isInteger(s[n])):
        noIntegers += 1
        if s[n] not in symbolList:
            symbolList.append(s[n])
            countList.append(s.count(s[n]))
            tokenList.append("Integer")

    elif(isReal(s[n])):
        noReals += 1
        if s[n] not in symbolList:
            symbolList.append(s[n])
            countList.append(s.count(s[n]))
            tokenList.append("Real")

    else:
       noIdentifiers += 1
       if s[n] not in symbolList:
           symbolList.append(s[n])
           countList.append(s.count(s[n]))
           tokenList.append("Identifier")


# Print symbol table and list how many times tokens of each class appeared.
print()
print("Symbol \t\t Count \t\t Token Type")
print("------ \t\t ----- \t\t ----------")
for c1, c2, c3 in zip(symbolList, countList, tokenList):
    print(str(c1)+ '\t\t ' + str(c2) + '\t\t ' + str(c3))
print()
print("Total Keywords: " + str(noKeywords))
print("Total Identifiers: " + str(noIdentifiers))
print("Total Integers: " + str(noIntegers))
print("Total Reals: " + str(noReals))
print("Total Specials: " + str(noSpecials))
