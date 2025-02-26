Python 3.13.2 (v3.13.2:4f8bb3947cf, Feb  4 2025, 11:51:10) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> class CoffeeShop:
...     def __init__(self):
...         self.menu = {
...             'espresso': 3.50
... Print(Welcome to my Coffee Shop)
...             
SyntaxError: '{' was never closed
>>> Print('Welcome to my coffee shop')
...             
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    Print('Welcome to my coffee shop')
NameError: name 'Print' is not defined. Did you mean: 'print'?
>>> 'Print'('Welcome to my coffee shop')
...             
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    'Print'('Welcome to my coffee shop')
TypeError: 'str' object is not callable
