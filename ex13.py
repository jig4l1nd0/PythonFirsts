# - - coding: utf- 8 -- 
from sys import argv

script, first, second, third = argv

print "The script is called:",script 
print "Your first variable is",first
print "Your second variable is",second
print "Your third variable is",third
 
####para correr este programa hay que meterlo en la consola como
#usuarioLinux$ python2 ex13.py arg1 arg2 arg3
#### y entonces no arroja
#The script is called: ex13.py
#Your first variable is arg1
#Your second variable is arg2
#Your third variable is arg3
cosaloca = int(raw_input("Dame un número entero cualquiera y lo duplico: "))
print cosaloca*2

