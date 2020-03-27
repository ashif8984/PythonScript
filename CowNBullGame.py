"""
Create a program that will play the “cows and bulls” game with the user. The game works like this:

Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the user guessed correctly in the correct place, they have a “cow”. For every digit the user guessed correctly in the wrong place is a “bull.” Every time the user makes a guess, tell them how many “cows” and “bulls” they have. Once the user guesses the correct number, the game is over. Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.

Say the number generated by the computer is 1038. An example interaction could look like this:

  Welcome to the Cows and Bulls Game! 
  Enter a number: 
  >>> 1234
  2 cows, 0 bulls
  >>> 1256
  1 cow, 1 bull
  ...
Until the user guesses the number.
"""
import random
def guess_func(orig_number,input_num ):
    count_cow_bull = [0,0] # 0 is for cow(wrong) and 1 is bull(correct)

    for i in range(len(orig_number)):
        if orig_number[i] == input_num[i]:
            count_cow_bull[1] += 1
        else:
            count_cow_bull[0] += 1
    return count_cow_bull

orig_number = str(random.randint(0,99)) #random 2 digit number
print(orig_number)
counter = True
guesses = 0

print("--"*30)
print("Let's play a game of Cowbull!") #explanation
print("-----I will generate a number, and you have to guess the numbers one digit at a time.")
print("-----For every number in the wrong place, you get a cow. For every one in the right place, you get a bull.")
print("-----The game ends when you get 4 bulls!")
print("---Type exit at any prompt to exit.")
print("--"*30)


while counter:

    input_num = str(input("Guess the 4-digit number: "))

    if input_num == "exit":
        break

    compare_count = guess_func(orig_number,input_num )
    guesses += 1

    print("Cows = >" +str(compare_count[0])+ "  "+ "Bulls = >" +str(compare_count[1]) )

    print()

    if compare_count[1] == 2:
        counter = False
        print("You win after" +"  " +str(guesses) +" "+ "Attempt" +"  "+ "And the Number was:" + str(orig_number))
        break

    else:

        print("You did not Guess it right")


