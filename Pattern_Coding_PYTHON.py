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
'''

n = 5
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i + j > n + 1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
#o/p:
'''
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
    

























    

    
    
