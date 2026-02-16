'''
n = 5
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i + j == n + 1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
#o/p:

        * 
      *   
    *     
  *       
*         


n = 5
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i + j > n + 1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
    
#o/p:

       * 
      * * 
    * * * 
  * * * *
'''

#upper triangle pyramid 
'''n = 5
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i + j < n + 1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
#Hollow square boundary
'''
'''n = 5
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == 1 or i == n or j == 1 or j == n:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()'''
'''
+ + + + + 
+       + 
+       + 
+       + 
+ + + + +

#Plus Symbol (Middle Cross)
n = 5
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == 3 or j == 3:
            print('+', end=' ')
        else:
            print(' ', end=' ')
    print()
    +
    +     
+ + + + + 
    +     
    +

i == 1 or i == n	Horizontal boundaries (Top & Bottom)
j == 1 or j == n	Vertical boundaries (Left & Right)
i == 3	                entire 3rd row (Horizontal bar)
j == 3	                entire 3rd column (Vertical bar)


'''   
'''
#----------------------------------------------------------------
#o/p:1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5

n=5
for i in range(1,n+1):
    for j in range(1,n+1):
        print(j, end=' ')
    print()
#--------------------------------------------------------------------
#o/p:
1 0 0 0 0 
0 1 0 0 0 
0 0 1 0 0 
0 0 0 1 0 
0 0 0 0 1 
n=5
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            print('1', end=' ')
        else:
            print('0', end=' ')
    print()
    

#---------------------------------------------------------   

#Pyramid Star Pattern
n=5
c= n*2-1
for i in range(1,n+1):
    for j in range(1, n+1):
     if i+j > n+1:
      print('*',end=' ')
     else:
      print(' ',end=' ')
    print()  
#O/P:
        * 
      * * 
    * * * 
  * * * * 


n = 5
for i in range(1, n + 1):
    for j in range(1, 2 * n):
        if i == n or i + j == n + 1 or j - i == n - 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()


#O/P:
    *    
   * *   
  *   *  
 *     * 
*********


#Alphabetic Pattern
for i in range(1, 5):
    for j in range(i):
        print(chr(65 + j), end="")
    print()
#Output:
# A
# AB
# ABC
# ABCD
'''

#Reversed No. Pattern
for i in range(5,0,-1):
    for j in range(1,i+1):
        print(j, end=' ')
    print()

#Output:
#1 2 3 4 5 
#1 2 3 4 
#1 2 3 
#1 2 
#1

    
    




















    

    
    
