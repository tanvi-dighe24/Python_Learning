Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
bill=345.7
pay=int(bill)
pay
345
bill=7879.99
pay
345
pay=int(bill)
>>> pay
7879
>>> integer=123
>>> floatnum=float(integer)
>>> integer
123
>>> floatnum
123.0
>>> complexnum=complex(integer)
>>> complexnum
(123+0j)
>>> boolnum=bool(integer)
>>> boolnum
True
>>> stringnum=str(integer)
>>> stringnum
'123'
>>> string='ram'
>>> integer=str(string)
>>> integer
'ram'
>>> integer=int(string)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    integer=int(string)
ValueError: invalid literal for int() with base 10: 'ram'
>>> integer=int(string)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    integer=int(string)
ValueError: invalid literal for int() with base 10: 'ram'
>>> boolnum=bool(string)
>>> boolnum
True
>>> boolnum=0
>>> type(boolnum)
<class 'int'>
>>> boolnum=false
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    boolnum=false
NameError: name 'false' is not defined. Did you mean: 'False'?
>>> boolmum=False
>>> integer=int(boolnum)
>>> integer
0
