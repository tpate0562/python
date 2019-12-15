#This was made in repl.it by Tejas Patel Using Python v3
import random
tries=0
number=random.randint(1, 1000)
EntryQuestion=input("Hello, What should I call you?")
print("Hello,", EntryQuestion, "I am thinking of a number between 1 and 1000.")
guess=int(input("Have a guess:"))
while guess!=number:
  if guess>number:
    print("Guess Lower")
    tries+=1
    guess=int(input("Have a guess:"))
  if guess<number:
    print("Guess Higher")
    tries+=1
    guess=int(input("Have a guess:"))
if guess==number:
  print(" Congratulations! The number was", number, "and your guessed it in", tries, "tries!")
