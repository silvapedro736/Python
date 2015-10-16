#Password Cracker
print "Enter a 10 digit number password:"
password = raw_input()

t = 9 * (10**10)

for x in range(t):
    if x == password:
        print "password cracked"
