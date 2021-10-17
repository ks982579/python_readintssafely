"""
Write a function able to input integer values and check if they are
withing a specified range.
1.) Accept 3 Arguement: prompt, lower limit, upper limit.
2.) if it is not an integer, tell the user and prompt for another input
3.) If number in not in range, let the user know and prompt for another input
4.) if it's ok, tell the user.
"""

def read_int(minn, maxx):
    #print(pro,minn,maxx)
    needsInput = True
    mesg = "Please enter a value between {} and {}: "
    while needsInput:
        pro = input(mesg.format(minn,maxx))
        try:
            pro = int(pro)
            needInput = False
        except:
            print("Error: non integer value")
            continue
            #If it is not ingeter - next iteration for new value
            
        # If we got an integer value, check range
        lessThanMax = pro <= maxx
        greaterThanMin = pro >= minn
        inRange = lessThanMax and greaterThanMin
        if inRange:
            needsInput = False
            print("Valid Input")
        else:
            print("Input is not in range.")
    print("Exit read_int Function")
    return True
# end fn


# ---------------------------------- #
read_int(5,20)


