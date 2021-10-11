# - - coding: utf- 8 - -
#### Key words in python ####

### None
def improper_return_function(a):
    if a % 2 == 0:
        return True

x = improper_return_function(3)
print x

### and, or, not
print True and False
print True or False
print not False

### as
import math as myAlias
print  myAlias.cos(myAlias.pi)

### assert (se usa para debugging, muestra error si la condición es falsa)
a = 4
assert a < 5, "El numero es muy grande"
#assert condition, mesage

#otra forma
if not a < 5:
    raise AssertionError("El numero es muy grande")
    
### break, continue
for i in range(1,11):
    if i == 5:       #se salta el 5 y sale del bucle
        break
    print(i)

for i in range(1,11):
    if i == 5:        #se salta el 5 pero                                               
        continue      #no sale de del bucle
    print(i)    

### del (borra referencia a un objeto)
a = b = 5
del a
#print a
#error, a no esta definida

a = ["l","s","t","u"]
del a[1]
print a
#["x","z"]

### except, raise, try (with errors that suggests something 
                      # went wrong while executing our program.  )
   #IOError, ValueError, ZeroDivisionError, ImportError, NameError, TypeError
def reciprocal(num):
    try:
        r = 1/num
    except:
        print('Exception caught')
        return
    return r

print reciprocal(10)
print reciprocal(0)
#Here, the function reciprocal() returns the reciprocal of the input number.
#When we enter 10, we get the normal output of 0.1. But when we input 0, a ZeroDivisionError is raised automatically.
#This is caught by our try…except block and we return None. We could have also raised the ZeroDivisionError explicitly by checking the input and handled it elsewhere as follows:
def reciprocal(num):
    if num == 0:
        raise ZeroDivisionError('cannot divide')
    r = 1/num
    return r
    
print reciprocal(10)
print reciprocal(1)

### finally
#Using finally ensures that the block of code inside it gets executed even if there is an unhandled exception. For example:
#try:
#    Try-block
#except exception1:
#    Exception1-block
#except exception2:
#    Exception2-block
#else:
#    Else-block
#finally:
#    Finally-block

### global 
#global is used to declare that a variable inside
#the function is global (outside the function).
globvar = 10
def read1():
    print globvar
def write1():
    global globvar
    globvar = 5
def write2():
    globvar = 15

read1()
write1()
read1()
write2()
read1()

### lambda (crea funciones de una sola linea )
f = lambda x: x*2
for z in range (1,6):
    print f(z)

### pass
#Nothing happens when it is executed. It is used as a placeholder
def function(args):
    pass
    
class example:
    pass
    






