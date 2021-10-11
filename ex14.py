# - - coding: utf- 8 - - 
from sys import argv
script, user_name = argv
pr = 'Antw. Sie hier > '

print "Hello %s, der script heisst %s." % (user_name, script)
print "Ich mo8chte dir fragen, dass..."
print "Mast du mich %s?" % user_name
likes = raw_input(pr)

print "Wo wohnst du %s?" % user_name
lives = raw_input(pr)

print "Welche Art von Computer hast du?"
computer = raw_input(pr)

print """
Okay, du hast %r daru8ber gesagt, mich zu mo8gen.
Du wohnst in %s. Ich weiss nicht, wo das liegt.
Und du hast ein %r Computer. Toll!.
""" %(likes,lives,computer)    
