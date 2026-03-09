##If / Elif / Else 

##Q1. Write a Python program to check if a number entered by the user is positive, negative, or zero.


# number = float(input("Enter Number : "))

# if number > 0:
#     print("Positive")
# elif number <0:
#     print("Negative")
# else:
#     print("zero")

## Q2. Accept a user’s age and print:
## •	"Child" if below 13
# #•	"Teenager" if between 13–19
# #•	"Adult" if 20 or above


# Age = int(input("enter age : "))

# if Age <=13 :
#     print("Child")
# elif Age >13 and Age <=19 :
#     print("Teenager")
# else:
#     print("Adult")

##Q3. Input two numbers and print the larger one using an if-else statement.



# a= int(input("enter number :-"))
# b = int(input("enter number :-"))
# if a > b :
#     print("a is large number")
# else:
#     print("b is large number")

###Q4. Input a number and check if it’s even or odd.


# a= int(input("enter number :-"))
# list = [2,4,6,8,0]

# if a % 2 == 0 :
#     print("even")
# else:
#     print("odd")

 

##A student’s marks are entered.
## Print the grade based on this rule:
## 90–100 → A  
## 75–89  → B  
## 50–74  → C  
# #Below 50 → Fail


# marks = int(input("enter marks"))

# if marks >= 90 :
#     print("A")
# elif marks> 75 and marks <89 :
#     print("B")
# elif marks> 50 and marks <74 :
#     print("C")
# else:
#     print("Fail")

##Q6. Take a year as input and check if it’s a leap year.
##(A leap year is divisible by 4, but not by 100 unless divisible by 400.)


# year = int(input("enter year :"))

# if year % 4 ==0:
#     print("leap year")
# else :
#     print("normal year")

##Q7. Write a program to find the smallest of three numbers using if-elif-else.

# a = int(input("enter the number a = "))
# b = int(input("enter the number b = "))
# c = int(input("enter the number c = "))

# if a < b and a < c:
#     print("a is small")
# elif b<a and b<c:
#     print("b is small")
# else:
#     print("c is small")


##Q8. Take the temperature as input.
##Print:
##•	"Cold" if < 15
##•	"Pleasant" if 15–30
##•	"Hot" if > 30


# temp = int(input("enter temp"))

# if temp >30 :
#     print("hot")
# elif temp >15 and temp <30 :
#     print("Pleasant")
# else:
#     print("cold")


##Q9. Check if a given character is a vowel or consonant.


# char =  input("enter value ")
# vowel = ["a","e","i","o","u"]

# if char in vowel:
#     print("vowel")
# else:
#     print("consonant")


##Q10. Input an integer and check:
##•	If divisible by both 3 and 5 → print "FizzBuzz"
##•	If divisible by only 3 → print "Fizz"
##•	If divisible by only 5 → print "Buzz"

# number = int(input(" enter value "))

# if number % 3 == 0 and number % 5 == 0:
#     print("FizzBuzz")
# elif number % 3 == 0 and number % 5 ==1:
#     print("Fizz")
# else:
#     print("Buzz")
