#my cade for finding avrage of two numbers
a = int(input("enter first numper\n"))
b = int(input("enter 2nd number\n"))
print((a+b)/2)

''' stackoverflow.com code 
for finding avrage of two numbers'''
#get number 1, number2 as integers
number1 = int(input("Enter number1"))
number2 =int(input("Enter number2"))
#your function as it was
def average(number1, number2):
  return (number1 + number2) / 2
#function `average` returns an int. Store that result in `avg`
avg = average(number1,number2)
#print the result
print(avg)