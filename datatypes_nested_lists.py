#Given the names and grades for each student in a Physics class of n students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
#Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.

#Input Format:
#The first line contains an integer, n, the number of students. 
#The 2n subsequent lines describe each student over 2 lines; the first line contains a student's name, and the second line contains their grade.

#Constraints:
#2<=n<=5
#There will always be one or more students having the second lowest grade.

#Output Format:
#Print the name(s) of any student(s) having the second lowest grade in Physics; if there are multiple students, order their names alphabetically and print each one on a new line.

ru=int(input())
arr=[]
min1=10000000000000000000
min2=10000000000000000

for x in range(ru):
    name=input()
    grade=float(input())
    if(grade<min1):
        min2=min1
        min1=grade
    if(grade<min2 and grade>min1):
        min2=grade
    arr.append([name,grade])
    
arr=sorted(arr)
for x in arr:
    if(x[1]==min2):
        print(x[0])