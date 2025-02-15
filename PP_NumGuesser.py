
import random

token = 5
user_guess = 0

# this is the random number generator function and stores the value in randomNumIs
def randomNumGen(low_range, high_range):   

    # this is the random number generator and stores the value in randomNumIs
    randomNumIs = random.randint(low_range,high_range)
    
    # this commented code is for testing purposes and display the generated number
    # print("Generated Number: {}" .format(randomNumIs))

    #return the generated number
    return randomNumIs

# this is the range checker function that checks each range and swaps them if needed
def rangeChecker(low_range, high_range):

    # initialize temp variable
    tempSwap = 0
    # print("temp: {}".format(tempSwap))

    # check if low range is greater than high range
    if low_range > high_range:

        # temp variable stores low range
        tempSwap = low_range
        # print("temp: {}".format(tempSwap))

        # low range is equal to high range
        low_range = high_range
        # print("low: {}".format(low_range))

        # high range is equal to temp variable
        high_range = tempSwap
        # print("high: {}".format(high_range))

        # print("Your lowest range has been swapped with your highest range")
        tempSwap = 0
        # print("temp: {}".format(tempSwap))
        
    # if low_range and high_range DO NOT need to swapped return there same values
    else:
       pass

    return low_range, high_range

# this is the user guesser function that checks the user guess against the generated number
def userGuesser(token):
    
    # the users number of attempts are not equal to 0 keep guessing
    while token != 0:

        # print the number of attempts left
        print("Number of attempts left: {}" .format(token))
    
        # prompt the user for their guess
        user_guess = int(input("Please enter your guess: "))
    
        # check if the user guess is incorrect
        if user_guess != generatedNum: 
        
            print("your incorrect")

            # decrease the number of attempts by 1
            token -= 1

        # check if the user guess is correct
        elif user_guess == generatedNum:
        
            return True

        # check if the user has no more attempts
        elif token == 0:
            return False

# this is the prompt function that prompts the user for their range
def prompt():

    print("===================================================================================================\n")

    print("Hello and welcome to random number guesser")

    # prompt the user for their ranges
    low_range = int(input("Please enter your lowest range: "))
    high_range = int(input("Please enter your highest range: "))

    return low_range, high_range

# gather the values from the prompt function and store them in variables
low_range, high_range = prompt()


# gather the values from the range checker function and store them in variables
low_range, high_range = rangeChecker(low_range, high_range)

# gather the values from the random number generator function and store them in variable
generatedNum = randomNumGen(low_range, high_range)

# gather the values from the user guesser function and store them in variable
winLose = userGuesser(token)

# check if the user won or lost
if winLose == True:
    print("You win")
else:
    print("You lose")
    
print("\n===================================================================================================")

