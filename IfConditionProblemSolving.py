#Check Data is Mutable or Not
data =input('enter ur data')
if type(data) == list or type(data) == dict or type(data) == set:
    print("Mutable")
else:
    print("Immutable")
#O/P:
#enter ur data[1,2,3]
#Immutable
   

#Check char or speacial char
char =input('enter ur char')
if ('a' <= char <= 'z') or ('A' <= char <= 'Z'):
    print("It is an Alphabet")
elif '0' <= char <= '9':
    print("It is a Digit")
else:
    print("It is a Special Character")

#O/P:
#enter ur char'tanvi'
#It is a Special Character

#Even Or Odd
num=input('enter num')    
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
#O/P: error


#Same Memory Location Or NOt
x =input('enter value1')
y =input('enter value2')
if id(x) == id(y):
    print("Same memory location")
else:
    print("Different memory location")

#Positive No. or Negative No.
n=input('enter ur number')
if n >= 0:
    print("n is Positive No.")
else:
    print("n is Negative No.")


#String is Palindrom or Not
string=str(input("enter string"))
reversed_string=string[::-1]
if string==reversed_string:
    print("Ur String is Palindrom")
else:
    print("Ur String is not Palindrom")


#Lenght 2 of Tuple Check its Homogenous or not
#Ask for tuple input
Tuple=tuple(input("enter tuple with lenght2"))
if len(Tuple) == 2:
    print("Length of tuple is correct")
    if type(Tuple[0]) == type(Tuple[1]):
       print("tuple is homogeneous.")
    else:
       print("tuple is not hommogenous")



#list has middle element or not
List=list(input("enter list as ur wish"))
if len(List)%2!=0:
   print("LList has singlee mid element present")
else:
   print("No single mid in list present)")
   
            
           
           
    


    
