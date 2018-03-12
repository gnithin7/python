#Assignment:
#Given an integer, n, perform the following conditional actions:
#If n is odd, print Weird
#If n is even and in the inclusive range of 2 to 5, print Not Weird
#If n is even and in the inclusive range of 6 to 20, print Weird
#If n is even and greater than 20, print Not Weird
#Input Format: A single line containing a positive integer, n.

num = int(input())
mod = num % 2 #makes checking number easier.
if mod > 0: #checking whether input is odd.
    print("Weird") 
elif mod == 0 and 2 <= num <= 5: #checking if input is even and in the range of 2 to 5.
    print("Not Weird")
elif mod == 0 and 6 <= num <= 20: #checking if input is even and in the range of 6 to 20.
    print ("Weird")
elif mod == 0 and num > 20: #checking if input is even and greater than 20.
    print ("Not Weird")