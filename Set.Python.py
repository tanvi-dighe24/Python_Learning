Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Set: collection of homogeneous or heterogeneous values.
#Homogeneous: A collection of the same type of values.
#Example: 10, 20, 30, 40
#Heterogeneous: A collection of different types of values.
... 
... #Example: 10, 2.5, 9+6j, True
>>> #Set are enclosed within flower braces { }
>>> #Syntax: Variable name={value1 , value2 ,value3,…….Value n}
>>> #default value of a Set is an empty parenthesis "set( )".
>>> #empty set() is considered False in a Boolean context
>>> #Types of values can we store inside a Set
>>> #We can't store duplicate values. If it store it will remove automatically.
>>> #Modifying Set Elements: add()
>>> #To remove a specific value from a set: remove()
>>> #Syntax: variable name. remove(value)
>>> Q={True, 3.4, 56, 'py', 12, (56+23j)}
>>> Q. remove(3.4)
>>> Q
{True, (56+23j), 56, 12, 'py'}
>>> #To delete default 1st element pop()
>>> S= {12,'tanvee',7.8,(23+8j)}
>>> s.pop()
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    s.pop()
NameError: name 's' is not defined. Did you mean: 'S'?
>>> S.pop()
'tanvee'
>>> S
{12, (23+8j), 7.8}
>>> set1 = {1, 2, 3, 4, 4}
>>> print(set1)
{1, 2, 3, 4}
>>> set1 = {3, 4, 5}
>>> set1.update([1, 2, 3])
>>> print(set1)
{1, 2, 3, 4, 5}
>>> set1 = {1, 2, 3}
>>> set2 = set1.copy()
>>> set2.add(4)
>>> print(set1)
{1, 2, 3}
>>> set2
{1, 2, 3, 4}
>>> set1 = set([1, 2, 4, 4, 3, 3, 3, 6, 5]) 
... set1
SyntaxError: multiple statements found while compiling a single statement
>>> set1 = set([1, 2, 4, 4, 3, 3, 3, 6, 5])
>>> set1
{1, 2, 3, 4, 5, 6}
