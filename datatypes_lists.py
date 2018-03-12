#Consider a list (list = []). You can perform the following commands:
#1. insert i e: Insert integer e at position i.
#2. print: Print the list.
#3. remove e: Delete the first occurrence of integer e.
#4. append e: Insert integer e at the end of the list.
#5. sort: Sort the list.
#6. pop: Pop the last element from the list.
#7. reverse: Reverse the list.
#Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7 types listed above. Iterate through each command in order and perform the corresponding operation on your list.

#Input Format
#The first line contains an integer, n, denoting the number of commands. 
#Each line i of the n subsequent lines contains one of the commands described above.

x = int(input())
arr = []
for i in range(x):
    reader = input().split()
    if reader[0] == 'print':
        print(arr)
    elif reader[0] == 'append':
        arr.append(int(reader[1]))
    elif reader[0] == 'insert':
        arr.insert(int(reader[1]), int(reader[2]))
    elif reader[0] == 'remove':
        arr.remove(int(reader[1]))
    elif reader[0] == 'pop':
        arr.pop()   
    elif reader[0] == 'sort':
        arr.sort()  
    elif reader[0] == 'reverse':
        arr.reverse()
    
