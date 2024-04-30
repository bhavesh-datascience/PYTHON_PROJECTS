#4 digit otp generator 
import random
number="1234567890"
otpg=""
for otp in range(4):
    otpg+=random.choice(number)
print(f"otp generated is :{otpg}")
#6 digit otp generator
import random
number="1234567890"
otpg=""
for otp in range(6):
    otpg+=random.choice(number)
print("otp generated is :",otpg)
#otp genrator taking user length
import random
number="1234567890"
otpg=""
length=int(input("Enter The Lenght Of the OTP to be genrated : "))
for otp in range(length):
    otpg+=random.choice(number)
print("otp generated is :",otpg)