#input():which is used collect the datta from the user.


#syntax: vaiablename=input('message')


#note:input() will store the data by default in string



#print():itis used to print output


#syntax:print(val1,val2....valn,sep=' ',end='\n')





print(10+20)


a=100


b=5.5


print(a-b)



n=int(input('enter your data:'))


m=float(input('enter your data2:'))



print(n+m)



a=int(input('enter your data:'))


b=float(input('enter your data2:'))


c=complex(input('enter your data2:'))


d=bool(input('enter your data2:'))



f=list(input('enter your data2:'))


print(f)


g=tuple(input('enter your data2:'))


print(g)


h=set(input('enter your data2:'))


print(h)


i=dict(input('enter your data2:'))


print(i)




#eval():syntax:ariablename=eval(input('enter your data:'))



#m=eval(input('enter the data:'))


print(1,2,3,4,5,end='@',sep='#')


#print('sleping')




#task


1@2@4@@5 good morining




#Control Statements:


1.conditional statements:


    *simple if


    *if else


    *elif


    *nested if


2.looping statements:


    *while loop


    *for loop




#simple if:


#syntax: if codition:



        #<---> instructions




#1.wap to print the user enterer data is float or not



n=eval(input('enter the data:'))


if type(n)==float:


    print('it is a float')



#2.wap to check whther the user enter data is muatable or not


n=eval(input('enter the data:'))


if type(n) in [list,set,dict]:


    print('mutable')




#3.wap to check whether the user enter digit is even or not


n=int(input('enter the number:'))


if n%2==0:


    print('it is a even number')




#wap to check whther the user enter data is single value data type or not


n=eval(input('enter the data:'))


if type(n) in [int,float,complex,bool]:


    print('single value data type')



#wap to check whether the user enter character is upper case or not
n=input('enter the char:')


if 'A'<=n<='Z':
    print('upper case')

#2.if else:

#syntax: if condition:

<-->  instructions/True statement block


         else:


             instructions/False statement block


n=eval(input('enter the data:'))

if type(n)==float:


    print('it is a float')


else:


    print('it is not a float')



    

n=eval(input('enter the data:'))


if type(n) in [int,float,complex,bool]:


    print('single value data type')


else:


    print('collection')

