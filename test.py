import random 

points = 0

while True:

    number = random.randint(1, 10)
    user_guess = int(input("Write a number between 1 to 10: "))
    if user_guess == number:
        print("You got the number right")
        points += 1
    else:
        print("Number was: ", number)

    cont = input("Do you want to continue to play (yn)? ")
    if cont == "n":
        print("Your points: ", points)
        break
