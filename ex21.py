# - - coding: utf- 8 - -
def add(a,b):
    print "Adding %d + %d" % (a,b)
    return a+b
def substract(a,b):
    print "substractinging %d - %d" % (a,b)
    return a-b
def multiply(a,b):
    print "Multiplying %d * %d" % (a,b)
    return a*b
def divide(a,b):
    print "dividing %d / %d" % (a,b)
    return a/b

print  "Lest's do some math with just functions!"

age = add(30,5)
height = substract(78,4)
weight = multiply(90,2)
iq = divide(100,2)

print  "Age: %d, Height: %d, Weight: %d, IQ: %d"% (age, height, weight, iq)

# a puzzle for extra credit,     type it anyway
print "Here is pusle."

what = add(age, substract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"

