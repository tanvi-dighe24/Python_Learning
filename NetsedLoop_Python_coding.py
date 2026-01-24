#Nested If:writing a condition inside another condition.


Syntax: if condition1:


        <-->  if condition2:


              <--> if condition n:


                      <--> instructions


                    else:


                        instructions


                else:


                    instruction


        else:


            instructions



    



#wap to print the number is positive or negative.
n=eval(int('enter the data:'))


if type(n)==int:


    if n>0:


        print('positive')


    else:


        print('negative')



else:


    print('it is not integer data type')





#wap to print the user enter data is it uppercase or lower case character
n=eval(int('enter the data:'))


if type(n)==str:


    if 'A'<=n<='Z':


        print('upper')


    else:


        print('lower')



else:


    print('it is a not a string')





#wap to print the value as it  is if the length of the value is even.

value=eval(input('enter the data:'))


if len(value)>0:


    if len(value)%2==0:


        print('value is', value)


    else:


        print('the length odd')




else:


    print('empty input')


#wap to check whether the character is vowel or consonant.

n=eval(input('enter a character:'))


if 'A'<=n<='Z' or 'a'<=n<='z':


    if n in 'AEIOUaeiou':


        print('vowel')



    else:


        print('Consonant')


else:


    print('may be its digit or special character')


    









