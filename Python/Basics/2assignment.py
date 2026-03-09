###Write a program to ask for age and print the ticket price.


# age = int(input("enter your age : "))

# if age < 12 :
#     print("ticket price is 100")
# elif age >=12 and age < 18 :
#     print("ticket price is 200")
# elif age >=18 and age <= 60 :
#     print("ticket price is 400")
# else:
#     print("ticket price is 250")


###Take marks and print performance using match-case (Python 3.10+)

# marks = int(input("enter your marks"))

# match marks:
#     case _ if marks >=90 :
#         print("Excellent")
#     case _ if marks <89 and marks >75 :
        
#         print("good")
#     case _ if marks <74 and marks >50 :
        
#         print("Average")
#     case _:
#          print("poor")


###  Smart Elevator System


# while True:
#     floor = int(input("Enter the floor (1-10): "))
#     if 1 <= floor <= 10:
#         print(f"Valid floor number: {floor}")
#         break

#     else:
         
#       print("Invalid input. Please enter an integer.")
    
        


###  OTP Verification Simulation


# OTP ="1234"
# max_attempts = 3
# attempts = 0

# while max_attempts >attempts :
#     user_otp = input("enter otp : ")
#     if user_otp == OTP :
#         print("success")
#         break
#     attempts+= 1

#     return_otp = max_attempts -attempts
#     if return_otp > 0:
#         print(f"incorrect otp {attempts}")
#     else:
#         print("loop fail")


###. Discount Logic for E-Commerce


# amount = int(input("enter amount : "))

# match amount:

#     case _ if amount > 5000:
#         print("gold give  20% discount")

#     case _ if amount<5000 and amount >3000 :
#         print("silver give  10% discount")
#     case _:
#         print(" 5% discount")
        


### Robot Navigation


# corrent_direction = "N"
# sequence = input(f"enter sequence (L,F,R)").strip().upper()

# match sequence:
#     case (N,L):
#         print("W")



####. Banking PIN Validation


# PIN = 1234
# max_attempts = 3
# attempts = 0

# while max_attempts > attempts:

#   correct_pin = int(input("enter your PIN :"))
#   if correct_pin == PIN :
#     print("correct")
#     break
#   attempts+=1
#   return_PIN =max_attempts - attempts
#   if return_PIN>0:
#     print(f"enter youtr pin{attempts}")
#   else:
#     print("account Lock")


#### Movie Recommendation Filter

# genre  = input("enter  genre : ")

# if  genre =='action':
#     print("rating ≥ 8 → “Must Watch”")
# elif genre =='drama':
#     print("rating ≥ 7 → “Recommended””")
# else:
#     print("optional")


###Power Consumption Billing




# unites =int(input("enter electricity units : "))
# if unites>= 100 :
#     print(unites*5)
# elif unites>= 101 and unites <=300:
#     print(unites*8)
# elif unites>= 301 and unites<=500:
#     print(unites*10)
# else:
#     print(unites*100)




###Write a recursive function digital_root(n) that repeatedly sums digits until a single digit remains.
### Example: digital_root(9875) → 2 (9+8+7+5=29 → 2+9=11 → 1+1=2)
 
def digital_root(n):
    return 1 + (n - 1) % 9 
if n != 0:
else:
    0



    ####
    