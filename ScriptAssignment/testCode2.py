

# a note, single line

"""This is also a note
and it can continue
to be a longer note
"""

##Use Alt-3 to turn this into a note, alt-4 to turn back into line of code


def printMe():
    """this is a docstring - this is a note for the user not for the code writer, to explain the purpose of the function"""

    print("a string")

print(printMe.__doc__)
