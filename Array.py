#Arrays

#firstname | Lastname | Test1 | Test2 | Test 3
#Don | John | 100 | 50 | 20
#Jack | Joe | 20 | 90 | 100
#Sally | Sue | 85 | 80 | 80

a = [["Don", "John", 100, 50,20], ["Jack", "Joe", 20,90,100], ["Sally", "Sue", 85, 80,80]]
print "Average:"
for i in range(3):
    print a[i][0] + " " + a[i][1] + " has an average grade of ",
    print (a[i][2] + a[i][3] + a[i][4]) / 3.0
