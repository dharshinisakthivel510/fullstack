/******************************************************************************

Welcome to GDB Online.
  GDB online is an online compiler and debugger tool for C, C++, Python, PHP, Ruby, 
  C#, OCaml, VB, Perl, Swift, Prolog, Javascript, Pascal, COBOL, HTML, CSS, JS
  Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
arr = [1,2,3,4,5,6,7]
n = len(arr)
countEven = 0
for i in range(0, n):
    if arr[i]%2==0 :
        countEven += 1
print("Even Elements count : " )
print(countEven)