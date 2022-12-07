# DATETIME Challenge
#
# Version: Python 3.11.0
#
# Prompt:   Create a script that will find out the current times
#           in the Portland HQ and NYC and London branches. Then,
#           compare that time with each branch's hours to see if
#           they are open or closed. Print out to the screen the
#           three branches and whether they are open or closed.
#

from datetime import datetime
import pytz

Portland = datetime.now(pytz.timezone("America/Los_Angeles"))

NewYork = datetime.now(pytz.timezone("America/New_York"))

London = datetime.now(pytz.timezone("Europe/London"))


def PDXcheckOpen():
    hour = int(Portland.strftime("%H%M"))
    if hour > 900 and hour < 1700:
        print('Portland is OPEN\n')
    else:
        print('Portland is CLOSED\n')

def NYcheckOpen():
    hour = int(NewYork.strftime("%H%M"))
    if hour > 900 and hour < 1700:
        print('New York is OPEN\n')
    else:
        print('New York is CLOSED\n')

def LDcheckOpen():
    hour = int(London.strftime("%H%M"))
    if hour > 900 and hour < 1700:
        print('London is OPEN\n')
    else:
        print('London is CLOSED\n')



if __name__ == "__main__":
    print(("In Portland, it is currently "),Portland.strftime("%I:%M%p"))
    PDXcheckOpen()
    print(("In New York, it is currently "),NewYork.strftime("%I:%M%p"))
    NYcheckOpen()
    print(("In London, it is currently "),London.strftime("%I:%M%p"))
    LDcheckOpen()
