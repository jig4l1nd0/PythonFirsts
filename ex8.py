# - -  coding: utf- 8 - -
formatter = "%r %r %r %r"

print formatter % (1,2,3,4)
print formatter % ("eins","zwei","drei","vier")
print formatter % (True,False,False,True)
print formatter % (formatter,formatter,formatter,formatter)
print formatter% (
    "I had this thing.",
    "That you could type up right.",
    "But it did't sing.",
    "So I said goodnight"
    )
Index=False
print formatter % (
    1,
    True,
    "hello",
    Index
    )
