import random
number="1234567890"
otpg=""
for otp in range(6):
    otpg+=random.choice(number)
print("otp generated is :",otpg)