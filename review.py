###############################
#                             #
#           Review 2!         #
#                             #
###############################

# Write a program that uses a loop to print out:

#           2
#           4
#           6
#           8
# Who do we appreciate?

# Use a loop to complete this, either a for loop or a while loop.
# Each time through the loop, print out either 2, 4, 6 or 8.
# When the loop is finished, print "Who do we appreciate?"
# Remember how range can be used to create the list [2,4,6,8]
# When complete, commit to github and submit a pull request!
aList = [2,4,6,8,'who do we appreciate?']
counter = -1
keepGoing = True
while (keepGoing):
    counter = counter + 1
    if counter == 5:
        keepGoing = False
    else:
        print aList[counter]