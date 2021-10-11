# - - coding: utf- 8 --
from sys import argv
script,filename = argv

txt = open(filename)
print "Here's your file %r" % filename
print txt.read()

print "Type the filename again: "

txt_again = open(raw_input("> "))

print txt_again.read()

txt.close()
txt_again.close()

