#if number is equal to 3 then fizz and 5 then buzz
#fizz buzz game
target=100
for number in range(1,target+1):
    if number%3==0 and number%5==0:
        print("Fizz Buzz")
    elif number%3==0:
        print("fizz")
    elif number%5==0:
        print("buzz")
    else:
        print(number)