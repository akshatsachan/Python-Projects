'''
A calculator in Python that calculates arithmetic equations typed in as a string using
the eval() function
Performs addition, subtraction, division and multiplication
'''
import re   #importing the regex module


def perform_math(prev):
    eq = input()    #enter 'quit' to exit the program
    if eq == "quit":
        pass
    else:
        eq = re.sub('[A-Za-z,@,#,$,.?[]{}]','',eq)
        if prev != 0:
            prev = eval(str(prev)+eq)
        else:
            prev = eval(eq)
        print(prev)
        perform_math(prev)


perform_math(0)
