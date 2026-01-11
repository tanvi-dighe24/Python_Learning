Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> thislist = ["apple", "banana", "cherry"]
>>> mylist = thislist.copy()
>>> print(mylist)
['apple', 'banana', 'cherry']
>>> l1 = [1, 2, [3, 4]]
>>> l2 = copy.copy(l1)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    l2 = copy.copy(l1)
NameError: name 'copy' is not defined. Did you forget to import 'copy'?
>>> import copy
>>> l1 = [1, 2, [3, 4]]
>>> l2 = copy.copy(l1)
>>> l2[2][0] = 99
>>> print(l1)
[1, 2, [99, 4]]
>>> #l2 = copy.copy(l1) creates a shallow copy.
>>> #Syntax of Python Deepcopy
>>> #copy.deepcopy()
>>> import copy
>>> a = [[1, 2, 3], [4, 5, 6]]
>>> b = copy.deepcopy(a) #Creating a deep copy of the nested list 'a'
>>> b[0][0] = 99         #Modifying an element in the deep-copied list
>>> print(b)
[[99, 2, 3], [4, 5, 6]]
>>> #Syntax of Python Shallowcopy: copy.copy()
>>> import copy
>>> a = [[1, 2, 3], [4, 5, 6]]
>>> b = copy.copy(a)     # Modifying an element in the shallow-copied list
>>> print(b)             # Printing the original and shallow-copied lists
[[1, 2, 3], [4, 5, 6]]
>>> #A shallow copy only copies the outer structure, retaining references to the nested objects. In this case, the inner lists are shared between original and shallow_copied.
... 
... #As a result, changes to the nested elements in shallow_copied (e.g., modifying #shallow_copied[0][0]) are also reflected in original.
>>> #As a result, changes to the nested elements in shallow_copied (e.g., modifying #shallow_copied[0][0]) are also reflected in original
>>> 
>>> 
>>> #Deep copy: A deep copy creates a new compound object before inserting copies of the items found in the original into it in a recursive manner.
>>> #It will first construct a new collection object and then recursively populate it with copies of the child objects found in the original. It means that any changes made to a copy of the object do not reflect in the original object.
>>> #copy.deepcopy() ...syntax of deep copy
