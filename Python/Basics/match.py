# day = 4
# match day:
#     case 1:
#         print("1")
#     case 2:
#         print("2")
#     case _:
#         print("3")

# number = input()
# match number:

#     case 1:
#         print(1)
#     case 2:
#         print(2)
#     case 3:
#         print(3)



##Part B – Match Case (5 Questions)

##Q11. Create a simple calculator using match case.
##Input: two numbers and an operator (+, -, *, /)
##Output: perform and display the result.


# num1 = int(input("enter first number : "))
# num2 = int(input("enter second number : "))
# operator = input("enter +,-,*,/")


# match operator:

#     case '+':
#         print(num2+num1)
#     case '-':
#         print(num1-num2)
#     case '*':
#         print(num1 * num2)
#     case '/':
#         print(num1/num2)
#     case _:
#         print("ERROR")




# #Q12. Using match, take a number (1–7) and print the day of the week.

# number = int(input("Enter the number 1 to 7 :"))

# match number:
#     case 1:
#         print("sun")
#     case 2:
#         print("mon")
#     case 3:
#         print("tus")
#     case 4:
#         print("wen")
#     case 5:
#         print("thu")
#     case 6:
#         print("fri")
#     case 7:
#         print("sat")
#     case _:
#         print("error")



## Q13. Using match, input a grade letter (A/B/C/D/F) and print:
## •	“Excellent” for A
# #•	“Good” for B
# #•	“Average” for C
# #•	“Poor” for D
# #•	“Fail” for F


# grade = input("Enter th grade value (A/B/C/D/F):")

# match grade :
#     case "A" :
#         print("Excellent")
#     case "B":
#         print("Good")
#     case "C":
#         print("Average")
#     case "D":
#         print("Poor")
#     case "F":
#         print("Fail")
#     case _:
#         print("error")


###Q14. Using match, take a number (1–12) and print the month name.



# month = int(input("Enter number (1-12)"))

# match month:
#     case 1:
#         print("Jan1")
#     case 2:
#         print("Jan4")
#     case 3:
#         print("Jan3")
#     case 4:
#         print("Jan")
#     case 5:
#         print("Jan5")
#     case 6:
#         print("Jan6")
#     case 7:
#         print("Jan7")
#     case 8:
#         print("Jan8")
#     case 9:
#         print("Jan9")
#     case 10:
#         print("Jan0")
#     case 11:
#         print("Jan22")
#     case 12:
#         print("Jan12")
#     case _:
#         print("error")



#####Q15. Using match, take a fruit name and print its color.
# #Example:
# #Apple → Red  
# #Banana → Yellow  
# #Grapes → Green or Purple  


# fruit = input("enter fruit name : ")

# match   fruit:
#     case "Apple":
#         print("Red")
#     case "Banana":
#         print("Yellow")
#     case "Grapes":
#         print("Green")
#     case _:
#         print("error")