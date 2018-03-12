#Read two integers from STDIN and print three lines where:
#1. The first line contains the sum of the two numbers.
#2. The second line contains the difference of the two numbers (first - second).
#3. The third line contains the product of the two numbers.
#Input Format: The first line contains the first integer, b.
#Constraints: 
#1<=a<=10^10
#a<=b<=10^10

num1 = int(input()) #read first input
num2 = int(input()) #read second input
print(num1 + num2) #print sum of inputs
print(num1 - num2) #print difference of inputs
print(num1 * num2) #print product of inputs