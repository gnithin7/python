#Rules: We add a Leap Day on February 29, almost every four years. The leap day is an extra, or intercalary day and we add it to the shortest month of the year, February. 
#In the Gregorian calendar three criteria must be taken into account to identify leap years:
#1. The year can be evenly divided by 4, is a leap year, unless:
#2. The year can be evenly divided by 100, it is NOT a leap year, unless:
#3. The year is also evenly divisible by 400. Then it is a leap year.
#This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years.

#Assignment: You are given the year, and you have to write a function to check if the year is leap or not.
#Note that you have to complete the function and remaining code is given as template.
#Input Format
#Read y, the year that needs to be checked.
#Constraints:
#1900<=y<=10^5
#Output Format:
#Output is taken care of by the template. Your function must return a boolean value (True/False)

def is_leap(n):
    if n % 400 == 0: #checking rule #3
        return True
    if n % 100 == 0: #checking rule #2
        return False
    if n % 4 == 0: #checking rule #1
        return True
    return False #base case of false.

print(is_leap(int(input())))