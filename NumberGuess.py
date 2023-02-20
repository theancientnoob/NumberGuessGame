import random
import time

x = True

while x == True:

    userMin = int(input("Type the minimum range."))

    if userMin < 0:

        print("Please enter a natural number (Greater then 0)")

    else:

        userMax = int(input("Type the maximum range."))

        if userMax == userMin:
            print("That number is already set as the minimum value. Try again.")

        elif userMax < userMin:
            print("That number is lesser then the minimum range. Try again.")

        else:

            userVal = int(input("Please type a number which is inside the range that you have set."))


            if userVal < userMin:
                print("That value is lesser then the minimum range. Try again.")

            elif userVal > userMax:
                print("That value is higher then the maximum range. try again.")

            else:

                comp = int(random.randrange(userMin, userMax))

                print("the computer is thinking...")

                time.sleep(1)

                print("the computer is thinking...")

                if comp == userVal:
                    print("holy cow! you are right! Congratulations!")

                if comp > userVal:
                    print("you are close! the number is higher! try again!")

                if comp < userVal:
                    print("You are close! The number is lesser! try again!")









