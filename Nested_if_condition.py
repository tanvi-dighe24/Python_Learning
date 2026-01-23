#1
n = input('number: ')
#even or not
if len(n) % 2 == 0:
    print('even length')
    print(n)
else:
    print('odd length')
#o/p:number: 7
#odd length    


#2
char= input('enter single character between a to z')
if len(char)is 1:
    if 65<=ord(char)>=122:
        if char in ('a', 'e', 'i','o','u'):
            print('char is vowel')
        
    else:
        print('char is consonant')
else:
    print('your input char is not alphabet')
#o/p:enter single character between a to zt
#char is consonant    
    
    
#3
username_of_ram='ram123'
password_of_ram='pass@123'
#Ram is trying to sign in 
username=input('enter your instagram username:')
if username == username_of_ram:
    type_password=input('enter your password')
    if type_password==password:
        print('sign in successful')
    else:
        print('wrong password entered by you, try again')
else:
    print('username is invalid, try again')
#o/p:enter your instagram username:sita@123
#username is invalid, try again    
    

#4
d = input('enter string as a data: ')
Englishvowels = 'aeiou'

if type(d) is str:
    if d[0] in Englishvowels:
        if d[-1] not in Englishvowels:
            if len(d) % 2 != 0:
                print('u entered valid data as in d')
            else:
                print('enter odd length of data as d')
        else:
            print('data d does not end with a consonant')
    else:
        print('data d is not starting with a vowel')
#o/p:enter string as a data: 'ghfd'
#data d is not starting with a vowel        

#5
Q1 = input('is student present in class? ')
if Q1 == 'yes':
    Q2 = input('is student awake or not? ')
    if Q2 == 'yes':
        print('attendance succeed')
    else:
        print('canceled student attendance')
else:
    print('today student is absent')
#o/p:is student present in class? yes
#is student awake or not? no
#canceled student attendance    

    
          
                
             
     
       
