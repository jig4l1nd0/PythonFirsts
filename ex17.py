# - - coding: utf- 8 -- 
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Coping from %s to %s" %(from_file, to_file)

in_file = open(from_file) 
indata = in_file.read() 
###alternative to this 2 previous lines
#indata =  open(from_file).read()
### in this case ypu have to erase the line: in_file.close()

print "The input  file is %dbytes long" % len(indata) #len() mide el tamaño del archivo

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input("> ")

out_file = open(to_file, "w")
out_file.write(indata)

print "Alright, all done."

out_file.close()
in_file.close() 

