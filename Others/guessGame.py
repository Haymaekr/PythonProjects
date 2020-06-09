import sys
import random

print("Have you entered two numbers to start the game?")

first = int(sys.argv[1])
last = int(sys.argv[2])

i=True

rand_num = random.randint(first, last)

print(rand_num)
while i==True:
    try:
    	num = int(input("Guess the number\n"))
    	if last<num or num<first:
        	print(f"Enter the number betwee {first} and {last}, try again")
        	continue
  
    	elif num==rand_num:
        	print("Guess is RIGHT!!")
        	break
    except:

    	print("Enter a number (integer) between 1 to 10")
    	continue