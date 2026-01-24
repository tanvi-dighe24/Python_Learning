#looping statments:

#While loop:it is a phenomenon of performing a task again and gain.....


#syntax:
#intialization
while condition:  


        instructions....


        updation


#wap to eat panipuri 10 times
num=int(input('enter you panipuri count:'))#10


i=1


while i<=num:


        print('byya thoda pyaaz dalo... ...')


        i=i+1


#wap to print all the number which are multiple of 5 between  1 to n
5,10,15,20.....
n=int(input('enter a number:'))


i=1


while 1<=n:


    if i%5==0:


        print(i)


    i=i+1


#wap to print n natural numbers
#1.wap to print multiplication table for n


example: n=5,i=1



5X1=5


5X2=10


.


.


.


.


.


5X10=50



n=5


i=1


while i<=10:


    print(n,'X',i,'=',n*i)


    i=i+1




#2.wap to print numbers from n to 1


#example: n=100


#100 99 98 97 96 5 94 93....




n=100


i=1


while i<n:


    print(n-i)


    i=i+1 



i = 100


while i >= 1:


    print(i,end=' ')


    i -= 1





#wap to print every char from the given string


apple-->


a


p


p


l




n='Apple'


i=0


while i<len(n):


    print(n[i])


    i=i+1


'''


#4.wap to convert uppercase to lower cse and lower to upper case in given string



example:pyTHon-->

#5.wap to extract the uppercase characters from the given string

n='APPle'


i=0


while i<len(n):


    if 'A'<=n[i]<='Z':


        print(n[i])

