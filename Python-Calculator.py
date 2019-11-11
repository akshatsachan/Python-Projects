import re


def perform_math(prev):
    run = True
    eq = input()
    if eq == "quit":
        rum = False
    else:
        eq=re.sub('[A-Za-z,@,#,$,.?[]{}]','',eq)
        if prev!=0:
            prev=eval(str(prev)+eq)
        else:
            prev=eval(eq)
        print(prev)
        perform_math(prev)


perform_math(0)