import time
print "Hello, My name is Pyth"
print "What is your name?",
name = raw_input()
print "Oh, Hi " + name
print "What is yor age?"
age = raw_input()
print "I see"
year = time.strftime("%Y")
print year - age
