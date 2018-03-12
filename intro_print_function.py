#Read an integer n.
#Without using any string methods, try to print the following:
#123...n 
#Note that "..." represents the values in between.

#Input Format:
#The first line contains an integer n.
#Output Format:
#Output the answer as explained in the task.

#Use map function which is: map(function_to_apply, list_of_inputs).
       
func = lambda x:print(x + 1, end='') #define the lambda function.
list(map(func, range(int(input())))) #pass it through the map function.