#You have a record of n students. Each record contains the student's name, and their percent marks in Maths, Physics and Chemistry. The marks can be floating values. The user enters some integer n followed by the names and marks for n students. You are required to save the record in a dictionary data type. The user then enters a student's name. Output the average percentage marks obtained by that student, correct to two decimal places.

#Input Format:
#The first line contains the integer n, the number of students. The next n lines contains the name and marks obtained by that student separated by a space. The final line contains the name of a particular student previously listed.

#Constraints:
#2<=n<=10
#0<=Marks<=100

#Output Format:
#Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.


line = int(input())
s_dict = dict()

for x in range(line):
    tmp = input().split(' ')
    student = tmp[0]
    s_dict[student] = (float(tmp[1]), float(tmp[2]), float(tmp[3]))
    
student = input()
print('%.2f' % (sum(s_dict[student]) / 3.0))