# - - coding: utf- 8 - -
#### funciones en python wow!

### Esta es como los anteriores usando el 'argv'
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)
    
### okay, lo de antes es pura basura,
### podemos sustituirlo po rlo siguiente
def print_two_again(arg1,arg2):
    print "arg1: %r, arg2: %r" %(arg1,arg2)
    
### Lo que sigue solo toma un argumento 
def print_one(arg1):
    print "arg1: %r" % arg1 
    
### Este no tiene argumentos
def print_none():
    print "Tengo fe en que lo logrará."
    
print_two("Misaka","Touma")
print_two_again("Misaka","Touma")
print_one("Cuarta temporada!")
print_none()

          
