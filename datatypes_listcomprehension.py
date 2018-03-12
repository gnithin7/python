#Let's learn about list comprehensions! You are given three integers x,y and z representing the dimensions of a cuboid along with an integer n. You have to print a list of all possible coordinates given by i,j,k on a 3D grid where the sum of i+j+k is not equal to n. Here, 0<=i<=x; 0<=j<=y; 0<=k<=z
#Input Format:
#Four integers x,y,z and n each on four separate lines, respectively.
#Constraints:
#Print the list in lexicographic increasing order.

x = int(input()) + 1;
y = int(input()) + 1;
z = int(input()) + 1;
n = int(input());
arr = [];

for a in range(0,x):
    for b in range(0,y):
        for c in range(0,z): 
            if (a + b + c) != n: 
                arr.append([a,b,c]);
print(arr);