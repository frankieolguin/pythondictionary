import json
import difflib as dfl
import time

data=json.load(open("data.json"))

###################################################################################################################

###################################################################################################################

# this is our dictionary word search
# runs in O(n).
def wordSearch(word):
    
    # We check for user input errors
    # All capitilization outcomes are
    # checked
    # We suggest a close match word if
    # the input is not in the list and
    # it has at least 1 close match string
    if word=="":
        return("Empty? OK...")
    word=word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(dfl.get_close_matches(word,data.keys()))>0:
        print("\nDid you mean %s instead?"%dfl.get_close_matches(word,data.keys())[0])
        check=input("Type y if yes.  ")
        if check.lower()=="y":
            return data[dfl.get_close_matches(word,data.keys())[0]]
        else:
            return("%s does not exist in our dictionary...")%word
    else:
        return("%s does not exist in our dictionary...")%word
    return

###################################################################################################################

###################################################################################################################

# This is the start of our main code

print("YOU ARE ENTERING A DICTIONARY REALM...\n")
print("I N C O M I N G    L O A D I N G    S C R E E N")
for i in range(10):
    time.sleep(0.25)
    print(".")
    continue
time.sleep(1)
print("\nYou still there?\n")
while True:
    word = input("Please enter a word you would like\nTo search for in our dictionary.  ")
    output = wordSearch(word)
    print()
    
    # If output contains a list of string definition
    # We print every item in list output
    if type(output)==list:
        for item in output:
            print(". "+ item )
    else:
        print(output)
    
    # We if the user inputs and wishes to search again
    y_or_n = input("\nWould you like to look up another word?\nEnter y if yes.  ")
    if y_or_n.lower() != "y":
        print("\nGoodbye!\n")
        break
    print()
    