#  - - coding: utf- 8 - -
#### Dictionaries ####
# create a mapping of state to abbreviation
states = {
     'Oregon':'OR',
     "Florida":"FL",
     "California":"CA",
     "New York":"NY",
     "Michigan":"MI"
}
# create a basic set of states and some cities in them 
cities = {
    "CA":"San Francisco",
    "MI":"Detriot",
    "FL":"Jacksonville"
}
# add some more cities
cities["NY"] = "New York"
cities["OR"] = "Portland"

# printout some cities
print "-"*10
print "NY State has: ", cities["NY"]
print "OR State has: ", cities["OR"]

# print out some states
print "-"*10
print "Michigan's abreviatin is: ",states["Michigan"]
print "Florida's abreviatin is: ",states["Florida"]

# print it using the state then cities dictionaries
print'- '*1033   
print"Michigan has: ", cities[states['Michigan']]
print"Florida has: ", cities[states['Florida']] 
  
# print every state abreviation 
print"-"*10
for state, abbrev in states.items():
    print "%s is abbreviated %s"%(state,abbrev)
    
# print every city in state
for abbrev, city in states.items():
    print "%s has the city: %s"%(abbrev,city)

# now do both at the same time 
print "-"*10
for state, abbrev in states.items():
    print "%s state is bbreviated %s and has the city %s" %(
    state, abbrev, cities[abbrev])

print "-"*10
# safely get an abbreviation by state that might not be there
state=states.get("Texas",None)

if not state:
    print "Sorry, no Tesxas"
    
# get a city with a default value 
city = cities.get("TX","Does Not Exist")
print "The city for the state 'TX' is: %s"%city  

# the dic() constructor biults from sequences of key-value pairs
Tel = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print Tel

# dictionaris comprehension
pow = {x:x**2 for x in {2,4,6}} 
print pow

loco=dict(sape = 3242, guido = 8980, jack = 5758)
print loco

    

