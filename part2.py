"""
check leap year
"""


def function(year):
   
    if year % 4 == 0 and year % 100 != 0:
        print(year, "is a Leap Year")
    elif year % 400 ==0:
        print(year, "is a Leap Year")
    else:
        print(year, "is not a Leap Year")


# User enters the year
year = int(input("Enter Year: "))
function(year)





"""
Check Whether a Number is Even or Odd
"""

a=int(input())
def evenodd(n):
    
    if a%2==0:
        print('EVEN')
    else:
        print('ODD')
evenodd(a)




"""
Check if A Number is Prime or Not
"""

a=int(input())
def prime(n):
    for i in range (2,a):
        if a%i==0:
            print('not Prime')
            break
    else:
            print('Prime')

prime(a)


